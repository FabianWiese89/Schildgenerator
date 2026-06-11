from src.config import (
    LAYOUT_OPTION_4_LINES,
    LAYOUT_OPTION_5_LINES,
)

def get_line_count_from_layout(layout):
    if layout == LAYOUT_OPTION_5_LINES:
        return 5

    if layout == LAYOUT_OPTION_4_LINES:
        return 4

    return None