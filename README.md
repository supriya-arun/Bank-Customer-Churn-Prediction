**Bank Customer Churn Prediction**
========

![exit_img](https://github.com/user-attachments/assets/308f7ca4-d3db-4255-a37c-7cf8a3de01e8)


*Project Overview:* 
--------
This project aims to develop a machine learning model to predict bank customer churn. Customer churn, also known as customer attrition, refers to the phenomenon where customers stop doing business with a company or switch to a competitor. By identifying potential churners in advance, banks can take proactive measures to retain valuable customers and minimize revenue loss. This repository provides a comprehensive solution for predicting customer churn using various machine learning algorithms.

*Data Source:*
--------
The dataset used for this project can be obtained from Kaggle.
It contains relevant customer information such as demographics, account activity and Exit status.

*Implementation Details:*
--------
Methods Used:  
Machine Learning  
Data Visualization  
Exploratory Data Analysis  
Predictive Modeling  
Python  
Jupyter  
streamlit  

*Python Packages Used:* 
--------
Data Manipulation: Pandas, numpy  
Data Visualization: seaborn, matplotlib  
Data Preprocessing: imblearn  
Machine Learning: scikit, xgboost  


*Steps Followed:* 
--------
Data collection: Obtained the customer churn dataset from Source Dataset Link.  
Exploratory Data Analysis (EDA): Performed the comprehensive exploratory analysis to gain insights into the dataset, identify patterns, correlations, and potential predictive features.  
Data Preprocessing: Cleansed the data, handled categorical values, normalized the data, and addressed imbalanced data.  
Model Development: Implemented and trained various machine learning algorithms such as logistic regression, decision trees, random forests, and XGB.  
Model Evaluation: Assessed the performance of each model using metrics such as accuracy, precision, recall, F1-score. Selected the best-performing model for deploymet.  
Deployment: Deployed the chosen churn prediction model as a standalone application to enable real-time predictions for new customer data.  

*Results and Evaluation Criterion* 
--------

Based on the evaluation results, the best-performing model was XGBoost which achieved an accuracy of 99%.

*Future Improvements:* 
--------
Here are some potential areas for future improvements in the project:
Real-time monitoring: Implement a system to monitor and retrain the model periodically to adapt to changing customer dynamics.
User interface enhancement: Improve the user interface of the deployed application for better user experience.
