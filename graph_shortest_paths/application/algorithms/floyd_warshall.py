"""
Floyd–Warshall (Todos-para-todos).  O(V³).
Para manter assinatura igual, devolvemos apenas a linha 'source' de distâncias.
"""

from __future__ import annotations

from typing import Dict, Hashable, Tuple

from .base import ShortestPathAlgorithm
from ...domain.graph import Graph


class FloydWarshall(ShortestPathAlgorithm):
    def run(self, graph: Graph, source: Hashable):
        matrix, idx = graph.as_matrix()
        n = len(matrix)

        # algoritmo principal
        for k in range(n):
            for i in range(n):
                ik = matrix[i][k]
                if ik == float("inf"):
                    continue
                for j in range(n):
                    via_k = ik + matrix[k][j]
                    if via_k < matrix[i][j]:
                        matrix[i][j] = via_k

        # Constrói dicionário de distâncias a partir de 'source'
        src_idx = idx[source]
        dist: Dict[Hashable, float] = {
            v: matrix[src_idx][j] for v, j in idx.items()
        }

        prev: Dict[Hashable, Hashable] = {}  # 💡 TODO: reconstruir caminho se necessário
        return dist, prev
