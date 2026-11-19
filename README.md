# Diabetes Prediction Using Machine Learning

## 1. Project Overview
An end-to-end machine learning project that classifies diabetes status as Diabetes or No Diabetes using demographic, family history, lifestyle, dietary and health-related features.

The project covers data analysis, preprocessing, feature selection, model building, hyperparameter tuning, evaluation and deployment using Streamlit.

**Note:** This application is developed for educational purposes only and is not a medical diagnostic tool.

## 2. Dataset Description
- **Source:** [Kaggle – Diabetes Dataset](https://www.kaggle.com/datasets/datascikhan/diabetes)
- **Original records:** 100,000
- **Original features:** 209 columns
- **Sample used:** 20,000 records
- **Selected predictors:** 20
- **Target variable:** `diabetes_status`
  - 0 – No Diabetes
  - 1 – Diabetes

## 3. Project Workflow
1. Exploratory Data Analysis (EDA)
2. Data cleaning and missing value treatment
3. Feature selection
4. Categorical encoding and numerical scaling
5. Train-test splitting
6. Baseline model building
7. Hyperparameter tuning using GridSearchCV
8. Model evaluation and comparison
9. Model saving using Joblib
10. Deployment using Streamlit

## 4. Machine Learning Algorithms
- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)

## 5. Model Evaluation

The models were evaluated using Accuracy, Precision, Recall, F1-score and ROC-AUC.

| Model | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Logistic Regression | 81.40% | 78.80% | 45.84% | 57.97% |
| Decision Tree | 70.25% | 46.85% | 47.18% | 47.02% |
| Random Forest | 81.15% | 79.20% | 44.24% | 56.77% |
| KNN | 75.38% | 57.94% | 43.70% | 49.82% |

**Selected Model:** Tuned Logistic Regression.

It was selected based on its overall performance, including the highest accuracy, F1-score and ROC-AUC among the tuned models.

## 6. Streamlit Application
An interactive application was developed using Streamlit. Users can enter the selected input features and obtain a model classification.

To run the application locally:

```bash
python -m streamlit run app.py
```

## 7. Project Structure

```text
ML_Diabetes_Project/
│
├── data/
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   └── 03_Model_Building.ipynb
│
├── models/
│   └── diabetes_model.pkl
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 8. Limitations
- The model is developed for educational purposes.
- The prediction is based on the selected dataset and features.
- The model has limited recall for the Diabetes class, meaning some positive cases may be missed.
- The output should not be used for medical diagnosis or treatment decisions.
