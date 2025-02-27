from pathlib import Path
import nbformat
from glob import glob


nbpaths = glob("./chapters/**/*.ipynb", recursive=True)

excluding_tags = ["remove-cell"]

def extract_content(notebook_file: str) -> str:

    abs_path = Path(notebook_file).resolve()

    with abs_path.open("r", encoding="utf-8") as file:
        nb = nbformat.read(file, nbformat.NO_CONVERT)

    return " ".join([
        cell.source
        for cell in nb.cells
        if not set(excluding_tags) & set(cell.get("metadata", {}).get("tags", [])) # Intersection
    ])

def extract_all() -> list[str]:
    return [extract_content(path) for path in nbpaths]

