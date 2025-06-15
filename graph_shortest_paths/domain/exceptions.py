class GraphError(Exception):
    """Erro genérico de grafo (classe‐mãe)."""


class NoPathError(GraphError):
    """Não existe caminho possível entre origem e destino."""


class NegativeCycleError(GraphError):
    """Ciclo de peso negativo detectado (Bellman-Ford ou FW)."""
