# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:30:43 2019

@author: GITAA
"""
# =============================================================================
# MULTIPLE LINEAR REGRESSION
# =============================================================================
####################### Required modules #######################

# Pandas - to work with dataframes
import pandas as pd

# Numpy - to work with numerical computations
import numpy as np



# =============================================================================
# IMPORTING DATA
# =============================================================================
data = pd.read_csv('cleaned_toyota.csv')


######TO GET RID OF THE SI.NO COLUMN
data = pd.read_csv('cleaned_toyota.csv',index_col=0)


#"""
#Exploratory data analysis:
#
#1.Data information (types and missing value) and statistics
#2.Data preprocessing (Missing value,handling categorical variables etc)
#3.Data visualization
#"""
# ==================== To get data information ================================
print(data.info()) 


######## CHECK FOR THE MISSING VALUES
data.isnull().sum()



# ==================== To get 5 number summary and counts================================
summary=(data.describe()) 


data.head()

data.tail()



# =============================================================================
# CORRELATION
# =============================================================================

# Finding the correlation between numerical variables
correlation = data.corr()
print(correlation)

import seaborn as sns
sns.heatmap(correlation)


sns.pairplot(data, kind="scatter")

# =============== Regression modeling starts from here ========================
# =============================================================================
# DUMMY VARIABLE ENCODING
# =============================================================================
# =============================================================================
# =============================================================================
# Convert string into dummy variable

data=pd.get_dummies(data,drop_first=True) 
# drop_first => whether to get k-1 dummies out of k categorical levels by 
# removing the level which is less in frequency.


# Storing the column names in variables 
features = list(set(data.columns)-set(['Price']))
target   = list(['Price'])

print(features)
print(target)

# =============================================================================

x = data.loc[:, features]   
y = data.loc[:,target]     

# Sklearn - package to split data into train & test
from sklearn.model_selection import train_test_split


# Splitting test & train as 30% and 70%


train_x, test_x, train_y, test_y = train_test_split(x,y,
                                                    test_size=0.3,
                                                    random_state=40)

######################MULTIPLE LINEAR REGRESSION###########################################

# statsmodels to build linear regression model
import statsmodels.formula.api as smf


Model=smf.OLS(train_y,train_x).fit()
Model.summary()


predictions = Model.predict(test_x) # make the predictions by the model


# finding the mean for test data value
base_pred = np.mean(test_y)
print(base_pred)

# Repeating same value till length of test data
base_pred = np.repeat(base_pred, len(test_y))

# finding the RMSE
from sklearn.metrics import mean_squared_error
base_RMSE =(mean_squared_error(test_y,base_pred))**0.5                            
print(base_RMSE)

# RMSE of the linear model
lr_rmse = (mean_squared_error(test_y,predictions))**0.5

print(lr_rmse)


# =============================================================================
# END OF SCRIPT
# =============================================================================
