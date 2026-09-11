from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
NOTES_DIR = PROJECT_ROOT / "data" / "notes"


def _safe_path(filename: str) -> Path:
    """
    Convert a filename into a safe path inside the notes directory.
    """

    requested_path = (NOTES_DIR / filename).resolve()

    if not requested_path.is_relative_to(NOTES_DIR.resolve()):
        raise ValueError("Access outside the notes directory is not allowed.")

    return requested_path


def list_files():
    """
    List files inside the notes directory.
    """

    NOTES_DIR.mkdir(parents=True, exist_ok=True)

    files = []

    for path in NOTES_DIR.iterdir():
        if path.is_file():
            files.append(path.name)

    return sorted(files)


def read_file(filename: str) -> str:
    """
    Read a UTF-8 text file from the notes directory.
    """

    path = _safe_path(filename)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {filename}")

    if not path.is_file():
        raise ValueError("The requested path is not a file.")

    return path.read_text(encoding="utf-8")