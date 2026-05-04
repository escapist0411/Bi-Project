# 📊 BI-Based Job Market Demand Analysis Dashboard

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange.svg)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)](https://pandas.pydata.org/)
[![Power BI](https://img.shields.io/badge/Power--BI-Visualizations-yellow.svg)](https://powerbi.microsoft.com/)

## 📝 Project Overview
This project focuses on building a **Business Intelligence (BI) Dashboard** to analyze job market demand using Machine Learning. We leverage a **Decision Tree Classifier** optimized via **Grid Search Cross-Validation (GridSearchCV)** to predict the target variable (Job Location) based on inputs such as Job Title, Experience Level, and Salary. 

The machine learning insights generated from the backend python scripts are designed to be imported into **Power BI** to deliver an interactive, data-driven visualization dashboard.

---

## 🛠️ Technologies Used
*   **Python (Jupyter Notebook / Python Scripts)**: The backbone for data analysis, preprocessing, and machine learning model training.
*   **Pandas & NumPy**: For generating, manipulating, and preparing data for ML pipelines.
*   **Scikit-Learn**: For implementing hyperparameter-tuned Decision Tree classification.
*   **Matplotlib / Seaborn**: For static data visualizations inside Python workflows.
*   **Power BI**: The end-stage visualization tool mapping data into dynamic dashboards (Scatter plots, Bar charts, interactive filters).

---

## 📁 Project Structure

```text
BI-Project/
│
├── data/
│   └── dataset.csv              # The CSV dataset (generated via mock script)
│
├── src/
│   └── model.py                 # Core ML logic (Decision Tree + GridSearch)
│
├── create_mock_data.py          # Script to generate a 500-sample mock dataset
├── DAX_formulas.md              # Helpful DAX expressions for Power BI Dashboarding
├── requirements.txt             # Python project dependencies
└── README.md                    # Project Documentation
```

---

## 📊 The Dataset Architecture
The machine learning model operates on a relational dataset containing the following attributes:
*   **Job Title**: Type of job role (Algorithmically Encoded: `0-40`)
*   **Experience Level**: The required experience level for the job (`0%-100%`)
*   **Salary**: Base compensation bracket (`0-100`)
*   **Location (Target Variable)**: The job location bucket mapping predictions to geographic hubs.

---

## 🚀 Setup & Installation Instructions

### 1. Clone the repository
```bash
git clone https://github.com/escapist0411/Bi-Project.git
cd Bi-Project
```

### 2. Install Dependencies
Make sure you are utilizing a Python 3.x environment. Then, install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Generate Mock Data
Since datasets are often private, we included a script to generate 500 rows of synthetic real-world matching data:
```bash
python create_mock_data.py
```
*(This will generate `data/dataset.csv`)*

### 4. Train and Evaluate the Model
Run the primary Machine Learning analysis:
```bash
cd src
python model.py
```
This routine splits the dataset (80% training / 20% testing), executes Hyperparameter tuning using `GridSearchCV`, and prints analytical scores such as:
- **Accuracy Score**
- **Precision, Recall, & F1-Score**
- **Confusion Matrix**

### 5. Build Power BI Dashboard
1. Open **Power BI Desktop**.
2. Go to `Get Data` -> `Text/CSV` and select `data/dataset.csv`.
3. Consult `DAX_formulas.md` in this repository for plug-and-play formulas to create `High Demand Flags`, `Average Salary`, and `Total Job Openings` measures.
4. Visualize using Interactive line charts & map clusters!
