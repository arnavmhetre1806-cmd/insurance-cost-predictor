# 💰 Medical Insurance Cost Predictor

A Machine Learning-powered web application that predicts medical insurance charges based on personal and lifestyle information such as age, BMI, smoking habits, gender, number of children, and residential region.

Built using Python, Scikit-learn, Pandas, and Streamlit.

## 🚀 Project Overview

The objective of this project is to develop a regression-based Machine Learning system that estimates individual medical insurance costs.

Three regression algorithms are trained and compared using 5-Fold Cross-Validation. The best-performing model is then integrated into an interactive Streamlit application.

## ✨ Features

- Exploratory Data Analysis (EDA)
- Data cleaning and preprocessing
- Missing value and duplicate checks
- Categorical feature encoding using OneHotEncoder
- Numerical feature scaling using StandardScaler
- Multiple regression model comparison
- 5-Fold Cross-Validation
- Model evaluation using MAE, RMSE, and R²
- Feature importance analysis
- Interactive Streamlit prediction interface

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Exploratory data analysis |
| Scikit-learn | Machine Learning |
| Joblib | Model serialization |
| Streamlit | Web application |

## 📊 Dataset

**Medical Cost Personal Dataset**

The dataset contains information about individuals and their medical insurance charges.

Features:

| Feature | Description |
|---|---|
| age | Age of the individual |
| sex | Gender |
| bmi | Body Mass Index |
| children | Number of dependent children |
| smoker | Smoking status |
| region | Residential region |
| charges | Medical insurance cost (Target) |

## 🤖 Machine Learning Models

Three regression algorithms were implemented and compared:

1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor

### Model Performance

Evaluation results using 5-Fold Cross-Validation:

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 4209.91 | 6108.49 | 0.739 |
| Random Forest | 2667.40 | 4848.32 | 0.837 |
| Gradient Boosting | 2512.72 | 4585.04 | 0.853 |

**Best Model: Gradient Boosting Regressor**

Test-set performance:

| Metric | Score |
|---|---:|
| MAE | 2535.06 |
| RMSE | 4271.89 |
| R² | 0.90 |

These results are specific to the current dataset split and experiment.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/insurance-cost-predictor.git
```

### 2. Navigate to the project directory

```bash
cd insurance-cost-predictor
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

Mac/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL provided in your terminal, usually:

```text
http://localhost:8501
```

## 📁 Project Structure

```text
insurance-cost-predictor/
│
├── app.py
├── insurance_cost_predictor.ipynb
├── insurance.csv
├── insurance_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## 🔍 Model Insights

Feature importance analysis from the Gradient Boosting model indicated that:

- Smoking status was the most influential feature.
- BMI was another important predictive feature.
- Age also contributed significantly.
- Children, sex, and region had comparatively lower feature importance.

Feature importance reflects the trained model's predictive behaviour and does not establish causation.

## ⚠️ Disclaimer

This application provides experimental machine learning estimates for educational purposes only. Predictions are not actual insurance quotations, medical advice, or financial advice.

## 👨‍💻 Author

**Arnav Mhetre**

Computer Science Engineering Student | Machine Learning Enthusiast

GitHub: https://github.com/arnavmhetre1806-cmd

---

⭐ If you find this project interesting, consider giving it a star!