# 🛒 Retail Data Analytics & Prediction System

An end-to-end Data Analytics and Machine Learning project built using Python.

This project simulates a real-world retail sales workflow where raw sales data is:
- cleaned and transformed,
- analyzed for business insights,
- visualized using charts,
- and used for machine learning predictions.

The project demonstrates practical skills across:
- Data Engineering
- Data Analysis
- Data Visualization
- Machine Learning

---

# 📌 Project Workflow

```text
Raw Sales Data
      ↓
Data Cleaning & Transformation
      ↓
Exploratory Data Analysis (EDA)
      ↓
Business Insights & Visualization
      ↓
Machine Learning Experiments
      ↓
Prediction System
```

---

# 📌 About the Dataset

The dataset used in this project is intentionally small but raw and unclean.  
This project was built primarily for learning purposes to understand real-world data workflows including:

- data cleaning,
- preprocessing,
- exploratory analysis,
- visualization,
- and machine learning pipelines.

The focus was on handling messy real-world issues such as:
- missing values,
- duplicates,
- inconsistent formatting,
- and invalid data types,

rather than building a production-scale model with a large dataset.

# 📂 Project Files

| File | Purpose |
|------|---------|
| `Cleaning.py` | Cleans and transforms raw sales data |
| `Analysis.py` | Performs exploratory analysis and visualization |
| `FailML.py` | Initial ML attempt using static Revenue formula |
| `Prediction.py` | Final ML model for quantity prediction |
| `sales_raw.csv` | Raw messy dataset |
| `sales_cleaned.csv` | Cleaned dataset generated after preprocessing |

---

# 🏗️ Phase 1 — Data Engineering (`Cleaning.py`)

The raw dataset intentionally contained multiple real-world data issues to simulate industry-style preprocessing challenges.

## ✅ Data Cleaning Performed

### 1. Duplicate Removal
Removed duplicate records based on `Order_ID`.

```python
df.drop_duplicates(subset='Order_ID')
```

---

### 2. Missing Value Handling

Handled missing values in:
- City
- Price
- Quantity
- Date

Approaches used:
- Median imputation
- Group-based median transformation
- Row removal for invalid dates
- Default values where appropriate

---

### 3. Data Type Conversion

Converted:
- Date → datetime
- Price → numeric
- Quantity → numeric

Used:
```python
errors='coerce'
```
to safely handle invalid values.

---

### 4. Text Standardization

Standardized categorical columns using:
```python
str.lower()
```

This helped maintain consistency in:
- Product names
- Categories
- Cities

---

### 5. Handling Invalid Data

Removed:
- Negative prices
- Zero or invalid quantities

Applied business logic to ensure realistic data.

---

### 6. Special Handling of Mixed Quantity Values

The dataset contained text values like:
```text
"three"
```

Instead of blindly coercing them into `NaN`, they were manually mapped:

```python
'three' → 3
```

This preserved valid business information instead of losing data.

---

### 7. Feature Engineering

Created additional columns:
- `Revenue = Price × Quantity`
- `Year`
- `Month`
- `Month_Name`

These features were later used for analysis and visualization.

---

# 📊 Phase 2 — Data Analysis (`Analysis.py`)

Performed exploratory data analysis (EDA) to extract business insights from cleaned sales data.

---

# 📈 Questions Answered

## ✅ Top-Selling Products
Identified products generating the highest revenue.

### Visualization:
- Bar Chart

---

## ✅ Revenue by City
Analyzed city-wise revenue contribution.

### Visualization:
- Pie Chart

---

## ✅ Monthly Sales Trend
Studied monthly revenue patterns and seasonality.

### Visualization:
- Line Chart

---

## ✅ Category Revenue Share
Compared contribution of each product category.

### Visualization:
- Pie Chart

---

# 🔍 Additional Business Questions Explored

Beyond the initial requirements, additional business-oriented questions were analyzed:

## ✅ Which city buys the most electronics?

Used filtered category-level aggregation to identify strongest electronics market.

---

## ✅ Which category sells the highest quantity?

Analyzed quantity-based demand rather than only revenue.

This helped distinguish:
- high-value products
vs
- high-demand products

---

## ✅ Which month generated the highest revenue?

Used grouped monthly aggregation to identify peak business periods.

---

# 💡 Business Insights Generated

Examples of insights extracted:

- Highest revenue-driving product
- Strongest performing city
- Peak sales month
- Highest contributing category

These insights simulate real business reporting workflows.

---

# 🤖 Phase 3 — Initial ML Attempt (`FailML.py`)

An initial machine learning attempt was made to predict Revenue.

However, during experimentation it was realized that:

```text
Revenue = Price × Quantity
```

This is a direct mathematical formula, not a hidden pattern.

Using Linear Regression on a deterministic formula does not represent meaningful machine learning.

## ❌ Why This Was Not Ideal

- Revenue was already mathematically defined.
- The model was effectively learning multiplication.
- Predictions were not valuable from a business intelligence perspective.

This experiment was intentionally kept in the project to demonstrate:
- critical thinking,
- model evaluation,
- and understanding of when ML is appropriate.

---

# 🤖 Phase 4 — Final Machine Learning Model (`Prediction.py`)

A more meaningful ML problem was designed:

## 🎯 Goal
Predict `Quantity` using:
- Price
- Product
- Category
- City

---

# 🧠 ML Workflow

## ✅ Train-Test Split

Dataset split:
- 80% training
- 20% testing

Used:
```python
train_test_split()
```

---

## ✅ Handling Categorical Data

Since ML models require numerical input:

Used:
- `OneHotEncoder`
- `ColumnTransformer`

to convert text categories into machine-readable features.

---

## ✅ Pipeline-Based Modeling

Implemented:
```python
Pipeline()
```

to automate:
1. Encoding
2. Preprocessing
3. Model Training

This created a cleaner and production-style ML workflow.

---

# 📉 Model Evaluation

Evaluated model performance using:

## RMSE (Root Mean Squared Error)
Measures average prediction error magnitude.

## R² Score
Measures how well the model explains data variance.

---

# 📊 Visualization

Generated:
- Actual vs Predicted Quantity plot

This helped visually inspect model performance.

---

# 👤 User Input Prediction System

Added interactive prediction functionality where users can enter:

- Price
- Product
- Category
- City

and receive predicted quantity output.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

# 📚 Key Concepts Demonstrated

## Data Engineering
- Data Cleaning
- Missing Value Handling
- Feature Engineering
- Data Transformation

## Data Analysis
- EDA
- Aggregation
- Visualization
- Business Insights

## Machine Learning
- Regression
- Encoding
- Pipelines
- Model Evaluation

---

# 🚀 Future Improvements

Possible future enhancements:
- Larger datasets
- Power BI dashboard
- Time-series forecasting
- Advanced ML models
- Deployment using Flask/Streamlit

---

# 👩‍💻 Author

Simran

This project was built as a hands-on learning project to understand real-world data workflows from raw data to prediction systems.
