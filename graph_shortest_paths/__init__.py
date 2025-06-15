"""
Inicialização do pacote raiz.

• Não execute nada pesado aqui (apenas exposições de API).
• Logger é *lazy* – só é criado se alguém chamar `get_logger()`.
"""

from .infrastructure.logger import setup_logger as _setup_logger

_setup_logger()

__all__ = []  # evita import “estrela” acidental
