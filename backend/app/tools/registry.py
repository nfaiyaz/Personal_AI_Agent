from app.tools.time_tool import get_current_time
from app.tools.calculator_tool import calculator
from app.tools.file_tool import list_files, read_file, search_files
from app.tools.note_tool import create_note


TOOLS = {
    "get_current_time": get_current_time,
    "calculator": calculator,
    "list_files": list_files,
    "read_file": read_file,
    "search_files": search_files,
    "create_note": create_note,
}


def get_tool(name: str):
    """
    Get a tool from the allow-list.
    """

    return TOOLS.get(name)


def list_tools():
    """
    Return the names of all available tools.
    """

    return list(TOOLS.keys())