import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class DataVisualizationGenerator:

    def __init__(self):
        self.data = None
        self.column_types = {
            "numeric": [],
            "categorical": [],
            "datetime": [],
            "id": []
        }

    def load_data(self):
        np.random.seed(42)

        data = {
            "order_id": range(1, 501),
            "date": pd.date_range("2026-01-01", periods=500),
            "product_category": np.random.choice(
                ["Electronics", "Clothing", "Books", "Home", "Sports"],
                500
            ),
            "quantity": np.random.randint(1, 10, 500),
            "unit_price": np.random.uniform(10, 500, 500).round(2),
            "customer_age": np.random.randint(18, 65, 500),
            "customer_rating": np.random.uniform(1, 5, 500).round(1),
            "region": np.random.choice(
                ["North", "South", "East", "West"],
                500
            )
        }

        self.data = pd.DataFrame(data)

        self.data["total_amount"] = (
            self.data["quantity"] * self.data["unit_price"]
        ).round(2)

        print("\n✅ Dataset loaded successfully!")
        print(f"Rows: {len(self.data)}")
        print(f"Columns: {len(self.data.columns)}")

    def detect_column_types(self):

        for column in self.data.columns:

            if pd.api.types.is_datetime64_any_dtype(
                self.data[column]
            ):
                self.column_types["datetime"].append(column)

            elif pd.api.types.is_numeric_dtype(
                self.data[column]
            ):
                if "id" in column.lower():
                    self.column_types["id"].append(column)
                else:
                    self.column_types["numeric"].append(column)

            else:
                self.column_types["categorical"].append(column)

        print("\n📋 COLUMN TYPE ANALYSIS")

        for column_type, columns in self.column_types.items():
            print(f"{column_type.title()}: {columns}")

    def recommend_charts(self):

        recommendations = []

        # Numeric columns → Histogram
        for column in self.column_types["numeric"]:
            recommendations.append(
                f"📊 Histogram → {column} (distribution)"
            )

        # Categorical columns → Bar Chart
        for column in self.column_types["categorical"]:
            recommendations.append(
                f"📊 Bar Chart → {column} (category comparison)"
            )

        # Two numeric columns → Scatter Plot
        if len(self.column_types["numeric"]) >= 2:
            x = self.column_types["numeric"][0]
            y = self.column_types["numeric"][1]

            recommendations.append(
                f"🔵 Scatter Plot → {x} vs {y}"
            )

        # Date + numeric → Line Chart
        if (
            self.column_types["datetime"]
            and self.column_types["numeric"]
        ):
            date = self.column_types["datetime"][0]
            value = self.column_types["numeric"][0]

            recommendations.append(
                f"📈 Line Chart → {value} over {date}"
            )

        # 3+ numeric columns → Heatmap
        if len(self.column_types["numeric"]) >= 3:
            recommendations.append(
                "🔥 Heatmap → Correlation between numeric columns"
            )

        return recommendations

    def create_histogram(self, column):
        plt.figure(figsize=(10, 6))

        plt.hist(
            self.data[column],
            bins=20,
            edgecolor="black"
        )

        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")

        plt.tight_layout()

        filename = f"histogram_{column}.png"
        plt.savefig(filename)

        plt.show()

        print(f"✅ Histogram created: {filename}")

    def create_bar_chart(self, column):
        plt.figure(figsize=(10, 6))

        value_counts = self.data[column].value_counts()

        plt.bar(
            value_counts.index,
            value_counts.values,
            edgecolor="black"
        )

        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")

        plt.xticks(rotation=30)

        plt.tight_layout()

        filename = f"bar_{column}.png"
        plt.savefig(filename)

        plt.show()

        print(f"✅ Bar chart created: {filename}")

    def create_scatter_plot(self, x_column, y_column):
        plt.figure(figsize=(10, 6))

        plt.scatter(
            self.data[x_column],
            self.data[y_column],
            alpha=0.6
        )

        plt.title(f"{y_column} vs {x_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)

        plt.tight_layout()

        filename = f"scatter_{x_column}_vs_{y_column}.png"
        plt.savefig(filename)

        plt.show()

        print(f"✅ Scatter plot created: {filename}")

    def create_line_chart(self, date_column, value_column):
        plt.figure(figsize=(10, 6))

        data = self.data.sort_values(date_column)

        plt.plot(
            data[date_column],
            data[value_column]
        )

        plt.title(f"{value_column} over Time")
        plt.xlabel(date_column)
        plt.ylabel(value_column)

        plt.xticks(rotation=45)

        plt.tight_layout()

        filename = f"line_{value_column}_over_time.png"
        plt.savefig(filename)

        plt.show()

        print(f"✅ Line chart created: {filename}")

    def create_pie_chart(self, column):
        plt.figure(figsize=(8, 8))

        value_counts = self.data[column].value_counts()

        plt.pie(
            value_counts.values,
            labels=value_counts.index,
            autopct="%1.1f%%"
        )

        plt.title(f"Distribution of {column}")

        plt.tight_layout()

        filename = f"pie_{column}.png"
        plt.savefig(filename)

        plt.show()

        print(f"✅ Pie chart created: {filename}")

    def create_heatmap(self):
        plt.figure(figsize=(10, 7))

        numeric_data = self.data[self.column_types["numeric"]]
        correlation = numeric_data.corr()

        sns.heatmap(
            correlation,
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )

        plt.title("Correlation Heatmap")

        plt.tight_layout()

        filename = "correlation_heatmap.png"
        plt.savefig(filename)

        plt.show()

        print(f"✅ Heatmap created: {filename}")

    def create_box_plot(self, column):
        plt.figure(figsize=(8, 6))

        plt.boxplot(
            self.data[column],
            orientation="vertical"
        )

        plt.title(f"Box Plot of {column}")
        plt.ylabel(column)

        plt.tight_layout()

        filename = f"boxplot_{column}.png"
        plt.savefig(filename)

        plt.show()

        print(f"✅ Box plot created: {filename}")

    def generate_insights(self):
        print("\n💡 AUTOMATIC INSIGHTS")
        print("-" * 40)

        # Total records
        print(f"📌 Total records: {len(self.data)}")

        # Numeric statistics
        for column in self.column_types["numeric"]:
            average = self.data[column].mean()
            minimum = self.data[column].min()
            maximum = self.data[column].max()

            print(f"\n📊 {column}")
            print(f"   Average: {average:.2f}")
            print(f"   Minimum: {minimum:.2f}")
            print(f"   Maximum: {maximum:.2f}")

        # Most common categories
        for column in self.column_types["categorical"]:
            most_common = self.data[column].value_counts().idxmax()

            print(
                f"\n🏆 Most common {column}: {most_common}"
            )

        # Correlation insights
        numeric_data = self.data[
            self.column_types["numeric"]
        ]

        correlation = numeric_data.corr()

        print("\n🔗 CORRELATION INSIGHTS")

        for i in range(len(correlation.columns)):
            for j in range(i + 1, len(correlation.columns)):

                column1 = correlation.columns[i]
                column2 = correlation.columns[j]

                value = correlation.iloc[i, j]

                if abs(value) >= 0.5:
                    strength = "strong"
                elif abs(value) >= 0.3:
                    strength = "moderate"
                else:
                    strength = "weak"

                direction = (
                    "positive"
                    if value > 0
                    else "negative"
                )

                print(
                    f"📈 {column1} vs {column2}: "
                    f"{strength} {direction} correlation "
                    f"({value:.2f})"
                )

        # Outlier detection
        print("\n🚨 OUTLIER DETECTION")

        for column in self.column_types["numeric"]:

            q1 = self.data[column].quantile(0.25)
            q3 = self.data[column].quantile(0.75)

            iqr = q3 - q1

            lower_limit = q1 - 1.5 * iqr
            upper_limit = q3 + 1.5 * iqr

            outliers = self.data[
                (self.data[column] < lower_limit)
                | (self.data[column] > upper_limit)
            ]

            print(
                f"📦 {column}: "
                f"{len(outliers)} outliers detected"
            )

    def generate_report(self):
        filename = "data_visualization_report.txt"

        with open(filename, "w", encoding="utf-8") as report:

            report.write("DATA VISUALIZATION REPORT\n")
            report.write("=" * 50 + "\n\n")

            # Dataset summary
            report.write("DATASET SUMMARY\n")
            report.write("-" * 30 + "\n")
            report.write(f"Total Records: {len(self.data)}\n")
            report.write(f"Total Columns: {len(self.data.columns)}\n\n")

            # Column analysis
            report.write("COLUMN TYPE ANALYSIS\n")
            report.write("-" * 30 + "\n")

            for column_type, columns in self.column_types.items():
                report.write(
                    f"{column_type.title()}: {', '.join(columns)}\n"
                )

            # Numeric statistics
            report.write("\nNUMERIC STATISTICS\n")
            report.write("-" * 30 + "\n")

            for column in self.column_types["numeric"]:
                average = self.data[column].mean()
                minimum = self.data[column].min()
                maximum = self.data[column].max()

                report.write(
                    f"{column}: "
                    f"Average={average:.2f}, "
                    f"Min={minimum:.2f}, "
                    f"Max={maximum:.2f}\n"
                )

            # Category insights
            report.write("\nCATEGORY INSIGHTS\n")
            report.write("-" * 30 + "\n")

            for column in self.column_types["categorical"]:
                most_common = self.data[column].value_counts().idxmax()

                report.write(
                    f"Most common {column}: {most_common}\n"
                )

            # Correlation analysis
            report.write("\nCORRELATION INSIGHTS\n")
            report.write("-" * 30 + "\n")

            numeric_data = self.data[
                self.column_types["numeric"]
            ]

            correlation = numeric_data.corr()

            for i in range(len(correlation.columns)):
                for j in range(i + 1, len(correlation.columns)):

                    column1 = correlation.columns[i]
                    column2 = correlation.columns[j]

                    value = correlation.iloc[i, j]

                    if abs(value) >= 0.5:
                        strength = "strong"
                    elif abs(value) >= 0.3:
                        strength = "moderate"
                    else:
                        strength = "weak"

                    direction = (
                        "positive"
                        if value > 0
                        else "negative"
                    )

                    report.write(
                        f"{column1} vs {column2}: "
                        f"{strength} {direction} "
                        f"correlation ({value:.2f})\n"
                    )

            # Outlier detection
            report.write("\nOUTLIER DETECTION\n")
            report.write("-" * 30 + "\n")

            for column in self.column_types["numeric"]:

                q1 = self.data[column].quantile(0.25)
                q3 = self.data[column].quantile(0.75)

                iqr = q3 - q1

                lower_limit = q1 - 1.5 * iqr
                upper_limit = q3 + 1.5 * iqr

                outliers = self.data[
                    (self.data[column] < lower_limit)
                    | (self.data[column] > upper_limit)
                ]

                report.write(
                    f"{column}: "
                    f"{len(outliers)} outliers detected\n"
                )

            # Generated charts
            report.write("\nGENERATED VISUALIZATIONS\n")
            report.write("-" * 30 + "\n")

            report.write("1. Histogram\n")
            report.write("2. Bar Chart\n")
            report.write("3. Scatter Plot\n")
            report.write("4. Line Chart\n")
            report.write("5. Pie Chart\n")
            report.write("6. Correlation Heatmap\n")
            report.write("7. Box Plot\n")

        print(f"\n📄 Report generated: {filename}")            


# ==================================================
# MAIN PROGRAM
# ==================================================

# Create generator
generator = DataVisualizationGenerator()

# Load dataset
generator.load_data()

# Detect column types
generator.detect_column_types()

# Chart recommendations
print("\n🤖 CHART RECOMMENDATIONS")

recommendations = generator.recommend_charts()

for recommendation in recommendations:
    print(recommendation)

# Histogram
print("\n📊 CREATING HISTOGRAM")

generator.create_histogram("total_amount")

# Bar chart
print("\n📊 CREATING BAR CHART")

generator.create_bar_chart("product_category")

# Scatter plot
print("\n🔵 CREATING SCATTER PLOT")

generator.create_scatter_plot(
    "quantity",
    "unit_price"
)

# Line chart
print("\n📈 CREATING LINE CHART")

generator.create_line_chart(
    "date",
    "total_amount"
)

# Pie chart
print("\n🥧 CREATING PIE CHART")

generator.create_pie_chart("region")

# Heatmap
print("\n🔥 CREATING HEATMAP")

generator.create_heatmap()

# Box plot
print("\n📦 CREATING BOX PLOT")

generator.create_box_plot("total_amount")

# Automatic insights
print("\n🧠 GENERATING AUTOMATIC INSIGHTS")

generator.generate_insights()

print("\n📄 GENERATING REPORT")

generator.generate_report()