from numpy import prod


def add_version_numbers(transmission, start):
    """
    Every packet begins with standard header: 3 version bits, then 3 type ID
    If type id == 4, then
    """
    total_version = int(transmission[start:start + 3], 2)
    packet_type = transmission[start + 3:start + 6]

    # Advance the pointer past the header
    pointer = start + 6
    if int(packet_type, 2) == 4:
        # The literal value starts here
        while transmission[pointer] == '1':
            # Increments of 5 bits
            pointer += 5
        # Now, get to the end of the literal
        pointer += 5
    else:
        # This is an operator packet
        length_type_id = transmission[pointer]
        pointer += 1
        if length_type_id == '0':
            # Next 15 bits represent total length in bits to advance the pointer
            num_bits = int(transmission[pointer:pointer + 15], 2)
            pointer += 15

            new_pointer = pointer
            while True:
                (version, new_pointer) = add_version_numbers(transmission, new_pointer)
                total_version += version
                if new_pointer - pointer == num_bits:
                    pointer = new_pointer
                    break

        else:
            # Next 11 bits represent number of sub-packets contained by this packet
            num_packets = int(transmission[pointer: pointer + 11], 2)
            pointer += 11
            for _ in range(num_packets):
                (version, new_pointer) = add_version_numbers(transmission, pointer)
                total_version += version
                pointer = new_pointer

    return total_version, pointer


def evaluate_expression(transmission, pointer):
    packet_type_id = int(transmission[pointer + 3:pointer + 6], 2)

    pointer += 6
    if packet_type_id == 4:
        # Literal value
        value = ""
        while transmission[pointer] == '1':
            value += transmission[pointer + 1:pointer + 5]
            pointer += 5
        value += transmission[pointer + 1:pointer + 5]
        pointer += 5
        return int(value, 2), pointer

    # The next bit is the length type id for the operator packet
    subs = []
    length_type_id = transmission[pointer]
    pointer += 1
    if length_type_id == '0':
        # Next 15 bits represent number of bits to process
        num_bits = int(transmission[pointer:pointer + 15], 2)
        pointer += 15
        new_pointer = pointer
        while True:
            sub, new_pointer = evaluate_expression(transmission, new_pointer)
            subs.append(sub)
            if new_pointer - pointer == num_bits:
                break
    else:
        # Next 11 bits represent number of packets to process
        num_packets = int(transmission[pointer:pointer + 11], 2)
        pointer += 11
        new_pointer = pointer
        for _ in range(num_packets):
            sub, new_pointer = evaluate_expression(transmission, new_pointer)
            subs.append(sub)

    return calculate_value(subs, packet_type_id), new_pointer


def calculate_value(sub_packets, packet_type_id):
    if packet_type_id == 0:
        return sum(sub_packets)
    if packet_type_id == 1:
        return prod(sub_packets)
    if packet_type_id == 2:
        return min(sub_packets)
    if packet_type_id == 3:
        return max(sub_packets)
    if packet_type_id == 5:
        return int(sub_packets[0] > sub_packets[1])
    if packet_type_id == 6:
        return int(sub_packets[0] < sub_packets[1])
    return int(sub_packets[0] == sub_packets[1])


def convert_transmission_to_binary(transmission):
    return ''.join([bin(int(c, 16))[2:].zfill(4) for c in transmission])


def main():
    with open('inputs/day16.txt') as f:
        transmission = f.readline().strip()
    t = convert_transmission_to_binary(transmission)
    # print(add_version_numbers(t, 0)[0])
    print(evaluate_expression(t, 0)[0])


if __name__ == '__main__':
    main()
