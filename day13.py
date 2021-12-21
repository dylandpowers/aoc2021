FOLD_INDEX = len("fold along ")


def dots_after_first_fold(paper, fold):
    ax, val = fold
    new_points = set()
    for (x, y) in paper:
        if ax == 'x':
            x_coord = x if x < val else val - (x - val)
            new_points.add((x_coord, y))
        else:
            y_coord = y if y < val else val - (y - val)
            new_points.add((x, y_coord))
    return len(new_points)


def print_unlock_code(paper, all_folds):
    points = set(paper)
    for fold in all_folds:
        ax, val = fold
        new_points = set()
        for (x, y) in points:
            if ax == 'x':
                x_coord = x if x < val else val - (x - val)
                new_points.add((x_coord, y))
            else:
                y_coord = y if y < val else val - (y - val)
                new_points.add((x, y_coord))
        points = new_points

    max_x = max([p[0] for p in points])
    max_y = max([p[1] for p in points])

    for j in range(max_y + 1):
        for i in range(max_x + 1):
            if (i, j) in points:
                print('#', end='')
            else:
                print(' ', end='')
        print()


if __name__ == '__main__':
    dots = []
    folds = []
    read_folds = False
    with open('inputs/day13.txt') as f:
        for line in f.readlines():
            if read_folds:
                axis, value = line[FOLD_INDEX:].split('=')
                folds.append((axis, int(value)))
                continue
            if not line.strip():
                # Everything after this is a fold
                read_folds = True
            else:
                dots.append(tuple([int(x) for x in line.strip().split(',')]))

    print(dots_after_first_fold(dots, folds[0]))
    print_unlock_code(dots, folds)
