"""
`python -m graph_shortest_paths`  →  executa:
1. Smoke-test dos 3 algoritmos em dois grafos (10 v e 12 v)
2. Exporta distâncias em CSV + JSON
3. Gera gráfico de desempenho em docs/timing.png
4. Roda pytest (pode comentar se não quiser)
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

import pytest

from .application.algorithms import BellmanFord, Dijkstra, FloydWarshall
from .domain.builders import cascavel_graph, regional_graph
from .infrastructure.timing import measure
from .infrastructure.io.exporters import (
    plot_timing_bar,
    export_distances_csv,
    export_distances_json,
)

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
# -------------------------------------------------------------------------------------------------


def smoke_test() -> None:
    """Executa os 3 algoritmos em dois grafos, mede tempo e exporta resultados."""
    graphs = [
        ("pequeno", cascavel_graph()),   # 10 vértices
        ("medio",   regional_graph()),   # 12 vértices
    ]
    algos = [
        ("dijkstra",       Dijkstra()),
        ("bellman-ford",   BellmanFord()),
        ("floyd-warshall", FloydWarshall()),
    ]

    labels, times_ms = [], []
    docs_dir = Path(__file__).resolve().parent.parent / "docs"
    res_dir  = docs_dir / "resultados"
    docs_dir.mkdir(exist_ok=True)
    res_dir.mkdir(parents=True, exist_ok=True)

    for g_name, g in graphs:
        logger.info("🚩  Grafo %s", g_name)
        for a_name, algo in algos:
            # -------- execução e medição ---------------------------------------------------------
            (dist, _), t = measure(lambda a=algo: a.run(g, "CA"), repeat=3)
            ms = t * 1e3
            labels.append(f"{a_name}\n{g_name}")
            times_ms.append(ms)
            logger.info("  • %-14s  %7.2f ms", a_name.capitalize(), ms)

            # -------- exportação CSV + JSON ------------------------------------------------------
            base = res_dir / f"{a_name}_{g_name}"
            export_distances_csv(dist, base)   # → .csv
            export_distances_json(dist, base)  # → .json
            logger.debug("    dist(CA→MR) = %s  (arquivos em %s)",
                         dist.get("MR"), res_dir)
    # -------- gráfico de barras ------------------------------------------------------------------
    plot_timing_bar(labels, times_ms, docs_dir / "timing.png")
    logger.info("📊  Gráfico salvo em %s", docs_dir / "timing.png")


def run_pytest() -> int:
    """Dispara a suíte de testes e mostra resumo; retorna exit-code."""
    logger.info("⚙️  Rodando pytest…")
    code = pytest.main(["-q", "--color=yes"])
    if code == 0:
        logger.info("✅  Todos os testes passaram.")
    else:
        logger.error("❌  Falhas nos testes.")
    return code


def main() -> None:
    smoke_test()
    # comente a linha abaixo se não quiser rodar a suíte sempre
    run_pytest()


if __name__ == "__main__":
    sys.exit(main())
