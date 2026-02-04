import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from enum import Enum
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Sandoz Pipeline Decision System",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f0f4f8 0%, #e8eef5 100%);
    }
    
    /* Enhanced metric card */
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.12), 0 1px 3px rgba(0,0,0,0.08);
        border-left: 5px solid #2563eb;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        box-shadow: 0 8px 32px rgba(0,0,0,0.16), 0 2px 6px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    
    .metric-value {
        font-size: 32px;
        font-weight: 800;
        color: #1f2937;
        text-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .metric-label {
        font-size: 12px;
        color: #6b7280;
        margin-bottom: 8px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Product card with depth */
    .product-card {
        background: white;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        margin-bottom: 12px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .product-card:hover {
        box-shadow: 0 8px 24px rgba(37, 99, 235, 0.15), 0 4px 12px rgba(0,0,0,0.1);
        transform: translateY(-2px);
        border-color: #3b82f6;
    }
    
    .section-header {
        font-size: 20px;
        font-weight: 800;
        color: #1f2937;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        text-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    /* Enhanced Tab styling */
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 16px;
        font-weight: 700;
        padding: 14px 28px;
        border-radius: 10px;
        background-color: #f3f4f6;
        color: #374151;
        border: 2px solid #d1d5db;
        margin-right: 12px;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    
    .stTabs [data-baseweb="tab-list"] button:hover {
        background-color: #e5e7eb;
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border: 2px solid #1d4ed8;
        box-shadow: 0 8px 24px rgba(59, 130, 246, 0.5), 0 4px 12px rgba(59, 130, 246, 0.3);
        font-weight: 800;
    }
    
    /* Colored containers for sections with enhanced shadows */
    .uptake-container {
        background: linear-gradient(135deg, #e0f2fe 0%, #f0f9ff 100%);
        padding: 18px;
        border-radius: 14px;
        border-left: 6px solid #0284c7;
        margin: 16px 0;
        box-shadow: 0 4px 16px rgba(2, 132, 199, 0.15), 0 2px 8px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
    }
    
    .uptake-container:hover {
        box-shadow: 0 8px 28px rgba(2, 132, 199, 0.25), 0 4px 12px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    
    .pricing-container {
        background: linear-gradient(135deg, #f0fdf4 0%, #f7fee7 100%);
        padding: 18px;
        border-radius: 14px;
        border-left: 6px solid #65a30d;
        margin: 16px 0;
        box-shadow: 0 4px 16px rgba(101, 163, 13, 0.15), 0 2px 8px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
    }
    
    .pricing-container:hover {
        box-shadow: 0 8px 28px rgba(101, 163, 13, 0.25), 0 4px 12px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    
    .access-container {
        background: linear-gradient(135deg, #fef3c7 0%, #fffbeb 100%);
        padding: 18px;
        border-radius: 14px;
        border-left: 6px solid #ca8a04;
        margin: 16px 0;
        box-shadow: 0 4px 16px rgba(202, 138, 4, 0.15), 0 2px 8px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
    }
    
    .access-container:hover {
        box-shadow: 0 8px 28px rgba(202, 138, 4, 0.25), 0 4px 12px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    
    .section-title {
        font-size: 18px;
        font-weight: 800;
        color: #1f2937;
        margin-bottom: 12px;
        text-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    /* Enhanced Financial metrics card */
    .financial-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 28px;
        border-radius: 16px;
        color: white;
        box-shadow: 0 12px 40px rgba(102, 126, 234, 0.5), 0 6px 20px rgba(118, 75, 162, 0.3), inset 0 1px 0 rgba(255,255,255,0.2);
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .financial-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        transition: left 0.6s;
    }
    
    .financial-card:hover::before {
        left: 100%;
    }
    
    .financial-card:hover {
        transform: translateY(-6px) scale(1.02);
        box-shadow: 0 16px 56px rgba(102, 126, 234, 0.6), 0 8px 28px rgba(118, 75, 162, 0.4);
    }
    
    .financial-value {
        font-size: 36px;
        font-weight: 900;
        color: white;
        letter-spacing: -1px;
        text-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
    
    .financial-label {
        font-size: 14px;
        color: rgba(255,255,255,0.95);
        margin-top: 10px;
        font-weight: 700;
        letter-spacing: 0.3px;
    }
    
    .financial-subtitle {
        font-size: 12px;
        color: rgba(255,255,255,0.75);
        margin-top: 6px;
        font-weight: 500;
    }
    
    /* Enhanced Data display cards */
    .data-card {
        background: white;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        margin: 12px 0;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08), 0 1px 4px rgba(0,0,0,0.04);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .data-card:hover {
        box-shadow: 0 8px 24px rgba(37, 99, 235, 0.2), 0 4px 12px rgba(0,0,0,0.12);
        border-color: #3b82f6;
        transform: translateY(-3px);
        background: linear-gradient(135deg, #ffffff 0%, #f8fbff 100%);
    }
    
    .data-card-title {
        font-weight: 700;
        color: #1f2937;
        font-size: 14px;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.4px;
        opacity: 0.8;
    }
    
    .data-card-value {
        font-size: 22px;
        font-weight: 900;
        color: #2563eb;
        text-shadow: 0 1px 3px rgba(37, 99, 235, 0.1);
    }
    
    /* Dataframe styling */
    .stDataFrame {
        border-radius: 12px !important;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1) !important;
        overflow: hidden !important;
    }
    
    /* Button styling */
    .stButton > button {
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
        font-weight: 700;
        border: none;
        transition: all 0.3s ease;
        letter-spacing: 0.3px;
    }
    
    .stButton > button:hover {
        box-shadow: 0 8px 24px rgba(37, 99, 235, 0.4);
        transform: translateY(-2px);
    }
    
    </style>
           
            
""", unsafe_allow_html=True)

# Formatting functions
def format_number(num, decimals=1):
    """Format number with commas (international system)"""
    if isinstance(num, (int, float)):
        return f"{num:,.{decimals}f}"
    return str(num)

def format_currency(num, symbol="$"):
    """Format as currency with commas"""
    if isinstance(num, (int, float)):
        return f"{symbol}{num:,.1f}M" if num >= 1 else f"{symbol}{num*1000:,.0f}K"
    return str(num)

def format_percent(num):
    """Format as percentage"""
    if isinstance(num, (int, float)):
        return f"{num:.1f}%"
    return str(num)

# Data structures
class Priority(Enum):
    HIGH = "High"
    STRATEGIC = "Strategic"
    MEDIUM = "Medium"
    LOW = "Low"

class Phase(Enum):
    PRE_LAUNCH = "Pre-Launch"
    FILED = "Filed"
    PHASE_3 = "Phase 3"

# Pipeline products data
PIPELINE_PRODUCTS = [
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
            "uptake": {"y1": 8, "y2": 15, "y3": 22, "y4": 28, "y5": 32},
            "peakShare": 32,
            "pricing": {"wac": 850, "asp": 765, "gtn": 45},
            "access": {"tier1": 60, "tier2": 30, "tier3": 10},
            "competition": "High (5+ competitors)",
            "jcode": "Applied - 18mo to launch",
            "distribution": "Specialty + Limited"
        },
        "lastUpdated": "2026-01-28",
        "updatedBy": "Sarah Chen (US Market Access)"
    },
    {
        "id": "PRODUCT-002",
        "name": "Biosimilar Enbrel (Etanercept)",
        "archetype": "Med Benefit Med",
        "phase": "Filed",
        "launchDate": "2026-Q4",
        "territory": "US",
        "priority": "Medium",
        "npv": 178.3,
        "assumptions": {
            "uptake": {"y1": 6, "y2": 12, "y3": 18, "y4": 24, "y5": 28},
            "peakShare": 28,
            "pricing": {"wac": 720, "asp": 648, "gtn": 42},
            "access": {"tier1": 55, "tier2": 35, "tier3": 10},
            "competition": "Medium (3-4 competitors)",
            "jcode": "Pending - 24mo to launch",
            "distribution": "Specialty"
        },
        "lastUpdated": "2026-01-25",
        "updatedBy": "Michael Torres (Global BD)"
    },
    {
        "id": "PRODUCT-003",
        "name": "Generic Lyrica (Pregabalin)",
        "archetype": "Rx Benefit High",
        "phase": "Pre-Launch",
        "launchDate": "2026-Q3",
        "territory": "US",
        "priority": "High",
        "npv": 189.4,
        "assumptions": {
            "uptake": {"y1": 25, "y2": 38, "y3": 45, "y4": 48, "y5": 50},
            "peakShare": 50,
            "pricing": {"wac": 45, "asp": 38, "gtn": 65},
            "access": {"tier1": 85, "tier2": 12, "tier3": 3},
            "competition": "High (10+ competitors)",
            "jcode": "N/A - Retail",
            "distribution": "Retail + Specialty"
        },
        "lastUpdated": "2026-01-27",
        "updatedBy": "Jennifer Liu (US Market Access)"
    },
    {
        "id": "PRODUCT-004",
        "name": "Rare Disease Gene Therapy",
        "archetype": "Rare Disease",
        "phase": "Phase 3",
        "launchDate": "2027-Q2",
        "territory": "US",
        "priority": "Strategic",
        "npv": 312.8,
        "assumptions": {
            "uptake": {"y1": 3, "y2": 6, "y3": 9, "y4": 12, "y5": 15},
            "peakShare": 15,
            "pricing": {"wac": 125000, "asp": 115000, "gtn": 28},
            "access": {"tier1": 40, "tier2": 35, "tier3": 25},
            "competition": "Low (1-2 competitors)",
            "jcode": "To be applied - 36mo to launch",
            "distribution": "Ultra-Specialty + Hub"
        },
        "lastUpdated": "2026-01-20",
        "updatedBy": "David Park (Global Rare Disease)"
    }
]

# Archetype data
ARCHETYPES = [
    {"name": "Med Benefit High", "color": "#0066CC", "count": 8},
    {"name": "Med Benefit Med", "color": "#4A90E2", "count": 6},
    {"name": "Med Benefit Low", "color": "#7AB8FF", "count": 4},
    {"name": "Rx Benefit High", "color": "#00A86B", "count": 7},
    {"name": "Rx Benefit Med", "color": "#52C993", "count": 5},
    {"name": "Rx Benefit Low", "color": "#8FE5B8", "count": 3},
    {"name": "Rare Disease", "color": "#9B59B6", "count": 2}
]

# Version history data
VERSION_HISTORY = [
    {
        "version": "v1.3",
        "date": "2026-01-28",
        "user": "Sarah Chen",
        "changes": ["Updated GTN% from 42% to 45%", "Revised Tier 1 access from 55% to 60%"],
        "npvImpact": 12.3,
        "status": "Current"
    },
    {
        "version": "v1.2",
        "date": "2026-01-15",
        "user": "Michael Torres",
        "changes": ["Adjusted Y1 uptake from 6% to 8%", "Updated competition assessment"],
        "npvImpact": 8.7,
        "status": "Approved"
    },
    {
        "version": "v1.1",
        "date": "2025-12-20",
        "user": "Jennifer Liu",
        "changes": ["Initial US market assumptions", "Added J-code timeline"],
        "npvImpact": 15.2,
        "status": "Approved"
    },
    {
        "version": "v1.0",
        "date": "2025-12-01",
        "user": "David Park",
        "changes": ["Created baseline forecast from Global assumptions"],
        "npvImpact": 0,
        "status": "Baseline"
    }
]

# Helper functions
def get_priority_color(priority):
    colors = {
        "High": "#E74C3C",
        "Strategic": "#9B59B6",
        "Medium": "#F39C12",
        "Low": "#95A5A6"
    }
    return colors.get(priority, "#95A5A6")

def get_archetype_color(archetype):
    for arch in ARCHETYPES:
        if arch["name"] == archetype:
            return arch["color"]
    return "#95A5A6"

def get_phase_color(phase):
    colors = {
        "Pre-Launch": "#3B82F6",
        "Filed": "#F59E0B",
        "Phase 3": "#8B5CF6"
    }
    return colors.get(phase, "#6B7280")

# Initialize session state
if "view_mode" not in st.session_state:
    st.session_state.view_mode = "portfolio"
if "selected_product" not in st.session_state:
    st.session_state.selected_product = "PRODUCT-001"
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "assumptions"

# Beautiful Header Container with Logo and Title
header_col1, header_col2, header_col3 = st.columns([0.2, 0.6, 0.2])

with header_col1:
    st.markdown("<br>", unsafe_allow_html=True)
    # Handle logo with proper path for cloud deployment
    logo_path = Path(__file__).parent / "Sandoz.png"
    if logo_path.exists():
        st.image(str(logo_path), use_container_width=True)
    else:
        st.write("📦")  # Fallback if logo not found

with header_col2:
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h1 style="margin: 0; font-size: 48px; font-weight: 900; color: #0055CC; letter-spacing: -1px; text-shadow: 0 1px 4px rgba(0,85,204,0.1);">
            Pipeline Decision System
        </h1>
        <p style="margin: 12px 0 0 0; font-size: 16px; color: #004499; font-weight: 500; letter-spacing: 0.3px;">
            Centralized Portfolio Management & NPV Tracking
        </p>
    </div>
    """, unsafe_allow_html=True)

with header_col3:
    st.markdown("")

# st.markdown("")

# View mode toggle


col1, col2, col3 = st.columns([0.3, 0.01, 0.3])
with col1:
    if st.button("📦 Single Product View", use_container_width=True, 
                 key="btn_single",
                 help="View detailed information for a single product"):
        st.session_state.view_mode = "single"
with col3:
    if st.button("📊 Portfolio View", use_container_width=True,
                 key="btn_portfolio",
                 help="View all products in the portfolio"):
        st.session_state.view_mode = "portfolio"


# st.markdown("---")

# PORTFOLIO VIEW
if st.session_state.view_mode == "portfolio":
    # Enhanced Portfolio Overview Header
    st.markdown("""
    <div style="text-align: center; padding: 12px 0; margin-bottom: 14px;">
        <h2 style="margin: 0; font-size: 28px; font-weight: 900; color: #0055CC; letter-spacing: -1px;">📈 Portfolio Overview</h2>
        <p style="margin: 4px 0 0 0; color: #6b7280; font-size: 13px;">Real-time insights across 4 pipeline products</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Calculate metrics
    portfolio_npv = sum(p["npv"] for p in PIPELINE_PRODUCTS)
    high_priority_count = len([p for p in PIPELINE_PRODUCTS if p["priority"] in ["High", "Strategic"]])
    products_count = len(PIPELINE_PRODUCTS)
    launches_this_year = 3
    
    # Wrap metrics in enhanced card container with gradient
    # st.markdown("""
    # <div class="metrics-overview-card" style="background: linear-gradient(135deg, #f0f9ff 0%, #fafbfc 100%); border: 2px solid #0055CC33; padding: 18px 16px;">
    # """, unsafe_allow_html=True)
    
    # Summary metrics with custom styling
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4, gap="small")
    
    with metric_col1:
        st.markdown(f"""
        <div style="text-align: center; padding: 16px 12px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; box-shadow: 0 4px 12px rgba(102, 126, 234, 0.25), 0 2px 6px rgba(0,0,0,0.08); transition: all 0.3s ease;">
            <div style="font-size: 11px; color: rgba(255,255,255,0.9); font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 8px;">Total Pipeline NPV</div>
            <div style="font-size: 32px; font-weight: 900; color: white; text-shadow: 0 2px 8px rgba(0,0,0,0.2); letter-spacing: -1px;">${portfolio_npv:.1f}M</div>
            <div style="font-size: 10px; color: rgba(255,255,255,0.75); margin-top: 4px; font-weight: 500;">Across all products</div>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_col2:
        st.markdown(f"""
        <div style="text-align: center; padding: 16px 12px; background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%); border-radius: 10px; box-shadow: 0 4px 12px rgba(14, 165, 233, 0.25), 0 2px 6px rgba(0,0,0,0.08); transition: all 0.3s ease;">
            <div style="font-size: 11px; color: rgba(255,255,255,0.9); font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 8px;">Products in Pipeline</div>
            <div style="font-size: 32px; font-weight: 900; color: white; text-shadow: 0 2px 8px rgba(0,0,0,0.2); letter-spacing: -1px;">{products_count}</div>
            <div style="font-size: 10px; color: rgba(255,255,255,0.75); margin-top: 4px; font-weight: 500;">Active programs</div>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_col3:
        st.markdown(f"""
        <div style="text-align: center; padding: 16px 12px; background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); border-radius: 10px; box-shadow: 0 4px 12px rgba(245, 158, 11, 0.25), 0 2px 6px rgba(0,0,0,0.08); transition: all 0.3s ease;">
            <div style="font-size: 11px; color: rgba(255,255,255,0.9); font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 8px;">High Priority Assets</div>
            <div style="font-size: 32px; font-weight: 900; color: white; text-shadow: 0 2px 8px rgba(0,0,0,0.2); letter-spacing: -1px;">{high_priority_count}</div>
            <div style="font-size: 10px; color: rgba(255,255,255,0.75); margin-top: 4px; font-weight: 500;">Strategic focus</div>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_col4:
        st.markdown(f"""
        <div style="text-align: center; padding: 16px 12px; background: linear-gradient(135deg, #10b981 0%, #059669 100%); border-radius: 10px; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.25), 0 2px 6px rgba(0,0,0,0.08); transition: all 0.3s ease;">
            <div style="font-size: 11px; color: rgba(255,255,255,0.9); font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 8px;">Launches This Year</div>
            <div style="font-size: 32px; font-weight: 900; color: white; text-shadow: 0 2px 8px rgba(0,0,0,0.2); letter-spacing: -1px;">{launches_this_year}</div>
            <div style="font-size: 10px; color: rgba(255,255,255,0.75); margin-top: 4px; font-weight: 500;">Upcoming events</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Archetype Distribution with enhanced styling
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h3 style="margin: 0; font-size: 28px; font-weight: 800; color: #1f2937; letter-spacing: -0.5px;">🎯 Portfolio by Archetype</h3>
        <p style="margin: 8px 0 0 0; color: #6b7280; font-size: 14px;">Distribution across 7 product archetypes</p>
    </div>
    """, unsafe_allow_html=True)
    
    # st.markdown('<div class="portfolio-card-wrapper" style="padding: 28px; background: linear-gradient(135deg, #fafbfc 0%, #f8f9fa 100%);">', unsafe_allow_html=True)
    
    arch_cols = st.columns(7, gap="medium")
    for idx, archetype in enumerate(ARCHETYPES):
        with arch_cols[idx]:
            st.markdown(f"""
            <div class="archetype-card" style='border-color: {archetype['color']}; background: white; padding: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.08);'>
                <div style='width: 70px; height: 70px; border-radius: 50%; background: linear-gradient(135deg, {archetype['color']} 0%, {archetype['color']}dd 100%); 
                            margin: 0 auto 14px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 900; font-size: 24px; box-shadow: 0 6px 20px {archetype['color']}50; transition: all 0.3s ease;'>
                    {archetype['count']}
                </div>
                <p style='font-size: 13px; margin: 0; font-weight: 700; color: #1f2937; text-align: center; line-height: 1.4;'>{archetype['name']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Portfolio Table with enhanced header
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h3 style="margin: 0; font-size: 28px; font-weight: 800; color: #1f2937; letter-spacing: -0.5px;">📋 Pipeline Portfolio Overview</h3>
        <p style="margin: 8px 0 0 0; color: #6b7280; font-size: 14px;">Complete financial and strategic view of all products</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="portfolio-table-card">', unsafe_allow_html=True)
    
    # Table header
    st.markdown("""
    <div style="display: grid; grid-template-columns: 2fr 1.2fr 1.2fr 1.2fr 1.2fr 1.2fr 1fr; gap: 12px; padding: 16px 12px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px 10px 0 0; margin-bottom: 0;">
        <div style="color: white; font-weight: 800; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;">Product</div>
        <div style="color: white; font-weight: 800; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;">Archetype</div>
        <div style="color: white; font-weight: 800; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;">Launch</div>
        <div style="color: white; font-weight: 800; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;">NPV</div>
        <div style="color: white; font-weight: 800; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;">5-Yr Rev</div>
        <div style="color: white; font-weight: 800; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;">Peak Rev</div>
        <div style="color: white; font-weight: 800; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;">Priority</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Table rows
    for idx, product in enumerate(PIPELINE_PRODUCTS):
        priority_color = get_priority_color(product['priority'])
        phase_color = get_phase_color(product['phase'])
        archetype_color = get_archetype_color(product['archetype'])
        
        # Calculate metrics
        five_year_rev = product['npv'] * 1.8
        peak_rev = product['npv'] * 0.45
        
        # Alternating row colors
        bg_color = "#ffffff" if idx % 2 == 0 else "#f9fafb"
        border_bottom = "border-bottom: 1px solid #e5e7eb;" if idx < len(PIPELINE_PRODUCTS) - 1 else ""
        
        st.markdown(f"""
        <div style="display: grid; grid-template-columns: 2fr 1.2fr 1.2fr 1.2fr 1.2fr 1.2fr 1fr; gap: 12px; padding: 16px 12px; background-color: {bg_color}; {border_bottom}">
            <div>
                <div style="font-weight: 700; color: #1f2937; font-size: 14px;">{product['name']}</div>
                <div style="font-size: 11px; color: #6b7280; margin-top: 4px;">ID: {product['id']}</div>
            </div>
            <div style="display: flex; align-items: center;">
                <span style="background: {archetype_color}20; color: {archetype_color}; padding: 8px 12px; border-radius: 6px; font-size: 12px; font-weight: 700; border-left: 3px solid {archetype_color};">{product['archetype']}</span>
            </div>
            <div style="display: flex; align-items: center;">
                <span style="background: #f3f4f6; padding: 6px 10px; border-radius: 6px; font-size: 12px; font-weight: 600; color: #1f2937;">{product['launchDate']}</span>
            </div>
            <div style="display: flex; align-items: center;">
                <span style="background: linear-gradient(135deg, #ede9fe, #f5f3ff); padding: 8px 12px; border-radius: 6px; font-size: 13px; font-weight: 800; color: #7c3aed; border-left: 3px solid #a78bfa;">${format_number(product['npv'], 1)}M</span>
            </div>
            <div style="display: flex; align-items: center;">
                <span style="background: linear-gradient(135deg, #dbeafe, #eff6ff); padding: 8px 12px; border-radius: 6px; font-size: 13px; font-weight: 800; color: #1d4ed8; border-left: 3px solid #3b82f6;">${format_number(five_year_rev, 1)}M</span>
            </div>
            <div style="display: flex; align-items: center;">
                <span style="background: linear-gradient(135deg, #dcfce7, #f0fdf4); padding: 8px 12px; border-radius: 6px; font-size: 13px; font-weight: 800; color: #15803d; border-left: 3px solid #16a34a;">${format_number(peak_rev, 1)}M</span>
            </div>
            <div style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap;">
                <span style="background: {priority_color}30; color: {priority_color}; padding: 4px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.3px;">{product['priority']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Table footer
    st.markdown("""
    <div style="background: #f9fafb; padding: 12px; border-radius: 0 0 10px 10px; border-top: 2px solid #e5e7eb; margin-top: 0; font-size: 11px; color: #6b7280;">
        Last updated: Portfolio data refreshed daily | Total Assets: 4 Products
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("View Single Product Details", use_container_width=True):
            st.session_state.view_mode = "single"
            st.rerun()
    
    with col2:
        # Create CSV data
        df_export = pd.DataFrame([{
            "Product": p["name"],
            "ID": p["id"],
            "Archetype": p["archetype"],
            "Phase": p["phase"],
            "Launch Date": p["launchDate"],
            "Priority": p["priority"],
            "NPV ($M)": f"{p['npv']:.1f}",
            "Last Updated": p["lastUpdated"]
        } for p in PIPELINE_PRODUCTS])
        
        st.download_button(
            label="📥 Export to CSV",
            data=df_export.to_csv(index=False),
            file_name="portfolio.csv",
            mime="text/csv",
            use_container_width=True
        )

# SINGLE PRODUCT VIEW
else:
    # Product selector as top bar
    st.markdown("---")
    
    # Product selection dropdown in main area (not sidebar)
    col_select, col_space = st.columns([0.4, 0.6])
    
    with col_select:
        selected = st.selectbox(
            "🔍 Select Product",
            options=[p["id"] for p in PIPELINE_PRODUCTS],
            format_func=lambda x: next((p["name"] for p in PIPELINE_PRODUCTS if p["id"] == x), x),
            index=[p["id"] for p in PIPELINE_PRODUCTS].index(st.session_state.selected_product),
            key="product_selector",
            on_change=lambda: setattr(st.session_state, 'selected_product', st.session_state.product_selector)
        )
    
    current_product = next((p for p in PIPELINE_PRODUCTS if p["id"] == st.session_state.selected_product), None)
    
    if current_product:
        # Quick actions and summary in top banner
        col1, col2, col3, col4 = st.columns([0.25, 0.25, 0.25, 0.25])

        with col1:
            show_version_history = st.checkbox("📜 History", False, key="version_history")
            show_scenario = st.checkbox("🔀 Scenarios", False, key="scenario_comp")
        
        with col2:
            st.metric("NPV", f"${format_number(current_product['npv'], 1)}M")
        
        with col3:
            st.metric("Phase", current_product['phase'])
        
        with col4:
            st.metric("Launch", current_product['launchDate'])



        st.markdown("---")
        
        # Product header - centered and prominent with enhanced styling
        st.markdown(f"""
        <div style="text-align: center; padding: 28px 24px; background: linear-gradient(135deg, #0055CC 0%, #003d99 100%); border-radius: 16px; margin: 20px 0; box-shadow: 0 8px 32px rgba(0,85,204,0.3), 0 4px 16px rgba(0,0,0,0.1); border: 2px solid rgba(255,255,255,0.2);">
            <h2 style="margin: 0; color: white; font-size: 36px; font-weight: 900; letter-spacing: -1px; text-shadow: 0 2px 8px rgba(0,0,0,0.2);">{current_product['name']}</h2>
            <p style="margin: 10px 0 0 0; color: rgba(255,255,255,0.9); font-size: 14px; font-weight: 600; letter-spacing: 0.5px;">ID: {current_product['id']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Product badges in a clean row with enhanced styling
        badge_col1, badge_col2, badge_col3, badge_col_space = st.columns([0.25, 0.25, 0.25, 0.25])
        
        with badge_col1:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #ede9fe 0%, #f3e8ff 100%); padding: 16px 14px; border-radius: 12px; text-align: center; border: 2px solid #c4b5fd; box-shadow: 0 4px 16px rgba(124, 58, 237, 0.15);">
                <div style="font-size: 11px; color: #6b7280; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 8px;">Archetype</div>
                <div style="font-size: 16px; color: #7c3aed; font-weight: 900; letter-spacing: -0.5px;">{current_product['archetype']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with badge_col2:
            priority_color = "#10b981" if current_product['priority'] == "High" else "#3b82f6" if current_product['priority'] == "Medium" else "#f59e0b"
            priority_bg_start = "#d1fae5" if current_product['priority'] == "High" else "#dbeafe" if current_product['priority'] == "Medium" else "#fef3c7"
            priority_bg_end = "#a7f3d0" if current_product['priority'] == "High" else "#bfdbfe" if current_product['priority'] == "Medium" else "#fde68a"
            priority_border = "#6ee7b7" if current_product['priority'] == "High" else "#93c5fd" if current_product['priority'] == "Medium" else "#fcd34d"
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {priority_bg_start} 0%, {priority_bg_end} 100%); padding: 16px 14px; border-radius: 12px; text-align: center; border: 2px solid {priority_border}; box-shadow: 0 4px 16px rgba(0,0,0,0.08);">
                <div style="font-size: 11px; color: #6b7280; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 8px;">Priority</div>
                <div style="font-size: 16px; color: {priority_color}; font-weight: 900; letter-spacing: -0.5px;">{current_product['priority']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with badge_col3:
            phase_color = get_phase_color(current_product['phase'])
            phase_bg_map = {
                "#3B82F6": "#dbeafe",  # Blue
                "#F59E0B": "#fef3c7",  # Amber
                "#8B5CF6": "#ede9fe"   # Purple
            }
            phase_border_map = {
                "#3B82F6": "#93c5fd",  # Blue
                "#F59E0B": "#fcd34d",  # Amber
                "#8B5CF6": "#c4b5fd"   # Purple
            }
            phase_bg = phase_bg_map.get(phase_color, "#f3f4f6")
            phase_border = phase_border_map.get(phase_color, "#d1d5db")
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {phase_bg} 0%, rgba(255,255,255,0.8) 100%); padding: 16px 14px; border-radius: 12px; text-align: center; border: 2px solid {phase_border}; box-shadow: 0 4px 16px rgba(0,0,0,0.08);">
                <div style="font-size: 11px; color: #6b7280; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 8px;">Phase</div>
                <div style="font-size: 16px; color: {phase_color}; font-weight: 900; letter-spacing: -0.5px;">{current_product['phase']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Enhanced Tabs with styling
        st.markdown("""
        <div style="margin-top: 20px; margin-bottom: 10px;">
            <p style="font-size: 14px; font-weight: 700; color: #1f2937; text-transform: uppercase; letter-spacing: 0.8px; margin: 0 0 12px 0;">Product Details</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Tabs
        tab1, tab2, tab3, tab4 = st.tabs(["📋 Assumptions", "💰 Financials", "🎯 Access", "📅 Timeline"])
        
        with tab1:
            # Market Uptake Assumptions Container
            st.markdown('<div class="uptake-container"><div class="section-title">📈 Market Uptake Assumptions</div></div>', unsafe_allow_html=True)
            
            uptake_data = current_product["assumptions"]["uptake"]
            uptake_df = pd.DataFrame({
                "Year": [f"Y{k.replace('y', '')}" for k in uptake_data.keys()],
                "Uptake %": [f"{v}%" for v in uptake_data.values()]
            })
            
            col1, col2 = st.columns([0.7, 0.3])
            with col1:
                st.dataframe(uptake_df, use_container_width=True, hide_index=True)
            with col2:
                st.markdown(f"""
                <div class="data-card">
                    <div class="data-card-title">Peak Market Share</div>
                    <div class="data-card-value">{current_product['assumptions']['peakShare']}%</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Pricing & GTN Assumptions Container
            st.markdown('<div class="pricing-container"><div class="section-title">💵 Pricing & GTN Assumptions</div></div>', unsafe_allow_html=True)
            
            pricing = current_product["assumptions"]["pricing"]
            col1, col2, col3 = st.columns(3)
            
            with col1:
                wac_formatted = format_currency(pricing['wac'])
                st.markdown(f"""
                <div class="data-card">
                    <div class="data-card-title">WAC (List Price)</div>
                    <div class="data-card-value">${format_number(pricing['wac'], 0)}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="data-card">
                    <div class="data-card-title">ASP (Avg Sales Price)</div>
                    <div class="data-card-value">${format_number(pricing['asp'], 0)}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="data-card">
                    <div class="data-card-title">Gross-to-Net %</div>
                    <div class="data-card-value">{pricing['gtn']}%</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Access & Distribution Container
            st.markdown('<div class="access-container"><div class="section-title">🎯 Access & Distribution</div></div>', unsafe_allow_html=True)
            
            access = current_product["assumptions"]["access"]
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Formulary Coverage")
                
                tier1_pct = access["tier1"]
                tier2_pct = access["tier2"]
                tier3_pct = access["tier3"]
                
                st.markdown(f"""
                <div class="data-card">
                    <div class="data-card-title">🔷 Tier 1 (Preferred): <b>{tier1_pct}%</b></div>
                </div>
                """, unsafe_allow_html=True)
                st.progress(tier1_pct / 100)
                
                st.markdown(f"""
                <div class="data-card">
                    <div class="data-card-title">🔷 Tier 2 (Non-Preferred): <b>{tier2_pct}%</b></div>
                </div>
                """, unsafe_allow_html=True)
                st.progress(tier2_pct / 100)
                
                st.markdown(f"""
                <div class="data-card">
                    <div class="data-card-title">🔷 Tier 3 (Specialty): <b>{tier3_pct}%</b></div>
                </div>
                """, unsafe_allow_html=True)
                st.progress(tier3_pct / 100)
            
            with col2:
                st.markdown("#### Market Details")
                st.info(f"**Competition Level:** {current_product['assumptions']['competition']}")
                st.info(f"**J-Code Status:** {current_product['assumptions']['jcode']}")
                st.info(f"**Distribution:** {current_product['assumptions']['distribution']}")
        
        with tab2:
            st.markdown("### 💰 Financial Metrics")
            
            npv = current_product['npv']
            five_year_revenue = npv * 1.8
            peak_revenue = npv * 0.45
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div class="financial-card">
                    <div class="financial-label">Net Present Value</div>
                    <div class="financial-value">${format_number(npv, 1)}M</div>
                    <div class="financial-subtitle">As of {current_product['lastUpdated']}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="financial-card">
                    <div class="financial-label">5-Year Revenue</div>
                    <div class="financial-value">${format_number(five_year_revenue, 1)}M</div>
                    <div class="financial-subtitle">Projected Total</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="financial-card">
                    <div class="financial-label">Peak Year Revenue</div>
                    <div class="financial-value">${format_number(peak_revenue, 1)}M</div>
                    <div class="financial-subtitle">Year 4-5 Estimate</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            st.markdown("### 💸 Revenue Waterfall (Year 1)")
            
            waterfall_data = {
                "Category": ["Gross Revenue\n(WAC)", "Rebates &\nDiscounts", "Chargebacks", "Admin Fees", "Net Revenue"],
                "Amount": [125.0, -42.5, -8.2, -6.8, 67.5]
            }
            
            waterfall_df = pd.DataFrame(waterfall_data)
            
            fig = go.Figure(go.Waterfall(
                x=waterfall_df["Category"],
                y=waterfall_df["Amount"],
                totals={"marker": {"color": "green"}},
                measure=["relative", "relative", "relative", "relative", "total"],
                text=["$125.0M", "-$42.5M", "-$8.2M", "-$6.8M", "$67.5M"],
                textposition="outside"
            ))
            fig.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            st.markdown("### 🎯 Market Access Strategy")
            st.info(f"Based on **{current_product['archetype']}** archetype - focus on **{current_product['assumptions']['distribution']}** channels")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Target Payers")
                payers = ["UnitedHealthcare", "CVS Caremark", "Humana", "Cigna", "Aetna"]
                for idx, payer in enumerate(payers):
                    priority = "🔴 High Priority" if idx < 2 else "🟡 Medium Priority"
                    st.markdown(f"- **{payer}** {priority}")
            
            with col2:
                st.markdown("#### Key Milestones")
                
                milestones = [
                    ("✅ FDA Approval", "Completed - 2025-Q4"),
                    ("🔵 Payer Negotiations", "In Progress - 2026-Q1"),
                    ("⭕ Commercial Launch", "Planned - 2026-Q2")
                ]
                
                for milestone, status in milestones:
                    st.markdown(f"**{milestone}**  \n*{status}*")
        
        with tab4:
            st.markdown("### 📅 Product Development Timeline")
            
            timeline_data = [
                {"Stage": "FDA Approval", "Date": "2025-Q4", "Status": "Completed", "Duration": "6 months"},
                {"Stage": "Payer Negotiations", "Date": "2026-Q1", "Status": "In Progress", "Duration": "3 months"},
                {"Stage": "Commercial Launch", "Date": "2026-Q2", "Status": "Upcoming", "Duration": "Ongoing"},
                {"Stage": "Formulary Wins", "Date": "2026-Q3", "Status": "Upcoming", "Duration": "6 months"},
                {"Stage": "Market Expansion", "Date": "2026-Q4", "Status": "Upcoming", "Duration": "Ongoing"}
            ]
            
            status_colors = {
                "Completed": "#10b981",      # Green
                "In Progress": "#3b82f6",    # Blue
                "Upcoming": "#f59e0b"        # Amber
            }
            
            status_bg_colors = {
                "Completed": "#d1fae5",      # Light green
                "In Progress": "#dbeafe",    # Light blue
                "Upcoming": "#fef3c7"        # Light amber
            }
            
            # Vertical timeline
            st.markdown("""
            <style>
            .timeline-container {
                position: relative;
                padding: 20px 0;
            }
            .timeline-item {
                display: flex;
                margin-bottom: 30px;
                position: relative;
            }
            .timeline-marker {
                width: 60px;
                height: 60px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 28px;
                font-weight: bold;
                color: white;
                border: 3px solid white;
                box-shadow: 0 0 0 3px;
                flex-shrink: 0;
                margin-right: 30px;
            }
            .timeline-content {
                flex: 1;
                padding: 20px;
                border-radius: 12px;
                background-color: white;
                border: 2px solid #e5e7eb;
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                transition: transform 0.2s, box-shadow 0.2s;
            }
            .timeline-content:hover {
                transform: translateX(5px);
                box-shadow: 0 4px 16px rgba(0,0,0,0.12);
            }
            .timeline-date {
                font-size: 18px;
                font-weight: 700;
                color: #1f2937;
                margin-bottom: 8px;
            }
            .timeline-stage {
                font-size: 16px;
                font-weight: 600;
                color: #374151;
                margin-bottom: 4px;
            }
            .timeline-status {
                font-size: 13px;
                font-weight: 600;
                padding: 4px 12px;
                border-radius: 20px;
                display: inline-block;
                margin-top: 8px;
            }
            .timeline-duration {
                font-size: 12px;
                color: #6b7280;
                margin-top: 6px;
                font-style: italic;
            }
            .timeline-vertical-line {
                position: absolute;
                left: 29px;
                top: 60px;
                width: 2px;
                height: calc(100% + 30px);
                background: #e5e7eb;
            }
            .timeline-item:last-child .timeline-vertical-line {
                display: none;
            }
            </style>
            """, unsafe_allow_html=True)
            
            st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
            
            for idx, task in enumerate(timeline_data):
                status = task["Status"]
                color = status_colors.get(status, "#9ca3af")
                bg_color = status_bg_colors.get(status, "#f3f4f6")
                status_icon = "✅" if status == "Completed" else "🔵" if status == "In Progress" else "⭕"
                
                timeline_html = f"""
                <div class="timeline-item">
                    <div class="timeline-vertical-line"></div>
                    <div class="timeline-marker" style="background-color: {color}; box-shadow: 0 0 0 3px {color}, 0 0 0 6px white;">
                        {status_icon}
                    </div>
                    <div class="timeline-content">
                        <div class="timeline-date">{task['Date']}</div>
                        <div class="timeline-stage">{task['Stage']}</div>
                        <div class="timeline-duration">Duration: {task['Duration']}</div>
                        <span class="timeline-status" style="background-color: {bg_color}; color: {color};">
                            {status}
                        </span>
                    </div>
                </div>
                """
                st.markdown(timeline_html, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("---")
            st.markdown("### 🎯 Key Activities by Stage")
            
            activities = {
                "FDA Approval": ["Complete clinical data package", "Respond to FDA questions", "Finalize labeling"],
                "Payer Negotiations": ["Submit dossier to major payers", "Prepare health economic data", "Conduct P&T committee meetings"],
                "Commercial Launch": ["Initiate marketing campaigns", "Activate sales force", "Establish distribution network"],
                "Formulary Wins": ["Secure preferred tier placement", "Negotiate rebates", "Launch field teams"],
                "Market Expansion": ["Expand to secondary indications", "Build market share", "Monitor competition"]
            }
            
            for stage, activity_list in activities.items():
                with st.expander(f"📋 {stage}"):
                    for activity in activity_list:
                        st.markdown(f"• {activity}")
        
        st.markdown("---")
        
        # Version History
        if show_version_history:
            st.markdown("### 📜 Version History & Audit Trail")
            
            for idx, version in enumerate(VERSION_HISTORY):
                with st.expander(f"{version['version']} - {version['status']}", expanded=(idx == 0)):
                    col1, col2 = st.columns([0.7, 0.3])
                    
                    with col1:
                        st.markdown("**Changes:**")
                        for change in version["changes"]:
                            st.markdown(f"• {change}")
                    
                    with col2:
                        st.markdown(f"**User:** {version['user']}")
                        st.markdown(f"**Date:** {version['date']}")
                        impact_color = "🟢" if version["npvImpact"] > 0 else "🔴" if version["npvImpact"] < 0 else "⚪"
                        st.markdown(f"**NPV Impact:** {impact_color} {version['npvImpact']:+.1f}M")
        
        # Scenario Comparison
        if show_scenario:
            st.markdown("### 🔀 Scenario Comparison")
            
            scenario_data = {
                "Metric": ["NPV", "Peak Share", "GTN %"],
                "Base Case": [
                    f"${current_product['npv']}M",
                    f"{current_product['assumptions']['peakShare']}%",
                    f"{current_product['assumptions']['pricing']['gtn']}%"
                ],
                "Optimistic": [
                    f"${current_product['npv'] * 1.25:.1f}M",
                    f"{current_product['assumptions']['peakShare'] + 8}%",
                    f"{current_product['assumptions']['pricing']['gtn'] - 5}%"
                ],
                "Conservative": [
                    f"${current_product['npv'] * 0.75:.1f}M",
                    f"{current_product['assumptions']['peakShare'] - 8}%",
                    f"{current_product['assumptions']['pricing']['gtn'] + 5}%"
                ]
            }
            
            scenario_df = pd.DataFrame(scenario_data)
            st.dataframe(scenario_df, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Footer
        col1, col2 = st.columns([0.7, 0.3])
        with col1:
            st.markdown(f"**Last updated by:** {current_product['updatedBy']}  \n**Date:** {current_product['lastUpdated']}")
        with col2:
            st.markdown("🟢 **Status:** Single Source of Truth | Version Control Enabled")
        
        # Back to portfolio button
        if st.button("⬅️ Back to Portfolio View", use_container_width=True):
            st.session_state.view_mode = "portfolio"
            st.rerun()
