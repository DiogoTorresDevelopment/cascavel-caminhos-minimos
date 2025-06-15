"""
“Fábricas” de grafos que o trabalho exige.
👉 Altere/adicione aqui apenas se precisar de outros cenários de teste.
"""

from .graph import Graph


def cascavel_graph() -> Graph:
    """Grafo de 10 vértices (≤ 100 km de Cascavel)."""
    g = Graph()
    g.add_edge("CA", "ST", 21)
    g.add_edge("CA", "CO", 27)
    g.add_edge("CA", "LI", 36)
    g.add_edge("CA", "TO", 45)
    g.add_edge("CA", "CT", 41)
    g.add_edge("CA", "MT", 69)
    g.add_edge("CA", "ME", 83)
    g.add_edge("CA", "AS", 73)
    g.add_edge("CA", "MR", 85)
    g.add_edge("ST", "LI", 29)
    g.add_edge("CO", "TO", 69)
    g.add_edge("TO", "AS", 45)
    g.add_edge("TO", "MR", 40)
    g.add_edge("ME", "MT", 15)
    return g


def regional_graph() -> Graph:
    """
    Versão maior (12 vértices) – adicione duas cidades vizinhas.
    👉 Pesquise distâncias reais se for exigir fidelidade.
    """
    g = cascavel_graph()
    g.add_edge("MR", "QU", 38)  # Quatro Pontes
    g.add_edge("TO", "QU", 24)
    g.add_edge("CO", "BR", 31)  # Braganey
    g.add_edge("BR", "CT", 37)
    return g
