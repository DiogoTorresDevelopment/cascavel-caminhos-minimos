"""
Estrutura de dados de grafo não dirigido ponderado.
Se precisar de grafo dirigido, basta instanciar com `directed=True`.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Hashable, Iterable, List, Tuple

Vertex = Hashable
Weight = float


@dataclass
class Graph:
    directed: bool = False
    _adj: Dict[Vertex, List[Tuple[Vertex, Weight]]] = field(default_factory=dict)

    # -------------------------- mutators --------------------------------- #
    def add_edge(self, u: Vertex, v: Vertex, w: Weight) -> None:
        if w < 0:
            raise ValueError("Peso negativo não permitido neste grafo (domínio).")
        self._adj.setdefault(u, []).append((v, w))
        self._adj.setdefault(v, [])  # garante vértice isolado armazenado
        if not self.directed:
            self._adj.setdefault(v, []).append((u, w))

    # -------------------------- accessors -------------------------------- #
    def neighbors(self, u: Vertex):
        return self._adj.get(u, [])

    @property
    def vertices(self) -> Iterable[Vertex]:
        return self._adj.keys()

    @property
    def edges(self) -> List[Tuple[Vertex, Vertex, Weight]]:
        es: List[Tuple[Vertex, Vertex, Weight]] = []
        for u, nbrs in self._adj.items():
            for v, w in nbrs:
                if self.directed or u <= v:
                    es.append((u, v, w))
        return es

    def as_matrix(self, inf=float("inf")):
        """
        Converte para (matriz de adjacência, dict índice→vértice).
        Útil para Floyd-Warshall.
        """
        idx = {v: i for i, v in enumerate(self.vertices)}
        n = len(idx)
        mat = [[inf] * n for _ in range(n)]
        for v in self.vertices:
            mat[idx[v]][idx[v]] = 0
        for u, v, w in self.edges:
            mat[idx[u]][idx[v]] = w
            if not self.directed:
                mat[idx[v]][idx[u]] = w
        return mat, idx
