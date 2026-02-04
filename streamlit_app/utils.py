"""
Utility functions for Sandoz Pipeline Application
"""

import pandas as pd
from config import (
    PIPELINE_PRODUCTS, ARCHETYPES, PRIORITY_COLORS, 
    PHASE_COLORS, FINANCIAL_FACTORS
)

def get_priority_color(priority):
    """Get color for priority level"""
    return PRIORITY_COLORS.get(priority, "#95A5A6")

def get_archetype_color(archetype):
    """Get color for archetype"""
    for arch in ARCHETYPES:
        if arch["name"] == archetype:
            return arch["color"]
    return "#95A5A6"

def get_phase_color(phase):
    """Get color for development phase"""
    return PHASE_COLORS.get(phase, "#6B7280")

def get_product_by_id(product_id):
    """Get product data by ID"""
    for product in PIPELINE_PRODUCTS:
        if product["id"] == product_id:
            return product
    return None

def get_all_products():
    """Get all products"""
    return PIPELINE_PRODUCTS

def calculate_portfolio_metrics():
    """Calculate portfolio-level metrics"""
    products = get_all_products()
    
    metrics = {
        "total_npv": sum(p["npv"] for p in products),
        "total_products": len(products),
        "high_priority_count": len([p for p in products if p["priority"] in ["High", "Strategic"]]),
        "launches_this_year": 3,
        "average_npv": sum(p["npv"] for p in products) / len(products) if products else 0
    }
    
    return metrics

def calculate_financial_metrics(product):
    """Calculate financial metrics for a product"""
    npv = product["npv"]
    
    metrics = {
        "npv": npv,
        "five_year_revenue": npv * FINANCIAL_FACTORS["five_year_multiplier"],
        "peak_year_revenue": npv * FINANCIAL_FACTORS["peak_year_multiplier"],
        "optimistic_npv": npv * FINANCIAL_FACTORS["optimistic_npv_multiplier"],
        "conservative_npv": npv * FINANCIAL_FACTORS["conservative_npv_multiplier"]
    }
    
    return metrics

def create_portfolio_dataframe():
    """Create DataFrame for portfolio table"""
    products = get_all_products()
    
    df_data = []
    for product in products:
        df_data.append({
            "Product": product["name"],
            "ID": product["id"],
            "Archetype": product["archetype"],
            "Phase": product["phase"],
            "Launch Date": product["launchDate"],
            "Priority": product["priority"],
            "NPV ($M)": f"${product['npv']:.1f}",
            "Last Updated": product["lastUpdated"],
            "Updated By": product["updatedBy"]
        })
    
    return pd.DataFrame(df_data)

def create_uptake_dataframe(uptake_dict):
    """Create DataFrame for uptake data"""
    data = []
    for key, value in uptake_dict.items():
        year_num = key.replace('y', '')
        data.append({
            "Year": f"Y{year_num}",
            "Uptake %": value
        })
    
    return pd.DataFrame(data)

def create_scenario_comparison_dataframe(product):
    """Create DataFrame for scenario comparison"""
    assumptions = product["assumptions"]
    pricing = assumptions["pricing"]
    peak_share = assumptions["peakShare"]
    gtn_pct = pricing["gtn"]
    
    data = {
        "Metric": ["NPV", "Peak Share", "GTN %"],
        "Base Case": [
            f"${product['npv']}M",
            f"{peak_share}%",
            f"{gtn_pct}%"
        ],
        "Optimistic": [
            f"${product['npv'] * 1.25:.1f}M",
            f"{peak_share + 8}%",
            f"{gtn_pct - 5}%"
        ],
        "Conservative": [
            f"${product['npv'] * 0.75:.1f}M",
            f"{peak_share - 8}%",
            f"{gtn_pct + 5}%"
        ]
    }
    
    return pd.DataFrame(data)

def format_currency(value, decimals=1):
    """Format value as currency"""
    return f"${value:,.{decimals}f}M"

def format_percentage(value):
    """Format value as percentage"""
    return f"{value}%"

def get_products_by_priority(priority):
    """Get all products with specific priority"""
    return [p for p in get_all_products() if p["priority"] == priority]

def get_products_by_phase(phase):
    """Get all products with specific phase"""
    return [p for p in get_all_products() if p["phase"] == phase]

def get_products_by_archetype(archetype):
    """Get all products with specific archetype"""
    return [p for p in get_all_products() if p["archetype"] == archetype]

def get_high_priority_products():
    """Get all high and strategic priority products"""
    return [p for p in get_all_products() if p["priority"] in ["High", "Strategic"]]

def calculate_archetype_distribution():
    """Calculate product distribution by archetype"""
    distribution = {}
    
    for archetype in ARCHETYPES:
        name = archetype["name"]
        count = len(get_products_by_archetype(name))
        distribution[name] = {
            "count": count,
            "color": archetype["color"],
            "percentage": (count / len(get_all_products()) * 100) if get_all_products() else 0
        }
    
    return distribution

def create_waterfall_data():
    """Create waterfall chart data"""
    return {
        "categories": ["Gross Revenue\n(WAC)", "Rebates &\nDiscounts", "Chargebacks", "Admin Fees", "Net Revenue"],
        "values": [125.0, -42.5, -8.2, -6.8, 67.5],
        "measures": ["relative", "relative", "relative", "relative", "total"]
    }

def get_product_timeline(product):
    """Get timeline for specific product"""
    return [
        {"Stage": "FDA Approval", "Date": "2025-Q4", "Status": "Completed"},
        {"Stage": "Payer Negotiations", "Date": "2026-Q1", "Status": "In Progress"},
        {"Stage": "Commercial Launch", "Date": product["launchDate"], "Status": "Upcoming"},
        {"Stage": "Formulary Wins", "Date": "2026-Q3", "Status": "Upcoming"},
        {"Stage": "Market Expansion", "Date": "2026-Q4", "Status": "Upcoming"}
    ]

def validate_product_data(product):
    """Validate product data structure"""
    required_fields = [
        "id", "name", "archetype", "phase", "launchDate",
        "territory", "priority", "npv", "assumptions",
        "lastUpdated", "updatedBy"
    ]
    
    for field in required_fields:
        if field not in product:
            return False, f"Missing field: {field}"
    
    return True, "Valid"

def get_summary_statistics():
    """Get summary statistics for portfolio"""
    products = get_all_products()
    npvs = [p["npv"] for p in products]
    
    stats = {
        "total_products": len(products),
        "total_npv": sum(npvs),
        "average_npv": sum(npvs) / len(npvs) if npvs else 0,
        "max_npv": max(npvs) if npvs else 0,
        "min_npv": min(npvs) if npvs else 0,
        "high_priority": len([p for p in products if p["priority"] in ["High", "Strategic"]]),
        "by_phase": {
            "Pre-Launch": len([p for p in products if p["phase"] == "Pre-Launch"]),
            "Filed": len([p for p in products if p["phase"] == "Filed"]),
            "Phase 3": len([p for p in products if p["phase"] == "Phase 3"])
        }
    }
    
    return stats
