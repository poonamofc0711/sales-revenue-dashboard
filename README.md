# Sales & Revenue Performance Dashboard

## Project Overview
This project enables quick tracking of sales trends and performance for startups and SMBs, replacing slow manual reviews. Using Power BI for interactive visuals and Excel/CSV for data import, the dashboard monitors KPIs like Monthly Revenue, Sales Growth, Top Customers, and Region Performance. It includes trend analysis (e.g., revenue over time) and YoY comparisons for deeper insights.

Data is sourced from CSV files. For demo, sample data is generated with Python (pandas/numpy).

## Tools
- Power BI: Interactive dashboard and filters.
- Excel/CSV: Data import and transformation.
- Python: Sample data generation.

## KPIs and Formulas
- **Monthly Revenue**: Total revenue per month. Formula: `SUM(Revenue)` grouped by Month.
- **Sales Growth**: Month-over-month percentage growth. Formula: `((Current Revenue - Previous Revenue) / Previous Revenue) * 100`.
- **Top Customers**: Customers ranked by total revenue. Formula: `SUM(Revenue)` grouped by Customer, sorted descending.
- **Region Performance**: Total revenue by region. Formula: `SUM(Revenue)` grouped by Region.
- **YoY Comparison** (Extra): Year-over-year growth by month. Formula: `((Current Year Revenue - Previous Year Revenue) / Previous Year Revenue) * 100`.

## Setup Instructions
1. Run `scripts/generate_data.py` to create `data/sample_data.csv`.
2. Open Power BI, import the CSV.
3. Add DAX measures from `powerbi/dax_measures.txt`.
4. Build visuals: Line charts for trends, bar charts for growth/YoY, pie for regions, table for top customers.
5. Add slicers for Month (range), Region, and Year.
6. Create an Executive Summary page with KPI cards and trend highlights.

## Sample Visualizations
Use the generated data to create these in Power BI. Examples include:
- Monthly Revenue Line Chart
- Sales Growth Bar Chart
- Top Customers Bar Chart
- Region Performance Pie Chart
- YoY Revenue Comparison Bar Chart

[Insert rendered charts or images here in your README.]

## Business Impact
This dashboard provides fast insights into trends, top performers, and growth, helping leadership make data-driven decisions. It's appealing to SMBs for its simplicity and impact.

## License
MIT License.
