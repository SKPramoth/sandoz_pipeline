# Sandoz Pipeline Streamlit App - Installation & Quick Start

## 📦 What's Included

This complete Streamlit application includes:

✅ **Main Application** (`app.py`)
- Full portfolio management dashboard
- Single product detailed view
- Multi-tab analysis interface
- Version history tracking
- Scenario comparison

✅ **Configuration** (`config.py`)
- 4 pharmaceutical products with full details
- 7 product archetypes
- Version history records
- Color schemes and constants

✅ **Utilities** (`utils.py`)
- 20+ helper functions
- Data processing utilities
- Calculation functions
- Formatting tools

✅ **Documentation**
- README.md - Full documentation
- QUICKSTART.md - Quick start guide
- DEPLOYMENT.md - Deployment instructions
- PROJECT_STRUCTURE.md - Project organization

✅ **Configuration Files**
- requirements.txt - All dependencies
- .streamlit/config.toml - Streamlit theme config
- .gitignore - Git configuration

## 🚀 Quick Start (30 seconds)

### Windows PowerShell
```powershell
# Navigate to folder
cd C:\Users\PramothSKarthikeyan\Documents\Sandoz_pipeline_streamlit

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

### macOS/Linux Terminal
```bash
# Navigate to folder
cd Sandoz_pipeline_streamlit

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

**✨ That's it! App opens at `http://localhost:8501`**

## 📊 What You'll See

### Portfolio View (Default)
```
┌─────────────────────────────────────────────────────┐
│ 💊 Pipeline Decision System                         │
│ Centralized Portfolio Management & NPV Tracking     │
└─────────────────────────────────────────────────────┘

[📦 Single Product View] [📊 Portfolio View ✓]

┌─────────────────────────────────────────────────────┐
│ Total Pipeline NPV    Products    High Priority    │
│ $926.1M               4           3                │
│                       Launches: 3                   │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Archetype Distribution                              │
│ [Med Benefit High] [Med Benefit Med] [Rx Benefit]  │
│ [Rare Disease] ... (7 total)                       │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Portfolio Table                                     │
│ Product | Archetype | Phase | Launch | NPV | ...   │
├─────────────────────────────────────────────────────┤
│ Biosimilar Humira | Med Benefit High | ... $245.6M │
│ Biosimilar Enbrel | Med Benefit Med | ... $178.3M  │
│ Generic Lyrica | Rx Benefit High | ... $189.4M     │
│ Rare Disease Gene Therapy | Rare ... | ... $312.8M │
└─────────────────────────────────────────────────────┘
```

### Single Product View
```
┌─────────────────────────────────────────────────────┐
│ ☜ [SIDEBAR]  │ Biosimilar Humira (Adalimumab)    │
│ Products:     │ Archetype: Med Benefit High      │
│ • Product 1   │ Priority: High | Phase: Pre-Launch│
│ • Product 2   │ Launch: 2026-Q2                   │
│ • Product 3   │                                   │
│ • Product 4   │ NPV: $245.6M                      │
│               │                                   │
│ Quick Actions │ [📋 Assumptions][💰 Financials] │
│ Show Version  │ [🎯 Access] [📅 Timeline]       │
│ Show Scenarios│                                   │
└─────────────────────────────────────────────────────┘
                        ↓
        [Detailed Analysis & Charts]
```

## 📊 Portfolio Overview

### Products ($926.1M Total NPV)

| # | Product | Phase | Launch | Priority | NPV |
|---|---------|-------|--------|----------|-----|
| 1 | Biosimilar Humira | Pre-Launch | 2026-Q2 | High | $245.6M |
| 2 | Biosimilar Enbrel | Filed | 2026-Q4 | Medium | $178.3M |
| 3 | Generic Lyrica | Pre-Launch | 2026-Q3 | High | $189.4M |
| 4 | Rare Disease Gene Therapy | Phase 3 | 2027-Q2 | Strategic | $312.8M |

### Archetypes

| Archetype | Count | Color |
|-----------|-------|-------|
| Med Benefit High | 8 | 🔵 Blue |
| Med Benefit Med | 6 | 🔷 Light Blue |
| Med Benefit Low | 4 | 🔲 Lighter Blue |
| Rx Benefit High | 7 | 🟢 Green |
| Rx Benefit Med | 5 | 🟩 Light Green |
| Rx Benefit Low | 3 | 🟩 Lighter Green |
| Rare Disease | 2 | 🟣 Purple |

## 🎯 Key Features

### Portfolio View
- ✅ Summary metrics (NPV, products, priorities)
- ✅ Archetype visualization with counts
- ✅ Complete product table
- ✅ Export to CSV
- ✅ Navigate to product details

### Single Product View
- ✅ Product selector dropdown
- ✅ Quick action toggles
- ✅ Multi-tab analysis interface
- ✅ **Assumptions Tab**: Uptake, pricing, access
- ✅ **Financials Tab**: NPV, revenue projections
- ✅ **Access Tab**: Market strategy, payers
- ✅ **Timeline Tab**: Development milestones
- ✅ Version history with audit trail
- ✅ Scenario comparison (base/optimistic/conservative)

## 💡 Key Data Points

### Assumptions Available
- **Uptake**: Year-by-year market uptake (Y1-Y5)
- **Peak Share**: Expected maximum market share
- **Pricing**: WAC, ASP, Gross-to-Net percentages
- **Access**: Formulary tier percentages
- **Competition**: Competition level assessment
- **J-Code**: Unique J-code status
- **Distribution**: Distribution channel strategy

### Financial Calculations
- **NPV**: Net Present Value (primary metric)
- **5-Year Revenue**: NPV × 1.8
- **Peak Year Revenue**: NPV × 0.45
- **Scenarios**: ±25% from base case
- **Waterfall**: Revenue decomposition

### Audit Trail
- Version control (v1.0 - v1.3)
- Change tracking with details
- NPV impact for each change
- Approval status tracking
- User attribution

## 📁 Files Created

```
Sandoz_pipeline_streamlit/
├── app.py                    ← Main application (~400 lines)
├── config.py                 ← Data & configuration (~200 lines)
├── utils.py                  ← Helper functions (~250 lines)
├── requirements.txt          ← Dependencies
├── README.md                 ← Full documentation
├── QUICKSTART.md             ← Quick start guide
├── DEPLOYMENT.md             ← Deployment guide
├── PROJECT_STRUCTURE.md      ← Project organization
├── .gitignore                ← Git configuration
└── .streamlit/
    └── config.toml          ← Streamlit configuration
```

## ⚙️ System Requirements

- **Python**: 3.8+
- **RAM**: 512MB minimum (2GB recommended)
- **Disk**: 500MB for venv + dependencies
- **Browser**: Any modern browser

## 🔧 Common Commands

```bash
# Run the app
streamlit run app.py

# Run with custom port
streamlit run app.py --server.port 8502

# Clear cache
streamlit cache clear

# View logs
streamlit logs

# Deactivate venv
deactivate
```

## 🐛 Troubleshooting

### "Port already in use"
```bash
streamlit run app.py --server.port 8502
```

### Missing dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Module not found errors
```bash
# Ensure venv is activated, then reinstall
pip install -r requirements.txt --force-reinstall
```

## 📈 Next Steps

1. ✅ Run the app locally
2. ✅ Explore portfolio view
3. ✅ Click on products to see details
4. ✅ Review different tabs
5. ✅ Check version history
6. ✅ Compare scenarios

## 🌐 Deployment Options

- **Streamlit Cloud**: Easiest (connect GitHub repo)
- **Heroku**: Free tier available
- **AWS EC2**: Full control
- **Docker**: Containerized deployment
- **On-premise**: Local server

See `DEPLOYMENT.md` for detailed instructions.

## 📞 Support

- Full documentation: `README.md`
- Quick start: `QUICKSTART.md`
- Deployment: `DEPLOYMENT.md`
- Structure: `PROJECT_STRUCTURE.md`

## 🎉 You're All Set!

Your Sandoz Pipeline Decision System is ready to use. 

**Start the app now:**
```bash
streamlit run app.py
```

---

**Version**: 1.0.0  
**Last Updated**: 2026-02-04  
**Status**: ✅ Production Ready
