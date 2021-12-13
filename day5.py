def num_overlapping_points():
    points = set()
    duplicates = set()
    with open('inputs/day5.txt') as f:
        for line in f.readlines():
            first = line[:line.index(" ")]
            after = line[line.index(" ") + 3:]
            first_coord = tuple([int(x.strip()) for x in first.split(',')])
            second_coord = tuple([int(x.strip()) for x in after.split(',')])

            if first_coord[0] == second_coord[0]:
                lesser = min(first_coord[1], second_coord[1])
                greater = second_coord[1] if lesser == first_coord[1] else first_coord[1]
                for i in range(lesser, greater + 1):
                    point = (first_coord[0], i)
                    if point in points:
                        duplicates.add(point)
                    points.add(point)
            elif first_coord[1] == second_coord[1]:
                lesser = min(first_coord[0], second_coord[0])
                greater = second_coord[0] if lesser == first_coord[0] else first_coord[0]
                for i in range(lesser, greater + 1):
                    point = (i, first_coord[1])
                    if point in points:
                        duplicates.add(point)
                    points.add(point)

    return len(duplicates)


def num_overlapping_points_with_diagonal():
    points = set()
    duplicates = set()
    with open('inputs/day5.txt') as f:
        for line in f.readlines():
            first = line[:line.index(" ")]
            after = line[line.index(" ") + 3:]
            first_coord = tuple([int(x.strip()) for x in first.split(',')])
            second_coord = tuple([int(x.strip()) for x in after.split(',')])

            curr_x, curr_y = first_coord
            if first_coord[0] == second_coord[0]:
                x_multiplier = 0
            elif first_coord[0] < second_coord[0]:
                x_multiplier = 1
            else:
                x_multiplier = -1

            if first_coord[1] == second_coord[1]:
                y_multiplier = 0
            elif first_coord[1] < second_coord[1]:
                y_multiplier = 1
            else:
                y_multiplier = -1

            while curr_x != second_coord[0] or curr_y != second_coord[1]:
                point = (curr_x, curr_y)
                if point in points:
                    duplicates.add(point)
                points.add(point)
                curr_x += 1 * x_multiplier
                curr_y += 1 * y_multiplier
            point = (curr_x, curr_y)
            if point in points:
                duplicates.add(point)
            points.add(point)
    return len(duplicates)