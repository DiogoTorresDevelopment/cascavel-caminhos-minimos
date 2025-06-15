"""
Stub simples que gera um README.pdf a partir de docs/*.md usando Pandoc.
Requer pandoc instalado; se não tiver, apenas marca TODO.
"""

import shutil
from pathlib import Path
import subprocess
import sys

DOCS = Path("graph_shortest_paths/docs")
MD_FILE = DOCS / "RELATORIO.md"
PDF_FILE = DOCS / "RELATORIO.pdf"

if not MD_FILE.exists():
    print("❌ docs/RELATORIO.md não encontrado. Crie o markdown primeiro.")
    sys.exit(1)

if shutil.which("pandoc") is None:
    print("⚠️  Pandoc não instalado. Instale ou gere o PDF manualmente.")
    sys.exit(1)

cmd = ["pandoc", str(MD_FILE), "-o", str(PDF_FILE)]
print("Gerando PDF…")
subprocess.check_call(cmd)
print(f"✅ Relatório criado em {PDF_FILE}")
