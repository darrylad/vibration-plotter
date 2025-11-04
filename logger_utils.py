"""
Simple logging utility to write to both console and file.
"""

import logging
import sys
from pathlib import Path
from datetime import datetime


def setup_logging(output_dir: Path = None, log_filename: str = "log.txt"):
    """
    Setup logging to write to both console and file.
    
    Args:
        output_dir: Directory to write log file (default: "output")
        log_filename: Name of log file (default: "log.txt")
    """
    # Use default output directory if not specified
    if output_dir is None:
        output_dir = Path("output")
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    # Full path to log file
    log_path = output_dir / log_filename
    
    # Clear any existing handlers
    root_logger = logging.getLogger()
    root_logger.handlers = []
    
    # Set logging level
    root_logger.setLevel(logging.INFO)
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    simple_formatter = logging.Formatter('%(levelname)s: %(message)s')
    
    # File handler (with timestamp)
    file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(detailed_formatter)
    
    # Console handler (simple format)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    
    # Add handlers to root logger
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    # Also capture print statements by creating a custom print function
    # (We'll use a simple wrapper instead)
    
    return log_path


class LogPrint:
    """
    Wrapper to capture print statements to log file.
    """
    def __init__(self, log_path: Path):
        self.log_path = log_path
        self.terminal = sys.stdout
        
    def write(self, message):
        """Write to both terminal and file."""
        self.terminal.write(message)
        if message.strip():  # Don't write empty lines
            with open(self.log_path, 'a', encoding='utf-8') as f:
                f.write(message)
    
    def flush(self):
        """Flush both outputs."""
        self.terminal.flush()


def enable_print_logging(log_path: Path):
    """
    Redirect print statements to both console and log file.
    
    Args:
        log_path: Path to log file
    """
    sys.stdout = LogPrint(log_path)