"""
Funções de exportação simples (CSV / gráfico de barras de tempo).
Expanda conforme necessidade do relatório.
"""
import json
from pathlib import Path
from typing import Mapping, Sequence

import csv
import matplotlib.pyplot as plt


def plot_timing_bar(labels: Sequence[str], times_ms: Sequence[float], outfile: Path):
    """Gera gráfico PNG comparando tempos de execução."""
    outfile = outfile.with_suffix(".png")
    fig = plt.figure()
    plt.bar(labels, times_ms)
    plt.ylabel("Tempo (ms)")
    plt.title("Comparação de desempenho – algoritmos de caminho mínimo")
    plt.tight_layout()
    fig.savefig(outfile)
    plt.close(fig)
    return outfile


def export_distances_csv(dist: Mapping[str, float], outfile: Path):
    """Salva distâncias em CSV (vértice;distância)."""
    outfile = outfile.with_suffix(".csv")
    with outfile.open("w", newline="", encoding="utf8") as fp:
        writer = csv.writer(fp, delimiter=";")
        writer.writerow(["vertex", "distance"])
        writer.writerows(dist.items())
    return outfile


# ---------- NOVO ----------
def export_distances_json(dist: Mapping[str, float], outfile: Path):
    """Salva distâncias em JSON prettificado."""
    outfile = outfile.with_suffix(".json")
    with outfile.open("w", encoding="utf8") as fp:
        json.dump(dist, fp, indent=2, ensure_ascii=False)
    return outfile
# ---------------------------