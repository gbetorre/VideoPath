"""
VideoPath package: Path Editor for VideoPad project files (.vpj).
"""

from .gui import VideoPathEditor
from .fileio import browse_and_read_file

__version__ = "0.1.0"

__all__ = [
    "VideoPathEditor",
    "browse_and_read_file",
]