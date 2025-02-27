from pathlib import Path
import nbformat
from glob import glob


nbpaths = glob("./chapters/**/*.ipynb", recursive=True)

excluding_tags = ["remove-cell"]


quiz_tag = "quiz"

def extract_content_cells(notebook_file, cell_n = 0):

    ''' cell_n: The cell number of the question. '''

    abs_path = Path(notebook_file).resolve()

    with abs_path.open("r", encoding="utf-8") as file:
        nb = nbformat.read(file, nbformat.NO_CONVERT)

    quiz_count: int = 0
    cell_content: list[str] = []

    for cell in nb.cells:
        if (quiz_count == cell_n):
            if not set(excluding_tags) & set(cell.get("metadata", {}).get("tags", [])):
                cell_content.append(cell.source)
        if quiz_tag in (cell.get("metadata", {}).get("tags", [])):
            quiz_count += 1
    return " ".join(cell_content)
    

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

