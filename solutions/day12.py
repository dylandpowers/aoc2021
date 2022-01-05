def num_paths_through_system(caves):
    return backtrack(['start'], caves)


def backtrack(path, caves):
    last = path[-1]
    total = 0
    for conn in caves[last]:
        if conn.islower() and conn in set(path):
            continue
        if conn == 'end':
            total += 1
        else:
            path.append(conn)
            total += backtrack(path, caves)
            path.pop()
    return total


def num_paths_through_system2(caves):
    return backtrack2(['start'], caves, False)


def backtrack2(path, caves, visit_twice):
    last = path[-1]
    total = 0
    for conn in caves[last]:
        if conn == 'start':
            continue
        if conn == 'end':
            total += 1
        elif conn.islower():
            if conn in set(path):
                if not visit_twice:
                    path.append(conn)
                    total += backtrack2(path, caves, True)
                    path.pop()
            else:
                path.append(conn)
                total += backtrack2(path, caves, visit_twice)
                path.pop()
        else:
            path.append(conn)
            total += backtrack2(path, caves, visit_twice)
            path.pop()
    return total


def build_graph(conns):
    graph = {}
    for conn in conns:
        u, v = conn.split('-')
        adj = graph[u] if u in graph else []
        adj.append(v)
        graph[u] = adj
        adj2 = graph[v] if v in graph else []
        adj2.append(u)
        graph[v] = adj2
    return graph


if __name__ == '__main__':
    with open('../inputs/day12.txt') as f:
        connections = [line.strip() for line in f.readlines()]
    g = build_graph(connections)
    # print(num_paths_through_system(g))
    print(num_paths_through_system2(g))
