from graph_shortest_paths.domain.graph import Graph


def test_matrix_roundtrip():
    g = Graph()
    g.add_edge("A", "B", 3)
    g.add_edge("B", "C", 2)
    mat, idx = g.as_matrix()
    # matriz principal deve ter zeros na diagonal
    for i in range(len(mat)):
        assert mat[i][i] == 0
    # dist(A, C) inicial é infinito
    assert mat[idx["A"]][idx["C"]] == float("inf")
