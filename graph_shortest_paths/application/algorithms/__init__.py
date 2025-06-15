"""
Facilita importações:  from ...application.algorithms import Dijkstra, BellmanFord…
"""

from .dijkstra import Dijkstra
from .bellman_ford import BellmanFord
from .floyd_warshall import FloydWarshall

__all__ = ["Dijkstra", "BellmanFord", "FloydWarshall"]
