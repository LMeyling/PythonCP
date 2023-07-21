graph = [x for x in range(1, (n * m) + 1)]
size = [0 for x in range(1, (n * m) + 1)]

def find(current):
    if graph[current - 1] == current:
        return current
    graph[current - 1] = find(graph[current - 1])
    return graph[current - 1]


def union(first, second):
    one = find(first)
    two = find(second)
    if one != two:
        if size[one - 1] < size[two - 1]:
            tmp = one
            one = two
            two = tmp
        graph[one - 1] = two
        if size[two - 1] == size[one - 1]:
            size[one - 1] += 1
        return 1
    return 0