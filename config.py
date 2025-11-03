"""
Configuration file for the vibration data plotter.
This keeps all settings in one place for easy modification.
"""

from pathlib import Path

# Data paths
DATA_ROOT = Path("/Users/darrylad/Darryl/Research/Darryl/Data")

# Conditions to analyze (in display order)
CONDITIONS = ["Healthy", "10 um", "45 um", "75 um", "100 um"]

# Plot configuration
PLOT_CONFIG = {
    "height_per_row": 300,  # Height of each subplot row
    "width": 1800,          # Total width of the plot
    "title_font_size": 16,
    "axis_font_size": 12,
}

# Color scheme for each axis
AXIS_COLORS = {
    "X": "#FF6B6B",  # Red
    "Y": "#4ECDC4",  # Teal
    "Z": "#95E1D3",  # Light teal
}

# Data column names (from your CSV)
TIME_COLUMN = "Channel name"
AXIS_COLUMNS = ["X", "Y", "Z"]