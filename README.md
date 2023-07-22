# Ecommerce Shipping Data
Final Project Miracle7 Team on Data Science: Machine Learning Specialization Program Rakamin Academy Batch 31 </br>
- Data: [E-Commerce Shipping Data](https://www.kaggle.com/datasets/prachi13/customer-analytics)
- Tools: Jupyter Notebook
- Library: Numpy, Pandas, Matplotlib, Seaborn, Scipy, Scikit-learn

## Bakground
An international e-commerce company that sells electronic products wants to discover key insights from its customer database. From the data, the on-time delivery rate is as low as 40% potentially increasing the churn rate and potential revenue loss. So the company uses a machine learning model that can predict whether delivery will be late or not as an effort to increase the on-time delivery rate.

## Exploratory Data Analysis
- The data consist of 12 data features with 10,999 rows
- Warehouses with both high and low capacity have the same percentage of delays.
- Most late products are a combination of high discount and light weighted goods (under 4 kgs)

## Data preprocessing
- Handling data: No missing and duplicated data
- Feature Extraction: weight class, frequent buy, price class, discount class, frequent call
- Feature Encoding: One Hot Encoding, Label Encoding
- Feature Selection: chi-square test
- Class Imbalance: Balanced data

## Machine Learning Modelling Evaluation
Models conducted in this experiment:
- Decision Tree
- KNN
- Adaboost
- XGBoost
- Random Forest
- CATBoost

From the models above we choose XGBoost as the best fit model which has the highest recall score after hyperparameter tuning of 98%. Also 97% recall cross-validation training and testing data.

## Recommendation
Recommendation of important attributes to gather to have a better understanding of the existing data and enhance the machine learning model.
- Order, shipping, and arrival date
- Type of the products
- Distance (geolocation)

Periodically evaluate machine learning model and order processing flow from order entry until it arrives at the customer to produce new, more specific solutions until standard on-time delivery of 90% is reached.

## Root-cause Analysis
After gathering more important attributes like order, shipping, and arrival date, we recommend doing a root-cause analysis to address the possible problem that happened in the order processing process or logistics.

Recommend collaborating with a fulfillment center or third-party logistics because can solve on-time delivery rate and low-cost compared to other recommendations.

## Business Metric Analysis
Implementing preventive measures of order prioritization on predicted late deliveries could boost on-time delivery rates by 10%, and also applying repressive measures to customers who might leave could reduce churn rates by 15% and reduce potential revenue loss by 25%.

## Contributor
- [Fawwaz Nurmansyah](https://www.linkedin.com/in/fawwaz-nurmansyah/)
- [Nabila Putri Ananda](https://www.linkedin.com/in/nabilaputriananda/)
- [Abiyyu Tsani](https://www.linkedin.com/in/abiyyutsany/)
- [Lutfi Santoso](https://www.linkedin.com/in/lutfisantoso/)
- [Bayu Suwandhika](https://www.linkedin.com/in/bayusuw/)


