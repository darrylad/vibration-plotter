"""
Main script to run the vibration data analysis and plotting.
"""

import logging
from pathlib import Path

# Import our modules
from config import DATA_ROOT, CONDITIONS, PLOT_CONFIG, AXIS_COLORS, TIME_COLUMN, AXIS_COLUMNS
from data_loader import load_all_conditions, test_loading
from plotter import create_vibration_plot

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """
    Main function to execute the complete analysis pipeline.
    """

    print("STEP 1: LOADING DATA")
    
    all_data = load_all_conditions(DATA_ROOT, CONDITIONS)
    
    if not all_data:
        logger.error("❌ No data loaded! Check your data path and condition names.")
        return
    
    print(f"\n✅ Successfully loaded {len(all_data)} conditions")
    
    print("STEP 2: CREATING INTERACTIVE PLOT")
    
    fig = create_vibration_plot(
        all_data=all_data,
        conditions=CONDITIONS,
        time_column=TIME_COLUMN,
        axis_columns=AXIS_COLUMNS,
        axis_colors=AXIS_COLORS,
        plot_config=PLOT_CONFIG
    )
    
    print("STEP 3: SAVING AND DISPLAYING")
    
    # Create output directory
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # Save as interactive HTML
    output_file = output_dir / "vibration_analysis.html"
    fig.write_html(str(output_file))
    print(f"\n✅ Interactive plot saved to: {output_file}")
    
    # Show in browser
    print("🌐 Opening plot in browser...")
    fig.show()
    
    print("✨ ANALYSIS COMPLETE")
    print("\nInteractive features:")
    print("  • Zoom: Click and drag")
    print("  • Pan: Hold shift and drag")
    print("  • Reset: Double click")
    print("  • Hover: See exact values")
    print("  • Compare: Hover shows all Y values at same time point")


def test_single_condition(condition: str = "Healthy"):
    """
    Test function to load and examine a single condition.
    Useful for debugging and understanding the data.
    """
    test_loading(DATA_ROOT, condition)


if __name__ == "__main__":
    # Run the main analysis
    main()
    
    # Uncomment below to test individual conditions:
    # test_single_condition("Healthy")
    # test_single_condition("10 um")