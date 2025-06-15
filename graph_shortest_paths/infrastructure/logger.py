"""
Configuração de logging única para o projeto.
Pode ser chamada uma única vez em `interfaces/cli.py` ou no `__init__`.
"""

import logging
from pathlib import Path

LOG_LEVEL = logging.INFO
LOG_FILE = Path(__file__).resolve().parent / "run.log"


def setup_logger():
    logging.basicConfig(
        level=LOG_LEVEL,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(LOG_FILE, encoding="utf8"),
        ],
    )
    logging.getLogger("matplotlib").setLevel(logging.WARNING)
