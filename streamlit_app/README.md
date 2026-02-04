# Sandoz Pipeline Decision System - Streamlit Version

A comprehensive pharmaceutical pipeline management and NPV tracking application built with Streamlit.

## Features

### 📊 Portfolio View
- **Summary Metrics**: Total Pipeline NPV, Product Count, Priority Assets, Launch Timeline
- **Archetype Distribution**: Visual breakdown of products by archetype with color-coded categories
- **Portfolio Table**: Comprehensive table view of all products with detailed information
- **Export Functionality**: Download portfolio data as CSV

### 📦 Single Product View
- **Product Details**: Complete information for selected product
- **Assumptions Tab**: Market uptake, pricing, GTN, access tiers, and distribution channels
- **Financials Tab**: NPV, 5-year revenue projections, and revenue waterfall analysis
- **Access Tab**: Market access strategy, target payers, and key milestones
- **Timeline Tab**: Product development timeline with key dates
- **Version History**: Audit trail with version control and NPV impact tracking
- **Scenario Comparison**: Base case, optimistic, and conservative scenarios

## Product Data

### Portfolio Products
1. **Biosimilar Humira (Adalimumab)** - $245.6M NPV
   - Phase: Pre-Launch (2026-Q2)
   - Priority: High
   - Archetype: Med Benefit High

2. **Biosimilar Enbrel (Etanercept)** - $178.3M NPV
   - Phase: Filed (2026-Q4)
   - Priority: Medium
   - Archetype: Med Benefit Med

3. **Generic Lyrica (Pregabalin)** - $189.4M NPV
   - Phase: Pre-Launch (2026-Q3)
   - Priority: High
   - Archetype: Rx Benefit High

4. **Rare Disease Gene Therapy** - $312.8M NPV
   - Phase: Phase 3 (2027-Q2)
   - Priority: Strategic
   - Archetype: Rare Disease

**Total Portfolio NPV: $926.1M**

## Archetype Distribution

| Archetype | Count | Color |
|-----------|-------|-------|
| Med Benefit High | 8 | #0066CC |
| Med Benefit Med | 6 | #4A90E2 |
| Med Benefit Low | 4 | #7AB8FF |
| Rx Benefit High | 7 | #00A86B |
| Rx Benefit Med | 5 | #52C993 |
| Rx Benefit Low | 3 | #8FE5B8 |
| Rare Disease | 2 | #9B59B6 |

## Installation

1. **Clone or download the project**
   ```bash
   cd Sandoz_pipeline_streamlit
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## Application Structure

### Data Models
- **Pipeline Products**: Complete product information with assumptions and metrics
- **Archetypes**: Product categorization for portfolio analysis
- **Version History**: Audit trail with change tracking
- **Financial Metrics**: NPV, revenue projections, and waterfall analysis

### Key Functions
- `get_priority_color()`: Maps priority levels to colors
- `get_archetype_color()`: Maps archetypes to brand colors
- `get_phase_color()`: Maps development phases to colors

### Session State Management
- `view_mode`: Portfolio vs Single Product view
- `selected_product`: Currently selected product ID
- `active_tab`: Current tab in product view

## Views

### Portfolio View
The default view showing:
- High-level portfolio metrics
- Archetype distribution visualization
- Complete product portfolio table
- Export and navigation options

### Single Product View
Detailed product analysis with:
- Left sidebar for product selection and quick actions
- Tabbed interface for different analysis areas
- Version history and scenario comparison options
- Dynamic financial calculations

## Financial Calculations

### NPV Impact
- Base case: Current product NPV
- Optimistic scenario: NPV × 1.25
- Conservative scenario: NPV × 0.75

### Revenue Projections
- 5-Year Revenue: NPV × 1.8
- Peak Year Revenue: NPV × 0.45
- Year 1 Revenue Waterfall included

### Uptake Assumptions
5-year uptake trajectory with peak market share calculations for each product

## User Interactions

1. **View Toggle**: Switch between Portfolio and Single Product views
2. **Product Selection**: Dropdown to select different products in sidebar
3. **Tab Navigation**: Four main tabs for different analysis types
4. **Quick Actions**: Toggle version history and scenario comparison
5. **Export**: Download portfolio data as CSV file
6. **Navigation**: Buttons to switch between views

## Customization

To modify product data:
1. Edit the `PIPELINE_PRODUCTS` list in `app.py`
2. Update `ARCHETYPES` for different archetype configurations
3. Modify `VERSION_HISTORY` for product version tracking

To customize styling:
1. Edit the `st.markdown()` CSS section at the top of the app
2. Modify color schemes in the helper functions
3. Adjust layout using Streamlit column/container utilities

## Future Enhancements

- Add scenario modeling with parameter adjustment
- Integration with database for persistent data storage
- User authentication and role-based access control
- Advanced analytics and forecasting models
- Real-time data updates and notifications
- Multi-user collaboration features

## Dependencies

- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **plotly**: Interactive visualizations
- **numpy**: Numerical computing

## Technical Notes

- Built with Streamlit 1.28.1
- Responsive design for various screen sizes
- Session state management for seamless navigation
- Interactive visualizations using Plotly
- Markdown-based custom styling

## Support

For issues or questions about the application, please refer to the code comments or contact the development team.

---

**Version:** 1.0.0  
**Last Updated:** 2026-02-04  
**Status:** Production Ready
