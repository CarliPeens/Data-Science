
# Telco Customer Churn Analysis

This notebook predicts customer churn using **Logistic Regression** and **Random Forest** models.  
It includes data inspection, preprocessing, visualization, scaling, training, evaluation, and inline explanations.

---

## Dataset Overview

The database contains **7044 rows** (customers) and **21 columns** (features).

### Features:

- `customerID`: Unique identifier of a customer  
- `gender`: Gender of customer  
- `SeniorCitizen`: Binary variable indicating if customer is senior citizen  
- `Partner`: Binary variable if customer has a partner  
- `Dependents`: Binary variable if customer has dependent  
- `tenure`: Number of weeks as a customer  
- `PhoneService`: Whether customer has phone service  
- `MultipleLines`: Whether customer has multiple lines  
- `InternetService`: Type of internet service ("DSL", "Fiber optic", "No")  
- `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`: Various services  
- `StreamingTV`, `StreamingMovies`: Streaming service usage  
- `Contract`: Type of contract ('Month-to-month', 'One year', 'Two year')  
- `PaperlessBilling`: Whether paperless billing is enabled  
- `PaymentMethod`: Customer payment method  
- `MonthlyCharges`: Monthly charge amount ($)  
- `TotalCharges`: Total amount charged so far ($)  
- `Churn`: Whether customer churned (Yes/No)  

---

## Key Implementation Highlights

### Data Preprocessing:

- Converted `TotalCharges` to numeric
- Dropped missing rows and `customerID`
- Encoded `Churn` as binary
- One-hot encoded all categorical features using `get_dummies()` with `drop_first=True`

### Visualisation:

- Correlation heatmap between features and `Churn`
- Histogram of `tenure`
- Scatter plot of `MonthlyCharges` vs `TotalCharges`
- Boxplot of `tenure` by `Churn` status

### Modeling:

**1. Logistic Regression**
- Accuracy, precision, and recall calculated
- Confusion matrix plotted
- Higher recall (0.5175) than Random Forest — better at identifying churners

**2. Random Forest**
- 2000 estimators, OOB scoring enabled, max_leaf_nodes=50, bootstrap=True
- Slightly higher accuracy but more false negatives (lower recall = 0.4541)
- OOB error ≈ 0.20 — generalises well without overfitting

---

## Final Evaluation

| Metric              | Logistic Regression | Random Forest |
|---------------------|---------------------|----------------|
| Accuracy            | ~0.79               | ~0.80          |
| Precision           | ~0.70               | ~0.71          |
| Recall              | **0.5175**          | 0.4541         |
| OOB Error           | N/A                 | ~0.20          |

### ✅ Conclusion:
- **Logistic Regression** performs better for identifying churners (higher recall)
- **Random Forest** performs slightly better in accuracy and precision but misses more actual churn cases

---

## Author:
Capstone Project – Telco Customer Churn (2025)
