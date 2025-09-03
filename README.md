# Sales Analytics Dashboard

## 📊 Project Overview
An interactive sales analytics dashboard built with Streamlit and Plotly, providing comprehensive insights into sales performance, regional analysis, and time-based trends. Features advanced filtering, multiple visualization types, and business intelligence capabilities.

## ✨ Key Features

### 🎯 Interactive Analytics
- **Multi-dimensional filtering** by region, category, and date range
- **Real-time KPI metrics** with dynamic calculations
- **4 comprehensive analysis tabs** covering different business perspectives
- **Responsive design** with mobile-friendly interface

### 📈 Advanced Visualizations
- **Sales vs Profit scatter plots** with profit margin sizing
- **Combined time-series analysis** with dual-axis charts
- **Geographic performance comparisons** across regions
- **Category-wise profit distribution** with pie charts and bar graphs

### 🔍 Business Intelligence
- **Performance metrics calculation** (profit margins, growth rates, AOV)
- **Top performer identification** with ranking tables
- **Trend analysis** with month-over-month growth calculations
- **Cross-dimensional analysis** (Category × Region performance matrix)

## 🛠️ Technical Stack
- **Frontend**: Streamlit for interactive web application
- **Visualization**: Plotly Express & Graph Objects for advanced charts
- **Data Processing**: Pandas for data manipulation and analysis
- **Deployment**: Streamlit Cloud ready with caching optimization

## 📁 Project Structure
```
sales_insights_dashboard/
├── app.py                 # Enhanced dashboard application
├── sales_data.csv        # Sample sales dataset
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Git ignore file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
1. **Clone the repository**
   ```bash
   git clone [your-repository-url]
   cd sales_insights_dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the dashboard**
   - Open your web browser to `http://localhost:8501`
   - Use the sidebar filters to explore different data views

## 📊 Dashboard Sections

### 🏠 Main Dashboard
- **KPI Overview**: Total sales, profit, margins, orders, and average order value
- **Dynamic filtering**: Multi-select filters with date range picker
- **Data validation**: Error handling and empty state management

### 📈 Sales Analysis Tab
- **Category Performance**: Bar charts showing sales by category
- **Profit Distribution**: Pie chart visualization of profit allocation
- **Sales vs Profit Analysis**: Scatter plot with profit margin indicators
- **Correlation insights**: Interactive hover data with order details

### 🎯 Performance Metrics Tab
- **Regional Profit Margins**: Comparative analysis across regions
- **Top Performers**: Ranking table of highest-profit orders
- **Performance Matrix**: Category × Region cross-analysis
- **Summary Statistics**: Aggregated metrics with calculated fields

### 🗺️ Regional Insights Tab
- **Geographic Comparison**: Sales performance by region
- **Order Volume Analysis**: Orders vs average order value scatter plot
- **Regional Metrics Table**: Formatted performance indicators
- **Market penetration insights**: Regional market analysis

### 📅 Time Analysis Tab
- **Trend Visualization**: Monthly sales and profit trend lines
- **Combined Analysis**: Dual-axis charts for sales/profit correlation
- **Growth Calculations**: Month-over-month growth rate metrics
- **Seasonal Patterns**: Time-based performance insights

## 📈 Key Metrics & Calculations

### Business Metrics
- **Total Sales**: Sum of all sales transactions
- **Total Profit**: Sum of all profit values
- **Average Profit Margin**: (Profit / Sales) × 100
- **Average Order Value**: Total Sales / Number of Orders
- **Month-over-Month Growth**: ((Current - Previous) / Previous) × 100

### Data Enhancements
- **Calculated Fields**: Profit margin, days since order, time periods
- **Data Validation**: Missing value handling, data type conversions
- **Performance Optimization**: Streamlit caching for faster loading

## 🎨 Visualization Features

### Chart Types
- **Bar Charts**: Category and regional comparisons
- **Line Charts**: Time-series trend analysis
- **Scatter Plots**: Correlation analysis with size encoding
- **Pie Charts**: Distribution and composition analysis
- **Dual-Axis Charts**: Multiple metric comparisons

### Interactive Elements
- **Hover Details**: Comprehensive data on mouse-over
- **Color Encoding**: Data-driven color scales
- **Size Encoding**: Profit margin representation in scatter plots
- **Responsive Design**: Automatic layout adjustment

## 🔧 Technical Highlights

### Data Processing
- **Pandas Integration**: Efficient data manipulation and aggregation
- **Date Handling**: Automatic date parsing and period extraction
- **Dynamic Filtering**: Real-time data subset calculations
- **Memory Optimization**: Cached data loading for performance

### Error Handling
- **File Validation**: Missing file detection and user feedback
- **Empty Data States**: Graceful handling of filtered empty datasets
- **Exception Handling**: Comprehensive error catching and display

### Code Quality
- **Modular Functions**: Reusable data processing functions
- **Documentation**: Inline comments and docstrings
- **Clean Architecture**: Logical separation of concerns
- **Performance Optimization**: Streamlit caching implementation

## 📊 Sample Data Structure
```csv
Order ID,Region,Category,Sales,Profit,Order Date
1001,East,Technology,200,60,2023-01-01
1002,West,Furniture,450,120,2023-01-16
1003,South,Office Supplies,300,75,2023-01-31
```

## 🎯 Business Use Cases
- **Sales Performance Monitoring**: Track KPIs and identify trends
- **Regional Strategy Planning**: Compare market performance across regions
- **Product Category Analysis**: Optimize product mix based on profitability
- **Financial Reporting**: Generate insights for stakeholder presentations

## 🚀 Future Enhancements
- **Predictive Analytics**: Sales forecasting capabilities
- **Customer Segmentation**: Advanced customer analysis features
- **Export Functionality**: PDF and Excel report generation
- **Advanced Filtering**: Custom date ranges and metric thresholds

## 👨‍💻 Author
**Osvaldo Ruiz**
- LinkedIn: [linkedin.com/in/OsvaldoRuiz](https://linkedin.com/in/OsvaldoRuiz)
- GitHub: [github.com/ruizOsvaldo](https://github.com/ruizOsvaldo)
- Portfolio: [ruizosvaldo.github.io](https://ruizosvaldo.github.io)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Built with ❤️ using Streamlit and Plotly for interactive data visualization and business intelligence.*
