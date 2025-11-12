"""
Main entry point for Streamlit Cloud deployment.
This file imports and runs the portfolio app from the streamlit-portfolio directory.
"""
import sys
from pathlib import Path

def main():
    # Add the streamlit-portfolio/src directory to Python path
    portfolio_src = Path(__file__).parent / "streamlit-portfolio" / "src"
    sys.path.insert(0, str(portfolio_src))
    
    # Import and run the portfolio app
    from app import main as portfolio_main
    portfolio_main()

if __name__ == "__main__":
    main()
else:
    # For Streamlit Cloud, run automatically
    main()