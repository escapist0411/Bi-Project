# BI-Based Job Market Demand Analysis Dashboard

## Project Overview
This project involves building a Business Intelligence (BI) dashboard to analyze job market demand using Machine Learning. A Decision Tree algorithm is trained on a dataset containing attributes such as Job Title, Experience Level, and Salary to predict the Job Location (Target Variable). The insights generated from the model are visualized using Power BI to provide an interactive dashboard.

## Technologies Used
*   **Python (Jupyter Notebook)**: Data analysis, preprocessing, and machine learning.
*   **Pandas**: Data manipulation and preprocessing.
*   **Scikit-Learn**: Decision Tree classifier implementation.
*   **Matplotlib / Seaborn**: Static visualizations.
*   **Power BI**: Interactive dashboards for data visualization.

## Dataset Description
The model uses a structured dataset with the following features:
*   **Job Title**: Type of job role (encoded 0-40)
*   **Experience Level**: Percentage of experience level (0-100%)
*   **Salary**: Salary offered (0-100)
*   **Location**: Job location (Target variable)

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd BI-Job-Market-Analysis
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the analysis:**
    Execute the Python scripts in the `src/` directory or open the Jupyter notebook (if provided) to reproduce the model evaluation.
