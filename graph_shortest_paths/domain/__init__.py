"""
Camada de domínio – entidades puras, sem efeitos colaterais de I/O.
Exporta apenas o necessário para consumo externo.
"""

from .graph import Graph
from .exceptions import GraphError, NoPathError, NegativeCycleError
from .builders import cascavel_graph, regional_graph

__all__ = [
    "Graph",
    "GraphError",
    "NoPathError",
    "NegativeCycleError",
    "cascavel_graph",
    "regional_graph",
]
