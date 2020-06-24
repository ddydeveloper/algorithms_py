from src.data_structures.trees.c_graph import Graph


def main():
    graph = Graph([
        (0, 1, 5), (0, 4, 5),
        (1, 2, 10), (1, 3, 4), (1, 4, 10),
        (2, 5, 15),
        (3, 6, 4),
        (4, 6, 6), (4, 7, 5), (4, 8, 8),
        (6, 5, 3),
        (7, 9, 10), (7, 10, 4),
        (8, 10, 5),
    ])

    return dijkstra(0, graph)


def dijkstra(start: int, graph: Graph):
    result = {start: 0}
    queue = [start]
    visited = []

    while len(queue) > 0:
        vtx = queue.pop(0)
        weight = result[vtx]

        relations = [(e[1], e[2]) for e in graph.edges if e[0] == vtx and e[1] not in visited]

        for r in relations:
            if r[0] in result:
                exists_weight = result[r[0]]
                result[r[0]] = exists_weight if exists_weight <= weight + r[1] else weight + r[1]
            else:
                result[r[0]] = weight + r[1]

            queue.append(r[0])

        visited.append(vtx)

    return result
