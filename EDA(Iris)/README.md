# Iris Dataset Exploratory Data Analysis (EDA)

## Overview
This project performs an exploratory data analysis (EDA) on the classic Iris dataset. The Iris dataset consists of 150 observations of iris flowers with four features — sepal length, sepal width, petal length, and petal width — along with their species labels. The goal of this analysis is to understand the data distribution, relationships between features, and key insights that can inform machine learning models.

## Dataset
The Iris dataset includes:

**Features:**
- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

**Target:**
- Species (`setosa`, `versicolor`, `virginica`)

The dataset is commonly available via Python libraries such as scikit-learn and seaborn.

## Project Structure
```
Iris_EDA/
│
├── Iris_EDA.ipynb       # Jupyter Notebook containing the analysis
├── README.md            # Project description and instructions
```

## Analysis Performed

**Data Inspection:**  
- Checking data types, missing values, and basic statistics.

**Visualization:**  
- Pairplots to visualize feature relationships by species.  
- Boxplots to check feature distributions.  
- Heatmap of feature correlations.

**Insights:**  
- Identify patterns or trends that distinguish different iris species.  
- Detect outliers and variations in measurements.

## Installation
To run this notebook locally:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

4. Open `Iris_EDA.ipynb` and run the cells.

## Dependencies
- Python 3.x  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

## Author
**Carli Peens** – Data Science Enthusiast

## License
This project is for educational purposes. Feel free to use or modify it with credit.


