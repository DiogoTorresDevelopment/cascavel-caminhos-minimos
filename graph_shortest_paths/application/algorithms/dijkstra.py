"""
Implementação de Dijkstra com fila de prioridade (heapq).
Complexidade O((V + E) log V) para grafos não densos.
"""

from __future__ import annotations

import heapq
import math
from typing import Dict, Hashable, Tuple

from .base import ShortestPathAlgorithm
from ...domain.graph import Graph

PQItem = Tuple[float, Hashable]  # (distância, vértice)


class Dijkstra(ShortestPathAlgorithm):
    def run(self, graph: Graph, source: Hashable):
        dist: Dict[Hashable, float] = {v: math.inf for v in graph.vertices}
        prev: Dict[Hashable, Hashable] = {}
        dist[source] = 0.0

        pq: list[PQItem] = [(0.0, source)]
        while pq:
            d_u, u = heapq.heappop(pq)
            if d_u != dist[u]:  # elemento obsoleto
                continue
            for v, w in graph.neighbors(u):
                alt = d_u + w
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(pq, (alt, v))

        return dist, prev
