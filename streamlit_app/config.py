"""
Configuration and constants for Sandoz Pipeline Application
"""

# Product Data
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

# Archetype Configuration
ARCHETYPES = [
    {"name": "Med Benefit High", "color": "#0066CC", "count": 8},
    {"name": "Med Benefit Med", "color": "#4A90E2", "count": 6},
    {"name": "Med Benefit Low", "color": "#7AB8FF", "count": 4},
    {"name": "Rx Benefit High", "color": "#00A86B", "count": 7},
    {"name": "Rx Benefit Med", "color": "#52C993", "count": 5},
    {"name": "Rx Benefit Low", "color": "#8FE5B8", "count": 3},
    {"name": "Rare Disease", "color": "#9B59B6", "count": 2}
]

# Version History
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

# Color Schemes
PRIORITY_COLORS = {
    "High": "#E74C3C",
    "Strategic": "#9B59B6",
    "Medium": "#F39C12",
    "Low": "#95A5A6"
}

PHASE_COLORS = {
    "Pre-Launch": "#3B82F6",
    "Filed": "#F59E0B",
    "Phase 3": "#8B5CF6"
}

# Timeline Data
TIMELINE_DATA = [
    {"Stage": "FDA Approval", "Date": "2025-Q4", "Status": "Completed"},
    {"Stage": "Payer Negotiations", "Date": "2026-Q1", "Status": "In Progress"},
    {"Stage": "Commercial Launch", "Date": "2026-Q2", "Status": "Upcoming"},
    {"Stage": "Formulary Wins", "Date": "2026-Q3", "Status": "Upcoming"},
    {"Stage": "Market Expansion", "Date": "2026-Q4", "Status": "Upcoming"}
]

# App Configuration
APP_CONFIG = {
    "title": "Pipeline Decision System",
    "subtitle": "Centralized Portfolio Management & NPV Tracking",
    "company": "SANDOZ",
    "version": "1.0.0",
    "last_updated": "2026-02-04"
}

# Financial Calculation Factors
FINANCIAL_FACTORS = {
    "five_year_multiplier": 1.8,
    "peak_year_multiplier": 0.45,
    "optimistic_npv_multiplier": 1.25,
    "conservative_npv_multiplier": 0.75
}

# Payers List
TARGET_PAYERS = [
    ("UnitedHealthcare", "high"),
    ("CVS Caremark", "high"),
    ("Humana", "medium"),
    ("Cigna", "medium"),
    ("Aetna", "medium")
]

# Milestones
MILESTONES = [
    ("FDA Approval", "Completed - 2025-Q4"),
    ("Payer Negotiations", "In Progress - 2026-Q1"),
    ("Commercial Launch", "Planned - 2026-Q2")
]

# Revenue Waterfall Components
REVENUE_WATERFALL = [
    {"Category": "Gross Revenue\n(WAC)", "Amount": 125.0, "Type": "relative"},
    {"Category": "Rebates &\nDiscounts", "Amount": -42.5, "Type": "relative"},
    {"Category": "Chargebacks", "Amount": -8.2, "Type": "relative"},
    {"Category": "Admin Fees", "Amount": -6.8, "Type": "relative"},
    {"Category": "Net Revenue", "Amount": 67.5, "Type": "total"}
]
