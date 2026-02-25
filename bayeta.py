import random
from pathlib import Path

FICHERO_FRASES = Path(__file__).with_name("frases.txt")

def frotar(n_frases: int = 1) -> list():
    if n_frases < 1:
        return []

    if not FICHERO_FRASES.exists():
        return []

    frases = [
        linea.strip()
        for linea in FICHERO_FRASES.read_text(encoding="utf-8").splitlines()
        if linea.strip()
    ]

    if not frases:
        return []

    return [random.choice(frases) for _ in range(n_frases)]
