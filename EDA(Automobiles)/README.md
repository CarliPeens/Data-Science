
# 🚗 Automobile Dataset - Exploratory Data Analysis (EDA)

This project performs exploratory data analysis on a dataset of automobiles. The objective is to clean the data, convert necessary fields into appropriate data types, and derive insights through visualizations about pricing, fuel efficiency, engine size, and manufacturer trends.

---

## 📁 Dataset

The dataset used in this analysis is `automobile.txt`, which contains specifications and characteristics of various car models including:
- Price
- Engine size
- Fuel efficiency (city & highway mpg)
- Body style
- Manufacturer (make)

---

## 🔧 Steps Performed

### 1. Data Cleaning
- Dropped irrelevant columns: `normalized-losses`, `symboling`, `engine-location`
- Removed rows with missing values indicated by `'?'`
- Removed duplicate rows

### 2. Data Type Conversion
- Converted all numeric-looking columns to `int64` using NumPy
- Handled coercion errors using `pd.to_numeric` and filled remaining `NaN` with 0

### 3. Category Analysis
- Isolated all cars with the `body-style` set as `hatchback`

---

## 📊 Visual Analysis

### 🔺 Most Expensive vs Cheapest Cars
- Compared highway and city MPG of the top 5 most expensive and cheapest cars
- Insight: Fuel efficiency is not significantly better in more expensive cars

### ⚡ Most Fuel-Efficient Manufacturer
- Calculated the average highway MPG for each manufacturer
- Insight: **Chevrolet** had the highest average fuel efficiency

### 🔧 Vehicles with Largest Engine Capacity
- Identified top 5 cars with the largest engine sizes
- Insight: **Jaguar** and **Mercedes-Benz** dominate the high-end performance segment

### 🏭 Manufacturers with the Most Models
- Counted the number of entries per manufacturer
- Insight: **Toyota** had the highest number of distinct entries

---

## 📈 Technologies Used

- **Python**: Data manipulation and logic
- **Pandas**: Data cleaning and transformation
- **Seaborn & Matplotlib**: Data visualization

---

## 📌 Conclusion

The analysis revealed that:
- More expensive vehicles do not always have better fuel economy
- Jaguar and Mercedes focus on performance (high engine capacity)
- Chevrolet leads in fuel efficiency
- Toyota is the most represented manufacturer in this dataset

---

## 🚀 How to Run

1. Clone this repository or download the files.
2. Ensure you have Python 3 and Jupyter Notebook installed.
3. Install the required libraries:
   ```bash
   pip install pandas matplotlib seaborn
   ```
4. Run the Jupyter notebook to see the outputs and visualizations:
   ```bash
   jupyter notebook automobile_eda.ipynb
   ```

---

## 👤 Author

**Carli Peens**   
July 2025

---

## 📄 License

This project is for educational purposes. Feel free to use or modify it with credit.
