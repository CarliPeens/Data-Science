
# 📉 Telco Customer Churn Prediction Project

## 📝 Overview

This project analyzes customer churn behavior in the telecom industry. Using a publicly available dataset, we predict which customers are likely to **churn** (i.e., stop using the service) using two machine learning models:

- **Logistic Regression**
- **Random Forest Classifier**

The notebook walks through all critical steps of a data science pipeline:
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Feature engineering and scaling
- Model training, evaluation, and comparison
- Business insights and model interpretability

---

## 📂 Dataset Summary

The dataset comes from the IBM Sample Data Sets and includes:
- **7044 rows** (individual customer records)
- **21 columns** (features and the target label)

### 🔑 Features include:
- Customer demographics: `gender`, `SeniorCitizen`, `Partner`, `Dependents`
- Service usage: `InternetService`, `TechSupport`, `StreamingTV`
- Account information: `Contract`, `MonthlyCharges`, `TotalCharges`
- Target variable: `Churn` (Yes/No)

---

## 🔧 Preprocessing Steps

1. Convert `TotalCharges` to numeric (handle non-numeric entries)
2. Remove missing values
3. Drop the irrelevant `customerID` column
4. Encode the `Churn` column: Yes → 1, No → 0
5. Apply one-hot encoding to all categorical features (`get_dummies`)
6. Store the clean dataset in `telecom_cust_dummies`

---

## 📊 Exploratory Data Analysis (EDA)

- **Heatmap** to visualize correlations between features and `Churn`
- **Histogram** of customer tenure
- **Scatter plot** between `MonthlyCharges` and `TotalCharges`
- **Boxplot** of `tenure` by churn status

### 📌 Key Findings:
- Churn is negatively correlated with tenure: **newer customers are more likely to churn**
- Most customers have lower tenure and lower total charges
- Longer-tenure customers are more likely to stay

---

## ⚙️ Machine Learning Models

### 1. Logistic Regression
- Baseline linear classifier
- Good recall: better at capturing customers who churn
- Model metrics:
  - Accuracy: ~0.79
  - Precision: ~0.70
  - Recall: **0.5175**

### 2. Random Forest Classifier
- 2000 decision trees
- Out-of-bag (OOB) validation enabled
- Limited tree complexity (`max_leaf_nodes=50`)
- Slightly higher accuracy, but more false negatives
- Model metrics:
  - Accuracy: ~0.80
  - Precision: ~0.71
  - Recall: **0.4541**
  - OOB Error: ~0.20

---

## 📈 Model Evaluation

| Metric      | Logistic Regression | Random Forest |
|-------------|---------------------|----------------|
| Accuracy    | ~0.79               | ~0.80          |
| Precision   | ~0.70               | ~0.71          |
| Recall      | **0.5175**          | 0.4541         |
| OOB Error   | N/A                 | ~0.20          |

- **Confusion matrices** were used to examine false positives and false negatives
- **Random Forest** had more false negatives, meaning it missed more true churn cases
- **Logistic Regression** is better suited if your business objective is to **retain churn-risk customers**

---

## 💼 Business Takeaways

- **Short-tenure customers** are at higher risk of churn — early intervention is key
- **Fiber optic users** and **monthly contract holders** tend to churn more
- Offering loyalty programs or discounts early could improve retention

---

## 🔍 Potential Improvements

- Add **ROC-AUC and F1 Score**
- Hyperparameter tuning using `GridSearchCV`
- Try other classifiers (e.g., XGBoost, SVM)
- Feature selection or dimensionality reduction (PCA)
- Use SHAP/LIME for interpretability

---

## 💾 Files

- `Telco-Customer-Churn.csv` – Raw dataset
- `telco_churn_analysis.ipynb` – Jupyter Notebook with full code
- `Telco_Churn_Analysis_README.md` – Project documentation (this file)


---

## 🧠 Keywords

`Data Science`, `Customer Churn`, `Classification`, `Logistic Regression`, `Random Forest`, `Pandas`, `Scikit-learn`, `Telco Dataset`

