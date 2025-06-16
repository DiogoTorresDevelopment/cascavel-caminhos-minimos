from tabulate import tabulate  # pip install tabulate  (opcional, só para estética)

from graph_shortest_paths.domain.builders import cascavel_graph
from graph_shortest_paths.application.algorithms import (
    Dijkstra, BellmanFord, FloydWarshall,
)

ALGOS = [
    ("Dijkstra", Dijkstra()),
    ("Bellman-Ford", BellmanFord()),
    ("Floyd-Warshall", FloydWarshall()),
]

g = cascavel_graph()
src = "CA"

for name, algo in ALGOS:
    dist, _ = algo.run(g, src)
    # ordena alfabeticamente os vértices só para a impressão
    rows = [(v, f"{d:.0f}" if d < float("inf") else "∞") for v, d in sorted(dist.items())]

    print(f"\n=== {name} – distâncias a partir de {src} ===")
    print(tabulate(rows, headers=["Vértice", "Distância"], tablefmt="github"))
