import math
import pytest

from graph_shortest_paths.application.algorithms import (
    Dijkstra,
    BellmanFord,
    FloydWarshall,
)


@pytest.mark.parametrize("algo_cls", [Dijkstra, BellmanFord, FloydWarshall])
def test_all_reach_each_other(small_graph, algo_cls):
    dist, _ = algo_cls().run(small_graph, "CA")
    # todos os vértices devem ser alcançáveis (grafo conectado)
    assert all(d < math.inf for d in dist.values())


def test_consistency_between_algorithms(small_graph):
    dij_dist, _ = Dijkstra().run(small_graph, "CA")
    bf_dist, _ = BellmanFord().run(small_graph, "CA")
    assert dij_dist == bf_dist
