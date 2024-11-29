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

![image](https://github.com/user-attachments/assets/c4922334-135e-437e-a660-055f76cfff48)

![image](https://github.com/user-attachments/assets/a6b4ed8b-9918-4e93-b200-3d851cb68230)

![image](https://github.com/user-attachments/assets/6ecfe6fd-d05d-4c7d-bd6c-c174e74290f8)

![image](https://github.com/user-attachments/assets/f65873c2-275c-4e8b-aaa6-ca61a433148a)

![image](https://github.com/user-attachments/assets/33568644-37ff-4c4d-b6db-71157b8215a6)

![image](https://github.com/user-attachments/assets/bfb9857f-23c7-4ca7-a151-ecacb553e6e2)

![image](https://github.com/user-attachments/assets/c908ac88-61af-4274-a3c8-d71d1721a568)

![image](https://github.com/user-attachments/assets/d8693025-39d3-45c3-b0b0-4e0c062ea819)


---
### ***How To Use This Repository***
- Clone the repository: git clone https://github.com/Yusuf3838/bike-sharing-prediction-pycare.git
- Install dependencies: pip install -r requirements.txt
- Open and run the notebook: Use Jupyter or Google Colab to run the included notebook for detailed analysis.
---

## Conclusion
This project demonstrates the utility of PyCaret for bike-sharing demand prediction. The CatBoost Regressor was the standout model, showcasing its ability to handle complex data efficiently. Future exploration will involve deeper feature engineering and expanding the analysis to other datasets.




