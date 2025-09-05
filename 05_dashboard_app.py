import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv(r"C:\Users\ASUS\Desktop\FINAL PROJECT FOR PLACEMENT\Retail_EDA_project\data\retail_sales_featured.csv")
df['order_date'] = pd.to_datetime(df['order_date'])

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("🛍️ Retail Sales Dashboard")

# KPIs
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${df['total_sales'].sum():,.0f}")
col2.metric("Avg Order Value", f"${df['total_sales'].mean():.2f}")
repeat_rate = df.groupby('customer_id')['order_date'].count().gt(1).mean()*100
col3.metric("Repeat Purchase Rate", f"{repeat_rate:.1f}%")

# Revenue Trend
st.subheader("Revenue Trend")
rev_trend = df.groupby('order_date')['total_sales'].sum().reset_index()
fig = px.line(rev_trend, x="order_date", y="total_sales", title="Daily Revenue Trend", markers=True)
st.plotly_chart(fig, use_container_width=True)

# Category Sales
st.subheader("Category-wise Sales")
cat_sales = df.groupby('category_name')['total_sales'].sum().reset_index()
fig2 = px.bar(cat_sales, x="category_name", y="total_sales", title="Category-wise Sales", color="category_name")
st.plotly_chart(fig2, use_container_width=True)

# Payment Method
st.subheader("Payment Method Share")
payment_sales = df.groupby('payment_method')['total_sales'].sum().reset_index()
fig3 = px.pie(payment_sales, names="payment_method", values="total_sales", title="Payment Method Share")
st.plotly_chart(fig3, use_container_width=True)

# Age Distribution
st.subheader("Customer Age Distribution")
fig4 = px.histogram(df, x="age", nbins=20, color="gender", title="Customer Age Distribution")
st.plotly_chart(fig4, use_container_width=True)

# Review Scores
st.subheader("Review Score by Category")
fig5 = px.box(df, x="category_name", y="review_score", color="category_name", title="Review Score by Category")
st.plotly_chart(fig5, use_container_width=True)

