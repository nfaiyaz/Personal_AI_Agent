from pathlib import Path
from datetime import datetime


PROJECT_ROOT = Path(__file__).resolve().parents[3]
NOTES_DIR = PROJECT_ROOT / "data" / "notes"


def create_note(content: str, filename: str | None = None) -> str:
    """
    Create a text note inside the safe notes directory.
    """

    if not content.strip():
        raise ValueError("Note content cannot be empty.")

    NOTES_DIR.mkdir(parents=True, exist_ok=True)

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"note_{timestamp}.txt"

    if not filename.endswith(".txt"):
        filename += ".txt"

    path = (NOTES_DIR / filename).resolve()

    if not path.is_relative_to(NOTES_DIR.resolve()):
        raise ValueError("Access outside the notes directory is not allowed.")

    path.write_text(content.strip(), encoding="utf-8")

    return f"Note created successfully: {path.name}"