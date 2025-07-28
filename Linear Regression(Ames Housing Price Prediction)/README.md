# 🏡 Ames Housing Price Prediction

This project analyzes housing data from Ames, Iowa to predict house sale prices using multiple linear regression. The primary focus is on two features: `Gr_Liv_Area` (above ground living area) and `Garage_Area`.

---

## 📁 Dataset Description

The dataset is a simplified version of the **Ames Housing Dataset** originally compiled by De Cock (2011), describing 2,930 property sales in Ames, Iowa between 2006 and 2010.

**Selected Features:**
- `Year_Built`: Year the house was constructed
- `Year_Remod_Add`: Year the house was last remodeled
- `Total_Bsmt_SF`: Basement square footage
- `First_Flr_SF`: First floor square footage
- `Second_Flr_SF`: Second floor square footage
- `Gr_Liv_Area`: Above ground living area (in sq ft)
- `Full_Bath`, `Half_Bath`: Number of full/half bathrooms
- `Bedroom_AbvGr`: Number of bedrooms above ground
- `Kitchen_AbvGr`: Number of kitchens above ground
- `TotRms_AbvGrd`: Total rooms above ground (excl. bathrooms)
- `Fireplaces`: Number of fireplaces
- `Garage_Area`: Garage area (in sq ft)
- `Sale_Price`: Sale price (target variable)

> 📚 Source: [De Cock, D. (2011)](https://ww2.amstat.org/publications/jse/v19n3/decock.pdf)

---

## 🎯 Project Objective

To build a **Multiple Linear Regression** model that:
- Analyzes the relationships between `Gr_Liv_Area`, `Garage_Area`, and `Sale_Price`
- Predicts house sale prices using those features
- Evaluates model performance using RMSE and MSE

---

## 📊 Steps Performed

### 1. Data Inspection and Cleaning
- Checked for missing values — none found
- Checked for **zero values** in key numeric fields
  - Found several homes with 0 garage or basement area — realistic cases

### 2. Data Visualization
- Histograms of `Sale_Price`, `Gr_Liv_Area`, and `Garage_Area`
- Correlation heatmap
- Scatterplots and regression lines

### 3. Model Training
- Features: `Gr_Liv_Area`, `Garage_Area`
- Split: 75% training / 25% testing
- Used **LinearRegression** from `sklearn`

### 4. Evaluation
- Mean Squared Error (Mse)
- Root Mean Squared Error (RMSE)
- Plot of Actual vs. Predicted values

---

## 🧮 Results

### Coefficients:
- **Gr_Liv_Area:** ≈ $79 per sq ft
- **Garage_Area:** ≈ $141 per sq ft

### Performance:
- **RMSE:** ~$51,300
- Indicates a moderate prediction error

---

## 📈 Key Insights

- `Gr_Liv_Area` and `Garage_Area` both have strong positive correlations with sale price.
- Garage space has a **larger marginal impact per square foot** than living area in this model.
- Data is **right-skewed**, consistent with real estate markets.

---

## ▶️ How to Run

```bash
# 1. Clone the repository or download the files
# 2. Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

# 3. Run the Python script
python house_price_prediction.py
```

---

## 📜 License

MIT License. Educational use only.

---

## 🙌 Acknowledgements

- Dataset courtesy of [Journal of Statistics Education](https://ww2.amstat.org/publications/jse/v19n3/decock.pdf)
- Project inspired by common regression problems in real estate pricing.
