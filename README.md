# AI Data Visualization Generator

An automated Python-based data visualization system that analyzes a dataset, identifies column types, recommends suitable visualizations, generates charts, performs statistical analysis, detects correlations and outliers, and produces an analytical report.

## Features

* Automatic dataset generation and loading
* Automatic column type detection

  * Numeric
  * Categorical
  * Datetime
  * ID
* Automatic chart recommendations
* Histogram generation
* Bar chart generation
* Scatter plot generation
* Line chart generation
* Pie chart generation
* Correlation heatmap
* Box plot generation
* Automatic statistical insights
* Correlation analysis
* IQR-based outlier detection
* Automatic text report generation

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

## Project Structure

```text
AI-Data-Visualization-Generator/
│
├── app.py
├── requirements.txt
├── data_visualization_report.txt
├── histogram_total_amount.png
├── bar_product_category.png
├── scatter_quantity_vs_unit_price.png
├── line_total_amount_over_time.png
├── pie_region.png
├── correlation_heatmap.png
└── boxplot_total_amount.png
```

## How It Works

The system follows these main steps:

1. Generates and loads a sample dataset containing 500 records.
2. Identifies numeric, categorical, datetime, and ID columns.
3. Recommends appropriate visualization types based on the detected data.
4. Generates multiple charts automatically.
5. Calculates statistical summaries for numeric columns.
6. Analyzes correlations between numeric variables.
7. Detects outliers using the Interquartile Range (IQR) method.
8. Generates a text-based data visualization report.

## Dataset

The application creates a sample dataset containing information such as:

* Order ID
* Date
* Product Category
* Quantity
* Unit Price
* Customer Age
* Customer Rating
* Region
* Total Amount

The `total_amount` value is calculated from quantity and unit price.

## Generated Analysis

The application generates:

* Distribution analysis
* Category comparison
* Relationship analysis
* Time-based analysis
* Regional distribution
* Correlation analysis
* Outlier analysis

## Sample Results

The current generated dataset contains:

* **500 records**
* **9 columns**
* Average total amount: **1332.60**
* Most common product category: **Home**
* Most common region: **North**
* Strong positive correlation between quantity and total amount: **0.68**
* Strong positive correlation between unit price and total amount: **0.69**
* **3 outliers** detected in total amount

## Installation

Clone the repository and install the required libraries:

```bash
pip install -r requirements.txt
```

## Run the Application

Run the following command:

```bash
python app.py
```

The application will analyze the dataset, generate visualizations, display automatic insights, and create the data visualization report.

## Output

The application generates seven visualization files:

1. Histogram
2. Bar Chart
3. Scatter Plot
4. Line Chart
5. Pie Chart
6. Correlation Heatmap
7. Box Plot

It also generates:

```text
data_visualization_report.txt
```

## Internship Project

This project was developed as part of the **AI & Data Science Internship**.

### Project: Data Visualization Generator

### Technologies: Python, Pandas, NumPy, Matplotlib, Seaborn
