# Bike-Sharing-Prediction-Regression-Pycaret 👋🚲

---
## Abstract
In this project, I used regression techniques to predict the total count of rental bikes (`cnt`) in a bike-sharing system using the "Bike Sharing Dataset." The dataset consists of hourly data containing 17,379 rows and 13 columns, with features such as season, year, month, hour, holiday, weekday, workingday, weather conditions (e.g., temperature, humidity, wind speed), and other time-related features. 

The PyCaret regression module was utilized to automate the machine learning pipeline, including:
- Data preprocessing
- Feature selection
- Model comparison and evaluation

After cleaning the dataset by dropping irrelevant columns, the CatBoost Regressor emerged as the best performer with:
- **R²**: 0.9490
- **Mean Absolute Error (MAE)**: 25.2830

This project showcases the utility of PyCaret in identifying top-performing models for predictive tasks.

Dataset: https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset

---

## Key Findings from Literature
### 1. Machine Learning Approaches to Bike-Sharing Systems: A Systematic Literature Review
- **Models**: Random Forest, Support Vector Regression, Neural Networks
- **Key Insight**: Tree-based models like Random Forest excelled in prediction accuracy (R² > 0.9).

[Read More](https://www.researchgate.net/publication/348974351_Machine_Learning_Approaches_to_Bike-Sharing_Systems_A_Systematic_Literature_Review)

### 2. Random Forest for Regression Analysis of Bike Sharing System
- **Models**: Random Forest vs. Linear Regression vs. SVR
- **Performance**: Random Forest achieved **R² = 0.91**.

[Read More](https://www.researchgate.net/publication/339535558_Season_wise_bike_sharing_demand_analysis_using_random_forest_algorithm)

### 3. Bike Sharing Demand Prediction Using Machine Learning
- **Models**: Random Forest, Gradient Boosting, Neural Networks
- **Key Insight**: Weather and temporal features are crucial for accuracy.

[Read More](https://www.researchgate.net/publication/377641378_Using_machine_learning_for_bike_sharing_demand_prediction)

---

## Relating to My Notebook
The results of my notebook align closely with findings in the literature:
- Tree-based models like XGBoost and CatBoost were among the top performers.
- PyCaret simplified the comparison of multiple models, validating its value for efficient experimentation.

---

## Attributes Used for Estimation
### **Numerical Features**
- `hr`: Hour of the day
- `temp`: Normalized temperature
- `atemp`: Normalized feeling temperature
- `hum`: Normalized humidity
- `windspeed`: Normalized wind speed

### **Categorical Features**
- `season`: Season (1: spring, 2: summer, etc.)
- `yr`: Year (0: 2011, 1: 2012)
- `mnth`: Month (1-12)
- `holiday`: Holiday indicator (0 or 1)
- `weekday`: Day of the week (0-6)
- `workingday`: Working day indicator (0 or 1)
- `weathersit`: Weather situation (1-4)

### **Dropped Columns**
- `instant`: Index, irrelevant for prediction.
- `dteday`: Redundant due to other time-related features.
- `casual` and `registered`: Leakage features for this task.

---
### ***Graphs***

<img width="789" alt="1" src="https://github.com/user-attachments/assets/1ecdf7ee-b7cb-41b8-a81e-60ab3f0791c9">

<img width="763" alt="2" src="https://github.com/user-attachments/assets/2b6ae3e5-f65f-457d-afd3-eb673328e2b4">

<img width="740" alt="3" src="https://github.com/user-attachments/assets/403ecb4b-5e89-462f-afd7-4393dd37cf1c">

<img width="533" alt="4" src="https://github.com/user-attachments/assets/0beaa9bd-ef0f-4ee1-864c-67cc98f0eda0">

<img width="814" alt="5" src="https://github.com/user-attachments/assets/dbc03d22-27f8-4a32-9324-59aa40240989">

<img width="1563" alt="6" src="https://github.com/user-attachments/assets/8808e6e7-2d2d-4079-86d0-844066acfe32">

---
### ***How To Use This Repository***
- Clone the repository: git clone https://github.com/Yusuf3838/bike-sharing-prediction-pycare.git
- Install dependencies: pip install -r requirements.txt
- Open and run the notebook: Use Jupyter or Google Colab to run the included notebook for detailed analysis.
- Run using Docker (optional): docker build -t bike-sharing-prediction 
---

## Conclusion
This project demonstrates the utility of PyCaret for bike-sharing demand prediction. The CatBoost Regressor was the standout model, showcasing its ability to handle complex data efficiently. Future exploration will involve deeper feature engineering and expanding the analysis to other datasets.




