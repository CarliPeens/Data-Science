# PCA and Clustering Analysis on USArrests Dataset

This project explores and visualizes crime statistics across U.S. states using **Principal Component Analysis (PCA)** and **clustering techniques**. The dataset includes crime rates and urban population percentages from 1973.

## 📊 Dataset

**Source**: USArrests dataset (R base dataset)  
**Rows**: 50 (one for each U.S. state)  
**Columns**:
- `Murder`: Murder arrests per 100,000 residents
- `Assault`: Assault arrests per 100,000 residents
- `UrbanPop`: % of the population in urban areas
- `Rape`: Rape arrests per 100,000 residents

## 🧪 Objectives

- Understand the relationships between violent crimes and urban population.
- Reduce dimensionality using PCA while retaining most of the variance.
- Group similar states using KMeans and Hierarchical Clustering.
- Visualize data patterns, principal components, and clustering outcomes.

## 🔍 Analysis Steps

### 1. **Data Exploration**
- Summary statistics and missing value checks
- Correlation matrix heatmap
- Key findings:
  - Murder and Assault are highly correlated (r ≈ 0.80)
  - Urban population has weak correlation with crime rates

### 2. **Data Scaling & PCA**
- Data normalized using `StandardScaler`
- PCA applied to identify principal components
- Biplot generated to visualize the contributions of original features
- First 2 PCs capture ~86% of total variance

### 3. **Clustering**
- **KMeans** clustering applied to the first two PCs  
  - Optimal number of clusters determined using the Elbow method and Silhouette Score
- **Hierarchical Clustering** using Ward linkage  
  - Dendrogram plotted to visualize merge distances

### 4. **Visualizations**
- Biplot of PCA
- Explained variance plot
- KMeans cluster scatter plot
- Dendrogram
- Agglomerative clustering visualization

## 📌 Key Findings

- PCA revealed that **Murder**, **Assault**, and **Rape** contribute heavily to PC1.
- Clustering grouped states into 3 distinct crime profiles:
  1. High violent crime states
  2. Low crime states
  3. Moderate crime states
- Urban population had less influence on PCA and cluster grouping.

## 🛠 Dependencies

Create a virtual environment and install the required libraries:

```bash
python -m venv usarrests_env
source usarrests_env/bin/activate  # On Windows: usarrests_env\Scripts\activate
pip install pandas numpy matplotlib seaborn scikit-learn scipy adjustText
```

## 📁 Files

- `USArrests_PCA_Clustering_Updated.ipynb` — Jupyter Notebook with the full analysis
- `UsArrests.csv` — Dataset (make sure this is placed in the same directory)
- `README.md` — Project description

## 📌 Notes

- The dataset includes only 4 variables, making it ideal for demonstrating dimensionality reduction and clustering.
- PCA enables effective 2D visualizations while preserving interpretability.

## 📷 Preview

![PCA Clusters](images/sample_pca_clusters.png) *(Add this image if needed)*

## 👤 Author

Carli Peens  
**Date**: July 2025
