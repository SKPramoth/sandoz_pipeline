# Project Structure - Sandoz Pipeline Streamlit App

## File Organization

```
Sandoz_pipeline_streamlit/
│
├── app.py                          # Main Streamlit application
├── config.py                       # Configuration and constants
├── utils.py                        # Utility functions
│
├── requirements.txt                # Python dependencies
│
├── README.md                       # Full project documentation
├── QUICKSTART.md                   # Quick start guide
├── DEPLOYMENT.md                   # Deployment instructions
├── PROJECT_STRUCTURE.md            # This file
│
├── .gitignore                      # Git ignore rules
│
└── .streamlit/
    └── config.toml                 # Streamlit configuration

```

## File Descriptions

### Core Application Files

#### `app.py` (Main Application - ~400 lines)
- **Purpose**: Main Streamlit application
- **Features**:
  - Portfolio view with metrics and tables
  - Single product view with detailed analysis
  - Multi-tab interface for different analyses
  - Version history tracking
  - Scenario comparison
  - Interactive visualizations
  - Session state management
- **Key Components**:
  - Header and navigation
  - View mode toggle (Portfolio/Single)
  - Sidebar for product selection
  - Tabbed interface for analysis
  - Footer with metadata

#### `config.py` (Configuration & Constants - ~200 lines)
- **Purpose**: Centralized configuration
- **Contains**:
  - Product data (4 products with full details)
  - Archetype definitions (7 archetypes)
  - Version history data
  - Color schemes
  - Timeline data
  - Financial calculation factors
  - Payers list
  - Revenue waterfall components
- **Advantages**:
  - Easy data updates
  - Centralized constants
  - Reusable configurations

#### `utils.py` (Utility Functions - ~250 lines)
- **Purpose**: Helper and utility functions
- **Functions**:
  - `get_priority_color()` - Color mapping for priorities
  - `get_archetype_color()` - Color mapping for archetypes
  - `get_product_by_id()` - Product lookup
  - `calculate_portfolio_metrics()` - Portfolio calculations
  - `calculate_financial_metrics()` - Financial calculations
  - `create_*_dataframe()` - DataFrame builders
  - `format_currency()` / `format_percentage()` - Formatters
  - Filter functions (by priority, phase, archetype)
- **Benefits**:
  - Code reusability
  - Maintainability
  - Testability

### Documentation Files

#### `README.md` (Main Documentation)
- Project overview
- Feature list
- Product data summary
- Archetype distribution
- Installation instructions
- Running the application
- Application structure
- Financial calculations
- User interactions
- Customization guide
- Future enhancements
- Dependencies
- Technical notes

#### `QUICKSTART.md` (Quick Start Guide)
- Prerequisites
- Step-by-step setup
- Running the app
- Features overview
- Troubleshooting
- File structure
- Data modifications
- Keyboard shortcuts
- Performance tips

#### `DEPLOYMENT.md` (Deployment Guide)
- Local deployment steps
- Streamlit Cloud deployment
- Heroku deployment
- Docker deployment
- AWS EC2 deployment
- Environment variables
- Monitoring & maintenance
- Performance optimization
- Security considerations
- Scaling strategies
- Backup & recovery

#### `PROJECT_STRUCTURE.md` (This File)
- File organization
- File descriptions
- Data models
- Component overview
- Dependencies
- Usage patterns

### Configuration Files

#### `requirements.txt`
```
streamlit==1.28.1
pandas==2.1.1
plotly==5.17.0
numpy==1.24.3
```

#### `.streamlit/config.toml`
- Theme configuration
- Color scheme
- Client settings
- Logger configuration

#### `.gitignore`
- Python artifacts
- Virtual environments
- IDE files
- OS files
- Project-specific files

## Data Models

### Product Structure
```python
{
    "id": "PRODUCT-001",
    "name": "Biosimilar Humira (Adalimumab)",
    "archetype": "Med Benefit High",
    "phase": "Pre-Launch",
    "launchDate": "2026-Q2",
    "territory": "US",
    "priority": "High",
    "npv": 245.6,
    "assumptions": {
        "uptake": {"y1": 8, "y2": 15, ...},
        "peakShare": 32,
        "pricing": {"wac": 850, ...},
        "access": {"tier1": 60, ...},
        "competition": "High (5+ competitors)",
        "jcode": "Applied - 18mo to launch",
        "distribution": "Specialty + Limited"
    },
    "lastUpdated": "2026-01-28",
    "updatedBy": "Sarah Chen (US Market Access)"
}
```

### Archetype Structure
```python
{
    "name": "Med Benefit High",
    "color": "#0066CC",
    "count": 8
}
```

### Version History Structure
```python
{
    "version": "v1.3",
    "date": "2026-01-28",
    "user": "Sarah Chen",
    "changes": ["Updated GTN% from 42% to 45%", ...],
    "npvImpact": 12.3,
    "status": "Current"
}
```

## Component Overview

### Portfolio View Components
1. **Header Section**
   - Title and subtitle
   - Company branding
   - Navigation buttons

2. **Summary Metrics**
   - Total Pipeline NPV
   - Product count
   - High priority assets
   - Launches this year

3. **Archetype Distribution**
   - 7 archetype cards
   - Color-coded circles
   - Product counts

4. **Portfolio Table**
   - Product listing
   - Key metrics
   - Last update info
   - Action buttons

### Single Product View Components
1. **Sidebar**
   - Product selector
   - Quick actions
   - Product summary

2. **Main Content**
   - Product header
   - Tabbed interface
   - Version history (optional)
   - Scenario comparison (optional)

3. **Tabs**
   - Assumptions
   - Financials
   - Access
   - Timeline

## Dependencies

### Core Framework
- **streamlit**: Web application framework

### Data Processing
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing

### Visualization
- **plotly**: Interactive charts and graphs

## Usage Patterns

### Session State Management
```python
if "view_mode" not in st.session_state:
    st.session_state.view_mode = "portfolio"
```

### View Switching
```python
if st.button("Single Product View"):
    st.session_state.view_mode = "single"
```

### Product Selection
```python
selected = st.sidebar.selectbox("Select product", product_ids)
st.session_state.selected_product = selected
```

### Data Retrieval
```python
from config import PIPELINE_PRODUCTS
from utils import get_product_by_id

product = get_product_by_id(product_id)
```

### Metrics Calculation
```python
from utils import calculate_portfolio_metrics

metrics = calculate_portfolio_metrics()
```

## Key Features

### 📊 Analytics
- Portfolio metrics and KPIs
- Financial projections
- Archetype distribution
- Phase tracking

### 📈 Visualizations
- Summary cards
- Revenue waterfall
- Interactive tables
- Scenario comparisons

### 🎯 Navigation
- View mode toggle
- Product selector
- Tab navigation
- Quick actions

### 🔍 Details
- Product assumptions
- Market access strategy
- Timeline tracking
- Version history

## Performance Considerations

1. **State Management**
   - Uses session state for view persistence
   - Minimizes re-renders

2. **Data Loading**
   - Static data in config.py
   - No external API calls
   - Fast initial load

3. **Calculations**
   - Done on-demand
   - Lightweight operations
   - No heavy processing

## Customization Points

1. **Data**
   - Modify `config.py`
   - Update product information
   - Add/remove archetypes

2. **Styling**
   - Edit CSS in `app.py`
   - Adjust colors in `config.py`
   - Modify `.streamlit/config.toml`

3. **Functionality**
   - Add new tabs in single view
   - Add new metrics
   - Create new utility functions

## Testing Checklist

- [ ] Portfolio view renders correctly
- [ ] All 4 products display
- [ ] Archetype distribution shows 7 categories
- [ ] Metrics calculations are accurate
- [ ] Single product view displays details
- [ ] All tabs work properly
- [ ] Version history displays correctly
- [ ] Scenario comparison calculates correctly
- [ ] Navigation works smoothly
- [ ] Export to CSV works

## Version History

**Version 1.0.0** - 2026-02-04
- Initial release
- Full portfolio and single product views
- All financial calculations
- Version history tracking
- Scenario comparison

---

**Last Updated**: 2026-02-04  
**Status**: Production Ready
