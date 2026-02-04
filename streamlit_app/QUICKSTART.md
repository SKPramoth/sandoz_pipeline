# Quick Start Guide - Sandoz Pipeline Streamlit App

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Step 1: Setup

### On Windows (PowerShell)
```powershell
# Navigate to the project folder
cd C:\Users\PramothSKarthikeyan\Documents\Sandoz_pipeline_streamlit

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### On macOS/Linux (Terminal)
```bash
# Navigate to the project folder
cd Sandoz_pipeline_streamlit

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your default browser at:
```
http://localhost:8501
```

## Step 3: Using the Application

### Portfolio View (Default)
- View summary metrics at a glance
- See archetype distribution of products
- Browse the complete portfolio table
- Export data to CSV

### Single Product View
1. Click "Single Product View" button
2. Select a product from the sidebar dropdown
3. Explore different tabs:
   - **Assumptions**: Uptake, pricing, and access data
   - **Financials**: NPV and revenue projections
   - **Access**: Market access strategy
   - **Timeline**: Product development timeline
4. Toggle additional features in sidebar:
   - Version History (audit trail)
   - Scenario Comparison (optimistic/conservative)

## Features Overview

### 📊 Key Metrics
- Total Pipeline NPV: $926.1M
- Products: 4
- High Priority Assets: 3
- Launches This Year: 3

### 🎯 Archetypes
- Med Benefit High: 8 products
- Med Benefit Med: 6 products
- Med Benefit Low: 4 products
- Rx Benefit High: 7 products
- Rx Benefit Med: 5 products
- Rx Benefit Low: 3 products
- Rare Disease: 2 products

### 📦 Products
1. **Biosimilar Humira** - $245.6M (High Priority)
2. **Biosimilar Enbrel** - $178.3M (Medium Priority)
3. **Generic Lyrica** - $189.4M (High Priority)
4. **Rare Disease Gene Therapy** - $312.8M (Strategic)

## Troubleshooting

### Port Already in Use
If port 8501 is already in use:
```bash
streamlit run app.py --server.port 8502
```

### Missing Dependencies
Reinstall all dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### Virtual Environment Issues
Delete and recreate:
```bash
# Windows
rmdir /s venv
python -m venv venv

# macOS/Linux
rm -rf venv
python3 -m venv venv
```

## File Structure

```
Sandoz_pipeline_streamlit/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Full documentation
├── QUICKSTART.md         # This file
├── .gitignore            # Git ignore rules
└── .streamlit/
    └── config.toml       # Streamlit configuration
```

## Data Modifications

To modify product information, edit the `PIPELINE_PRODUCTS` dictionary in `app.py`:

```python
PIPELINE_PRODUCTS = [
    {
        "id": "PRODUCT-001",
        "name": "Your Product Name",
        "archetype": "Med Benefit High",
        "phase": "Pre-Launch",
        "launchDate": "2026-Q2",
        "territory": "US",
        "priority": "High",
        "npv": 245.6,
        # ... more fields
    }
]
```

## Keyboard Shortcuts in Streamlit

- `r`: Rerun the app
- `c`: Clear cache
- `p`: Show developer options

## Performance Tips

- The app uses session state to maintain view state
- Pandas dataframes are computed on each run (consider caching for large datasets)
- Plotly charts are interactive and responsive

## Support & Documentation

For more information:
- Streamlit Docs: https://docs.streamlit.io/
- Project README: See README.md in this folder
- Code Comments: Check app.py for inline documentation

---

**Version**: 1.0.0  
**Last Updated**: 2026-02-04
