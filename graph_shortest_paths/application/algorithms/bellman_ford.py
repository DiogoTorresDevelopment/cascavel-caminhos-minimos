"""
Bellman–Ford: aceita pesos negativos e detecta ciclo negativo.
Complexidade O(V · E).
"""

from __future__ import annotations

import math
from typing import Dict, Hashable, Tuple

from .base import ShortestPathAlgorithm
from ...domain.graph import Graph
from ...domain.exceptions import NegativeCycleError


class BellmanFord(ShortestPathAlgorithm):
    def run(self, graph: Graph, source: Hashable):
        dist: Dict[Hashable, float] = {v: math.inf for v in graph.vertices}
        prev: Dict[Hashable, Hashable] = {}
        dist[source] = 0.0

        V = list(graph.vertices)
        E = graph.edges  # [(u, v, w), ...]

        for _ in range(len(V) - 1):
            updated = False
            for u, v, w in E:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    updated = True
                if not graph.directed and dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w
                    prev[u] = v
                    updated = True
            if not updated:
                break

        for u, v, w in E:
            if dist[u] + w < dist[v]:
                raise NegativeCycleError("Ciclo negativo detectado – Bellman-Ford")
            if not graph.directed and dist[v] + w < dist[u]:
                raise NegativeCycleError("Ciclo negativo detectado – Bellman-Ford")

        return dist, prev

