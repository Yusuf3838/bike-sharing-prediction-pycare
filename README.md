# Bike-Sharing-Prediction-Regression-Pycaret
Abstract:
In this project, I used regression techniques to predict the total count of rental bikes (cnt) in a bike-sharing system using the "Bike Sharing Dataset." The dataset consists of hourly data containing 17,379 rows and 13 columns, with features such as season, year, month, hour, holiday, weekday, workingday, weather conditions (e.g., temperature, humidity, wind speed), and other time-related features. The target variable is the total bike rental count, excluding the casual and registered columns. I used the PyCaret regression module to automate the machine learning pipeline, which included data preprocessing, feature selection, model comparison, and evaluation. After cleaning the dataset by dropping the instant, dteday, casual, and registered columns, we identified the Random Forest Regressor model as the best performer. Among the models evaluated, including CatBoost, XGBoost, and LightGBM, the Random Forest Regressor demonstrated the most accurate predictions with an R² of 0.9401 and a mean absolute error (MAE) of 26.53. This model effectively forecasted bike rental demand based on environmental and time-based factors, showcasing the utility of PyCaret for efficient model selection and evaluation in predictive tasks.

1. Machine Learning Approaches to Bike-Sharing Systems: A Systematic Literature Review (İpek, S.; Balıkçı, A.; Özçift, A.)
Models: This paper reviewed various machine learning models applied to the Bike Sharing Dataset, including Random Forest, Support Vector Regression, Neural Networks, and others.
Performance: They found that tree-based models like Random Forest generally achieved the highest prediction accuracy, with R-squared values exceeding 0.9 in some cases. Support Vector Regression and Neural Networks also showed promising results.
Key Insights: The authors emphasized the importance of feature engineering and data preprocessing for achieving good performance. They also noted that the choice of performance metrics can significantly impact the evaluation and comparison of models.
https://www.researchgate.net/publication/348974351_Machine_Learning_Approaches_to_Bike-Sharing_Systems_A_Systematic_Literature_Review
2. Random Forest for Regression Analysis of Bike Sharing System (Sathishkumar V E, Jangwoo Park and Yongyun Cho)
Models: The paper focused on using Random Forest Regression to predict bike rental demand, comparing its performance with Linear Regression and Support Vector Regression.
Performance: The Random Forest model outperformed Linear Regression and Support Vector Regression, achieving higher accuracy and better generalization. They report an R2 value of 0.91 and MSE of 0.09.
Key Insights: The authors concluded that Random Forest is a robust and effective model for bike-sharing demand prediction, highlighting its ability to handle non-linear relationships and interactions between features.
https://www.researchgate.net/publication/339535558_Season_wise_bike_sharing_demand_analysis_using_random_forest_algorithm
3. Bike Sharing Demand Prediction Using Machine Learning (Mahesh Kumar M R, Gayathri P K and Shruthi R)
Models: This study explored several models, including Random Forest, Gradient Boosting, and Artificial Neural Networks, for predicting bike rental counts.
Performance: Random Forest and Gradient Boosting models achieved the best performance in terms of accuracy and computational efficiency.
Key Insights: The authors emphasized the importance of weather and temporal features in predicting bike-sharing demand. They also noted the importance of choosing the right performance metric to compare models.
https://www.researchgate.net/publication/377641378_Using_machine_learning_for_bike_sharing_demand_prediction
Overall Summary of Findings:
Tree-Based Models Dominate: Random Forest and Gradient Boosting consistently emerge as top performers across these studies. They achieve high prediction accuracy (R-squared values above 0.9) and handle the complexities of the bike-sharing data effectively.
Feature Engineering is Crucial: The quality and relevance of the features significantly impact model performance. Careful feature engineering, including creating new features and selecting the most relevant ones, is essential for achieving optimal results. Metric Selection Matters: Different performance metrics can lead to different conclusions when comparing models. Choosing a suitable metric that aligns with the goals of the prediction task is crucial. In these studies, metrics like R-squared, RMSE, and MAE were frequently used.

Relating to My Notebook:
My findings using XGBoost as the best model align well with the literature. XGBoost, similar to Random Forest and Gradient Boosting, is a tree-based ensemble method known for its ability to handle complex data and achieve high prediction accuracy.These papers reinforce the value of using PyCaret for tasks like bike-sharing demand prediction. By streamlining model comparison and evaluation, PyCaret enables you to quickly identify top-performing algorithms and build effective prediction models. 

Attributes Used for Estimation:
Here's a breakdown of the features used and their types:
Numerical Features:
hr: numerical - Hour of the day 
temp: numerical - Normalized temperature in Celsius.
atemp: numerical - Normalized feeling temperature in Celsius.
hum: numerical - Normalized humidity.
windspeed: numerical - Normalized wind speed.
Categorical Features:
season: categorical - Season (1:spring, 2:summer, 3:fall, 4:winter)
yr: categorical - Year (0: 2011, 1: 2012)
mnth: categorical - Month (1 to 12)
holiday: categorical - Whether the day is considered a holiday (0 or 1)
weekday: categorical - Day of the week (0 to 6)
workingday: categorical - If day is neither weekend nor holiday is 1, otherwise is 0.
weathersit: categorical - (1: Clear, Few clouds, Partly cloudy, Partly cloudy, 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist, 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds, 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog)
Dropped Columns and Reasons:
I dropped the following columns in my data preprocessing step:
instant: This column is simply a record index and does not provide any predictive information about bike rentals, making it irrelevant for the task.
dteday: This column represents the date. While it might seem relevant, you already have separate features for year (yr), month (mnth), holiday (holiday), and weekday (weekday), which capture the date-related information more effectively. Therefore, dteday becomes redundant.
casual: and registered: These columns represent the number of casual and registered users, respectively. While they are directly related to the total count (cnt), they are leakage features in this particular task of predicting the total rental count. If used, it would have given the model the value that is in fact a breakdown of the outcome, leading to overestimation and misleading performance.
Rationale for Feature Selection and Dropping:
Relevance: The selected features are likely to have a direct or indirect influence on bike rental demand.
Redundancy: Features like dteday were removed to avoid redundancy and potential multicollinearity issues.
Leakage: Dropping casual and registered prevents the model from learning patterns that wouldn't be available in a real-world prediction scenario, where you only have the total count (cnt) to predict.
By carefully selecting and preprocessing my features, I aim to build a robust and generalizable model that accurately predicts bike rental demand.


