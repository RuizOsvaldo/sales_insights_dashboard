import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load and prepare data
@st.cache_data
def load_data():
    """Load and preprocess sales data"""
    try:
        df = pd.read_csv("sales_data.csv")
        
        # Data validation
        if df.empty:
            st.error("Dataset is empty")
            return None
        
        # Check for required columns
        required_columns = ["Order Date", "Region", "Category", "Sales", "Profit"]
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            st.error(f"Missing required columns: {missing_columns}")
            return None
            
        # Date processing with error handling
        try:
            df["Order Date"] = pd.to_datetime(df["Order Date"])
            df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
            df["Quarter"] = df["Order Date"].dt.to_period("Q").astype(str)
            df["Year"] = df["Order Date"].dt.year
        except Exception as e:
            st.error(f"Error processing dates: {str(e)}")
            return None
        
        # Calculated metrics with error handling
        try:
            df["Profit Margin"] = (df["Profit"] / df["Sales"] * 100).fillna(0).round(2)
            df["Days_Since_Order"] = (datetime.now() - df["Order Date"]).dt.days
        except Exception as e:
            st.warning(f"Error calculating derived metrics: {str(e)}")
            # Continue without derived metrics
        
        return df
        
    except FileNotFoundError:
        st.error("sales_data.csv file not found. Please ensure the file is in the project directory.")
        return None
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

# Load data
df = load_data()
if df is None:
    st.stop()

# Sidebar configuration
st.sidebar.header("📊 Dashboard Controls")
st.sidebar.markdown("---")

# Filters
st.sidebar.subheader("🔍 Filters")
regions = st.sidebar.multiselect(
    "Select Region(s):",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

categories = st.sidebar.multiselect(
    "Select Category(s):",
    options=df["Category"].unique(), 
    default=df["Category"].unique()
)

# Date range filter
min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()
date_range = st.sidebar.date_input(
    "Select Date Range:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Apply filters
if len(date_range) == 2:
    start_date, end_date = date_range
    df_filtered = df[
        (df["Region"].isin(regions)) & 
        (df["Category"].isin(categories)) &
        (df["Order Date"].dt.date >= start_date) &
        (df["Order Date"].dt.date <= end_date)
    ]
else:
    df_filtered = df[
        (df["Region"].isin(regions)) & 
        (df["Category"].isin(categories))
    ]

# Main dashboard
st.title("📊 Sales Analytics Dashboard")
st.markdown("---")

# Check if filtered data is empty
if df_filtered.empty:
    st.warning("No data matches the selected filters. Please adjust your selection.")
    st.stop()

# Key Performance Indicators (KPIs)
st.subheader("🎯 Key Performance Indicators")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    total_sales = df_filtered["Sales"].sum()
    st.metric("Total Sales", f"${total_sales:,.0f}")

with col2:
    total_profit = df_filtered["Profit"].sum()
    profit_change = total_profit - df["Profit"].sum() + total_profit  # Simple change calculation
    st.metric("Total Profit", f"${total_profit:,.0f}")

with col3:
    avg_profit_margin = df_filtered["Profit Margin"].mean()
    st.metric("Avg Profit Margin", f"{avg_profit_margin:.1f}%")

with col4:
    total_orders = len(df_filtered)
    st.metric("Total Orders", f"{total_orders:,}")

with col5:
    avg_order_value = df_filtered["Sales"].mean()
    st.metric("Avg Order Value", f"${avg_order_value:.2f}")

st.markdown("---")

# Dashboard tabs
tab1, tab2, tab3, tab4 = st.tabs(["📈 Sales Analysis", "🎯 Performance Metrics", "🗺️ Regional Insights", "📅 Time Analysis"])

with tab1:
    st.subheader("Sales Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Sales by Category
        category_sales = df_filtered.groupby("Category")["Sales"].sum().reset_index()
        fig_category = px.bar(
            category_sales,
            x="Category", 
            y="Sales",
            title="Sales by Category",
            color="Sales",
            color_continuous_scale="blues"
        )
        fig_category.update_layout(showlegend=False)
        st.plotly_chart(fig_category, use_container_width=True)
    
    with col2:
        # Profit by Category
        category_profit = df_filtered.groupby("Category")["Profit"].sum().reset_index()
        fig_profit = px.pie(
            category_profit,
            values="Profit",
            names="Category", 
            title="Profit Distribution by Category"
        )
        st.plotly_chart(fig_profit, use_container_width=True)
    
    # Sales vs Profit Scatter Plot
    st.subheader("Sales vs Profit Analysis")
    fig_scatter = px.scatter(
        df_filtered,
        x="Sales",
        y="Profit", 
        color="Category",
        size="Profit Margin",
        hover_data=["Region", "Order Date"],
        title="Sales vs Profit by Category (Size = Profit Margin)"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with tab2:
    st.subheader("Performance Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Profit Margin by Region
        margin_by_region = df_filtered.groupby("Region")["Profit Margin"].mean().reset_index()
        fig_margin = px.bar(
            margin_by_region,
            x="Region",
            y="Profit Margin",
            title="Average Profit Margin by Region",
            color="Profit Margin",
            color_continuous_scale="greens"
        )
        st.plotly_chart(fig_margin, use_container_width=True)
    
    with col2:
        # Top Performing Orders
        st.subheader("Top 10 Orders by Profit")
        top_orders = df_filtered.nlargest(10, "Profit")[["Order ID", "Region", "Category", "Sales", "Profit", "Profit Margin"]]
        st.dataframe(top_orders, use_container_width=True)
    
    # Performance summary table
    st.subheader("Performance Summary by Category & Region")
    summary = df_filtered.groupby(["Category", "Region"]).agg({
        "Sales": ["sum", "mean"],
        "Profit": ["sum", "mean"], 
        "Profit Margin": "mean",
        "Order ID": "count"
    }).round(2)
    
    # Flatten column names
    summary.columns = ["Total Sales", "Avg Sales", "Total Profit", "Avg Profit", "Avg Margin %", "Order Count"]
    summary = summary.reset_index()
    st.dataframe(summary, use_container_width=True)

with tab3:
    st.subheader("Regional Insights")
    
    # Regional comparison
    regional_data = df_filtered.groupby("Region").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Order ID": "count"
    }).reset_index()
    regional_data["Avg Order Value"] = regional_data["Sales"] / regional_data["Order ID"]
    regional_data.rename(columns={"Order ID": "Total Orders"}, inplace=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Regional Sales Comparison
        fig_regional_sales = px.bar(
            regional_data,
            x="Region",
            y="Sales", 
            title="Total Sales by Region",
            color="Sales",
            color_continuous_scale="viridis"
        )
        st.plotly_chart(fig_regional_sales, use_container_width=True)
    
    with col2:
        # Regional Orders vs Average Order Value
        fig_orders_value = px.scatter(
            regional_data,
            x="Total Orders",
            y="Avg Order Value",
            size="Sales",
            color="Region",
            title="Orders vs Average Order Value by Region"
        )
        st.plotly_chart(fig_orders_value, use_container_width=True)
    
    # Regional performance table
    st.subheader("Regional Performance Metrics")
    regional_display = regional_data.copy()
    regional_display["Sales"] = regional_display["Sales"].apply(lambda x: f"${x:,.0f}")
    regional_display["Profit"] = regional_display["Profit"].apply(lambda x: f"${x:,.0f}")
    regional_display["Avg Order Value"] = regional_display["Avg Order Value"].apply(lambda x: f"${x:.2f}")
    st.dataframe(regional_display, use_container_width=True)

with tab4:
    st.subheader("Time-Based Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Monthly Sales Trend
        monthly_data = df_filtered.groupby("Month")["Sales"].sum().reset_index()
        fig_monthly = px.line(
            monthly_data,
            x="Month",
            y="Sales",
            title="Monthly Sales Trend",
            markers=True
        )
        fig_monthly.update_xaxis(title="Month")
        fig_monthly.update_yaxis(title="Sales ($)")
        st.plotly_chart(fig_monthly, use_container_width=True)
    
    with col2:
        # Monthly Profit Trend  
        monthly_profit = df_filtered.groupby("Month")["Profit"].sum().reset_index()
        fig_monthly_profit = px.line(
            monthly_profit,
            x="Month", 
            y="Profit",
            title="Monthly Profit Trend",
            markers=True,
            line_shape="spline"
        )
        fig_monthly_profit.update_traces(line_color="green")
        st.plotly_chart(fig_monthly_profit, use_container_width=True)
    
    # Combined Sales & Profit Trend
    st.subheader("Combined Sales & Profit Trends")
    
    fig_combined = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Add Sales trace
    fig_combined.add_trace(
        go.Scatter(x=monthly_data["Month"], y=monthly_data["Sales"], name="Sales", line=dict(color="blue")),
        secondary_y=False,
    )
    
    # Add Profit trace
    fig_combined.add_trace(
        go.Scatter(x=monthly_profit["Month"], y=monthly_profit["Profit"], name="Profit", line=dict(color="green")),
        secondary_y=True,
    )
    
    fig_combined.update_xaxes(title_text="Month")
    fig_combined.update_yaxes(title_text="Sales ($)", secondary_y=False)
    fig_combined.update_yaxes(title_text="Profit ($)", secondary_y=True)
    fig_combined.update_layout(title_text="Monthly Sales & Profit Trends")
    
    st.plotly_chart(fig_combined, use_container_width=True)
    
    # Time-based insights
    st.subheader("Time-Based Insights")
    
    # Calculate growth rates
    if len(monthly_data) > 1:
        latest_sales = monthly_data["Sales"].iloc[-1]
        previous_sales = monthly_data["Sales"].iloc[-2] if len(monthly_data) > 1 else latest_sales
        growth_rate = ((latest_sales - previous_sales) / previous_sales * 100) if previous_sales != 0 else 0
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Latest Month Sales", f"${latest_sales:,.0f}")
        with col2:
            st.metric("Previous Month Sales", f"${previous_sales:,.0f}")  
        with col3:
            st.metric("Month-over-Month Growth", f"{growth_rate:.1f}%")

# Footer with data info
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.info(f"📅 Data Range: {df['Order Date'].min().strftime('%Y-%m-%d')} to {df['Order Date'].max().strftime('%Y-%m-%d')}")
with col2:
    st.info(f"📊 Total Records: {len(df):,}")
with col3:
    st.info(f"🔍 Filtered Records: {len(df_filtered):,}")

# Sidebar footer
st.sidebar.markdown("---")
st.sidebar.markdown("**Sales Analytics Dashboard**")
st.sidebar.markdown("Built with Streamlit & Plotly")
st.sidebar.markdown("Data-driven insights for business growth")
