"""
Camada de aplicação – interface comum de algoritmos de caminho mínimo.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Hashable, Tuple

from ...domain.graph import Graph


class ShortestPathAlgorithm(ABC):
    """Contratos para qualquer algoritmo de caminho mínimo."""

    @abstractmethod
    def run(
        self, graph: Graph, source: Hashable
    ) -> Tuple[Dict[Hashable, float], Dict[Hashable, Hashable]]:
        """
        Executa o algoritmo a partir de ``source``.

        Returns
        -------
        dist : Dict[v, float]
            Menor custo de ``source`` até cada vértice v.
        prev : Dict[v, Hashable]
            Antecessor imediato no menor caminho (opcionalmente vazio).
        """
