
import pandas as pd
import plotly.express as px
import streamlit as st

# Load dataset
df = pd.read_csv("sales_data.csv")

# Sidebar filters
st.sidebar.header("Filter Options")
region = st.sidebar.multiselect("Select Region(s):", df["Region"].unique(), default=df["Region"].unique())
df_filtered = df[df["Region"].isin(region)]

# Dashboard title
st.title("Sales Insights Dashboard")

# KPIs
total_sales = df_filtered["Sales"].sum()
total_profit = df_filtered["Profit"].sum()

st.metric("Total Sales", f"${total_sales:,.0f}")
st.metric("Total Profit", f"${total_profit:,.0f}")

# Sales by Category
fig_category = px.bar(df_filtered.groupby("Category")["Sales"].sum().reset_index(),
                      x="Category", y="Sales", title="Sales by Category")
st.plotly_chart(fig_category)

# Monthly trend
df_filtered["Order Date"] = pd.to_datetime(df_filtered["Order Date"])
df_filtered["Month"] = df_filtered["Order Date"].dt.to_period("M").astype(str)
fig_monthly = px.line(df_filtered.groupby("Month")["Sales"].sum().reset_index(),
                      x="Month", y="Sales", title="Monthly Sales Trend")
st.plotly_chart(fig_monthly)
