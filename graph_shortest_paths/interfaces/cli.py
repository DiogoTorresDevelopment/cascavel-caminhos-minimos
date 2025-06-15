#!/usr/bin/env python
"""
Executa os algoritmos via terminal:

    python -m graph_shortest_paths.interfaces.cli \
           --algo dij --src CA --dst MR --export docs/

Use --help para ver todas as opções.
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path

from ..application.algorithms import BellmanFord, Dijkstra, FloydWarshall
from ..application.services.path_service import PathService
from ..domain.builders import cascavel_graph
from ..infrastructure.io.exporters import export_distances_csv
from ..infrastructure.logger import setup_logger

logger = logging.getLogger(__name__)


def _build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Algoritmos de Caminho Mínimo – Cascavel e região")
    p.add_argument("--algo", choices=["dij", "bf", "fw"], default="dij",
                   help="Algoritmo a ser executado (default: dij)")
    p.add_argument("--src", default="CA", help="Vértice de origem (default: CA)")
    p.add_argument("--dst", default=None, help="Vértice de destino (opcional)")
    p.add_argument("--export", type=Path, help="Diretório para salvar CSV de distâncias")
    return p


def main(argv: list[str] | None = None) -> None:  # entry-point para python -m
    setup_logger()
    args = _build_argparser().parse_args(argv)

    algo_map = {
        "dij": Dijkstra(),
        "bf": BellmanFord(),
        "fw": FloydWarshall(),
    }
    algo = algo_map[args.algo]
    svc = PathService(algo)

    logger.info("Rodando %s...", algo.__class__.__name__)
    g = cascavel_graph()
    dist, prev, elapsed = svc.shortest(g, args.src, args.dst)

    print(json.dumps(dist, indent=2, ensure_ascii=False))
    print(f"\nTempo: {elapsed * 1e6:.2f} µs")

    if args.export:
        args.export.mkdir(parents=True, exist_ok=True)
        outfile = export_distances_csv(dist, args.export / f"dist_{args.algo}.csv")
        logger.info("Distâncias exportadas em %s", outfile)


if __name__ == "__main__":  # permite python interfaces/cli.py localmente
    main()
