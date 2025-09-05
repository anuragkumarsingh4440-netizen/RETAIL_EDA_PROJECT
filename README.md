# Retail Sales Data Analysis (EDA)

## Project Overview
This project performs **Exploratory Data Analysis (EDA)** on a synthetic retail sales dataset.  
It uncovers sales trends, customer demographics, product performance, and payment preferences.  
The analysis is presented with **visualizations, insights, and business recommendations**.

## Dataset Description
File: `retail_sales.csv`  
Columns:
- `customer_id` → Unique customer identifier
- `order_date` → Date of purchase
- `product_id` → Unique product identifier
- `category_id` → Product category ID
- `category_name` → Product category name (Electronics, Fashion, etc.)
- `product_name` → Name of the purchased product
- `quantity` → Number of items bought
- `price` → Price per unit
- `payment_method` → Payment type (Credit Card, COD, etc.)
- `city` → Customer city
- `review_score` → Customer review rating (1–5)
- `gender` → Customer gender
- `age` → Customer age

## Sample Data
| customer_id | order_date | product_id | category_name       | product_name | quantity | price  | payment_method | city           | review_score | gender | age |
|-------------|------------|------------|---------------------|--------------|----------|--------|----------------|----------------|--------------|--------|-----|
| 13542       | 17-12-2024 | 784        | Electronics         | Smartphone   | 2        | 373.36 | Credit Card    | New Oliviaberg | 1            | F      | 56  |
| 23188       | 01-06-2024 | 682        | Sports & Outdoors   | Soccer Ball  | 5        | 299.34 | Credit Card    | Port Matthew   |              | M      | 59  |
| 55098       | 04-02-2025 | 684        | Sports & Outdoors   | Tent         | 5        | 23.00  | Credit Card    | West Sarah     | 5            | F      | 64  |
| 65208       | 28-10-2024 | 204        | Books & Stationery  | Story Book   | 2        | 230.11 | Bank Transfer  | Hernandezburgh | 5            | M      | 34  |

##  Steps in Analysis
1. **Data Understanding** – structure, missing values, datatypes
2. **Data Cleaning** – fixing dates, handling nulls, removing duplicates
3. **Exploratory Data Analysis** – univariate, bivariate, multivariate
4. **Visualization** – Matplotlib + Seaborn charts
5. **Business Insights** – clear, actionable recommendations

## 📈 Key Insights
- Electronics is the **highest revenue generator** 
- Majority of customers pay via **Credit Card** 
- Young adults (20–35) contribute most purchases
- Some products with low ratings need **quality improvement** 

##  Tech Stack
- Python  
- Pandas & NumPy  
- Matplotlib & Seaborn  

##  Project Structure
```
├── data
│   └── retail_sales.csv
├── notebooks
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   └── 04_dashboard.ipynb
├── Retail_EDA_Report_AnuragKumarSingh.pdf
├── README.md
```

##  Author
**Anurag Kumar Singh**  
Aspiring Data Analyst | SQL • Python • EDA • Visualization  

---
🔗 Feel free to use this project for learning or portfolio purposes.
