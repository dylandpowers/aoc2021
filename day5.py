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
            
    return len(duplicates)