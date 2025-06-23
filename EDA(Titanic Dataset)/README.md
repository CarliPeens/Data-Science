
# 🚢 Exploratory Data Analysis on the Titanic Dataset

This project performs a comprehensive Exploratory Data Analysis (EDA) on the famous Titanic dataset, which contains demographic and travel information of passengers aboard the RMS Titanic. The goal is to uncover patterns and key factors that influenced survival during the disaster.

---

## 📁 Dataset Overview

- **Rows:** 892  
- **Columns:** 12  
- **Target Variable:** `Survived` (1 = survived, 0 = did not survive)

### Main Features:
- `PassengerId`: Unique ID  
- `Pclass`: Passenger class (1st = Upper, 3rd = Lower)  
- `Name`, `Sex`, `Age`: Personal details  
- `SibSp`, `Parch`: Family aboard  
- `Ticket`, `Fare`, `Cabin`: Travel details  
- `Embarked`: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)  

---

## 📊 Project Structure

- **Data Cleaning:**
  - Filled missing values in `Age` and `Embarked`.
  - Dropped `Cabin` due to excessive missing data.
  - Converted `Sex` to numeric for analysis.

- **Visualizations:**
  - Histograms and box plots for continuous features (`Age`, `Fare`)
  - Count plots for categorical features (`Pclass`, `Embarked`)
  - Correlation heatmap for numerical variables
  - Bar plots to investigate survival by gender, age group, class, and embarkation port

- **Key Analysis Questions:**
  - Did women and children get priority?
  - Were upper-class passengers favored?
  - Does embarkation port impact survival?
  - Which features correlate most with survival?

---

## 📌 Key Findings

| Factor                  | Insight                                                       |
|------------------------|---------------------------------------------------------------|
| `Sex`                  | Women had significantly higher survival rates                 |
| `Age`                  | Children under 16 had better survival than adults             |
| `Pclass`               | 1st class passengers were prioritized during evacuation       |
| `Fare`                 | Higher fare generally linked to higher survival               |
| `Embarked`             | Passengers from Cherbourg had the highest survival rate       |

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Pandas** – data manipulation  
- **NumPy** – numerical operations  
- **Matplotlib & Seaborn** – visualizations  
- **Scikit-learn** – preprocessing  
- **Jupyter Notebook** – interactive analysis

---

## 📁 Files Included

- `Titanic.csv` – Dataset used  
- `Titanic_EDA.ipynb` – Notebook with full analysis  
- `README.md` – Project overview  

---

## 💡 Future Improvements

- Feature engineering (e.g., extract title from name)  
- Model building (classification using logistic regression, etc.)  
- Handling non-linear correlations  
- Dashboard for interactive exploration

---

## 📝 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
