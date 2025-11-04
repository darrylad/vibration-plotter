"""
Standalone PDF export script using Matplotlib.
Run this separately from the main HTML generation.
"""

import logging
from pathlib import Path

# Import modules
from config import (
    DATA_ROOT, CONDITIONS, AXIS_COLORS,
    TIME_COLUMN, AXIS_COLUMNS, FFT_CONFIG, PDF_CONFIG
)
from data_loader import load_all_conditions
from signal_processor import compute_all_frequency_spectra, get_frequency_display_range
from plotter_static import create_time_domain_pdf, create_frequency_domain_pdf

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """
    Main function for PDF export.
    """
    print("="*80)
    print("📄 PDF EXPORT TOOL (Matplotlib Backend)")
    print("="*80)
    print(f"\nConfiguration:")
    print(f"  Figure size: {PDF_CONFIG['figsize'][0]}\" × {PDF_CONFIG['figsize'][1]}\"")
    print(f"  DPI: {PDF_CONFIG['dpi']}")
    print(f"  Downsampling: Every {PDF_CONFIG['downsample_factor']} points")
    print(f"  Rasterized: {PDF_CONFIG['rasterized']}")
    
    # ========================================================================
    # STEP 1: LOAD DATA
    # ========================================================================
    print("\n" + "="*80)
    print("STEP 1: LOADING DATA")
    print("="*80)
    
    all_data = load_all_conditions(DATA_ROOT, CONDITIONS)
    
    if not all_data:
        logger.error("❌ No data loaded! Check your data path.")
        return
    
    print(f"\n✅ Loaded {len(all_data)} conditions")
    
    # ========================================================================
    # STEP 2: COMPUTE FREQUENCY SPECTRA
    # ========================================================================
    print("\n" + "="*80)
    print("STEP 2: COMPUTING FREQUENCY SPECTRA")
    print("="*80)
    
    all_spectra = compute_all_frequency_spectra(
        all_data=all_data,
        time_column=TIME_COLUMN,
        axis_columns=AXIS_COLUMNS,
        fft_config=FFT_CONFIG
    )
    
    max_freq = get_frequency_display_range(all_spectra, FFT_CONFIG)
    
    print(f"\n✅ Computed spectra for {len(all_spectra)} conditions")
    
    # ========================================================================
    # STEP 3: CREATE OUTPUT DIRECTORY
    # ========================================================================
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # ========================================================================
    # STEP 4: GENERATE TIME-DOMAIN PDF
    # ========================================================================
    print("\n" + "="*80)
    print("STEP 3: GENERATING TIME-DOMAIN PDF")
    print("="*80)
    
    time_pdf_path = output_dir / "time_domain.pdf"
    create_time_domain_pdf(
        all_data=all_data,
        conditions=CONDITIONS,
        time_column=TIME_COLUMN,
        axis_columns=AXIS_COLUMNS,
        axis_colors=AXIS_COLORS,
        pdf_config=PDF_CONFIG,
        output_path=time_pdf_path
    )
    
    # ========================================================================
    # STEP 5: GENERATE FREQUENCY-DOMAIN PDF
    # ========================================================================
    print("\n" + "="*80)
    print("STEP 4: GENERATING FREQUENCY-DOMAIN PDF")
    print("="*80)
    
    freq_pdf_path = output_dir / "frequency_domain.pdf"
    create_frequency_domain_pdf(
        all_spectra=all_spectra,
        conditions=CONDITIONS,
        axis_columns=AXIS_COLUMNS,
        axis_colors=AXIS_COLORS,
        pdf_config=PDF_CONFIG,
        max_frequency=max_freq,
        output_path=freq_pdf_path
    )
    
    # ========================================================================
    # COMPLETE
    # ========================================================================
    print("\n" + "="*80)
    print("✨ PDF EXPORT COMPLETE!")
    print("="*80)
    print("\nGenerated files:")
    print(f"  📈 Time Domain:      {time_pdf_path}")
    print(f"  📊 Frequency Domain: {freq_pdf_path}")
    print("\nFile specifications:")
    print(f"  Format: PDF (rasterized)")
    print(f"  Resolution: {PDF_CONFIG['dpi']} DPI")
    print(f"  Size: {PDF_CONFIG['figsize'][0]}\" × {PDF_CONFIG['figsize'][1]}\"")
    print(f"  Optimized for: Widescreen displays")


if __name__ == "__main__":
    main()