"""
Pequenos wrappers utilitários para medição de tempo.
Evita importar `timeit` toda hora e uniformiza saída.
"""

from __future__ import annotations

from time import perf_counter
from typing import Callable, Tuple, TypeVar

T = TypeVar("T")


def measure(fn: Callable[[], T], *, repeat: int = 1) -> Tuple[T, float]:
    """
    Executa `fn` e devolve (resultado, tempo_segundos).
    Se repeat > 1, devolve média do tempo (resultado é da última execução).
    """
    total = 0.0
    result = None
    for _ in range(repeat):
        t0 = perf_counter()
        result = fn()
        total += perf_counter() - t0
    return result, total / repeat


def ns(seconds: float) -> int:
    """Converte segundos para nanossegundos (int)."""
    return int(seconds * 1e9)
