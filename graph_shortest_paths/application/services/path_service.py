"""
Serviço que encapsula a execução do algoritmo + medição de tempo.
Permite trocar de algoritmo em run-time (injeção de dependência bem simples).
"""

from __future__ import annotations

from time import perf_counter
from typing import Hashable, Tuple

from ..algorithms.base import ShortestPathAlgorithm
from ...domain.graph import Graph
from ...domain.exceptions import NoPathError


class PathService:
    def __init__(self, algorithm: ShortestPathAlgorithm):
        self._algo = algorithm

    # --------------------------------------------------------------------- #
    # API pública
    # --------------------------------------------------------------------- #
    def shortest(
        self, graph: Graph, src: Hashable, dst: Hashable | None = None
    ) -> Tuple[dict, dict, float]:
        """
        Executa o algoritmo e devolve (dist, prev, elapsed_seconds).

        Se ``dst`` for informado e não houver caminho, dispara NoPathError.
        """
        t0 = perf_counter()
        dist, prev = self._algo.run(graph, src)
        elapsed = perf_counter() - t0

        if dst is not None and dist.get(dst, float("inf")) == float("inf"):
            raise NoPathError(f"Não existe caminho entre {src} → {dst}")

        return dist, prev, elapsed

    # --------------------------------------------------------------------- #
    # Conveniência – reconstrói o caminho usando 'prev'
    # --------------------------------------------------------------------- #
    @staticmethod
    def build_path(prev: dict, src: Hashable, dst: Hashable) -> list[Hashable]:
        path = [dst]
        while path[-1] != src:
            parent = prev.get(path[-1])
            if parent is None:
                raise NoPathError(f"Sem caminho completo de {src} para {dst}")
            path.append(parent)
        path.reverse()
        return path
