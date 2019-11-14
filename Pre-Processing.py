# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:41:25 2019

@author: Shayrin
"""

# pandas - to work with data frames
import pandas as pd 

# numpy- to work with numerical operations
import numpy as np

#==========================================================================================================
#==================READING DIFFERENT FILE FORMATS IN PYTHON ===============================================
#==========================================================================================================

#read an excel file
cars_data_xl=pd.read_excel('ToyotaCorollaNew.xlsx')


# read a text file
cars_data_txt=pd.read_table('ToyotaCorollaNew.txt')

# read a csv file
cars_data1=pd.read_csv('ToyotaCorollaNew.csv')

cars_data1=pd.read_csv('ToyotaCorollaNew.csv',index_col=0)

#deep copy
cars_data=cars_data1.copy()
#or
#cars_data1=cars_data.copy(deep=True)

# Attributes
cars_data.index
cars_data.columns
cars_data.size #no.of elements
cars_data.shape
#cars_data.memory_usage #in bytes
cars_data.ndim

#indexing
cars_data.head()#default 5
cars_data.tail()


#Data types-
cars_data.dtypes
cars_data.get_dtype_counts()

cars_data.info()

print(np.unique(cars_data['KM']))
print(np.unique(cars_data['HP']))
print(np.unique(cars_data['Doors']))


# =============================================================================
# IMPORTING DATA
# =============================================================================

# Importing data keeping the special categories in mind
cars_data=pd.read_csv('ToyotaCorollaNew.csv',index_col=0,
                      na_values=["??","????"])


print(np.unique(cars_data['KM']))
# Gives structure of data and no. of filled rows


#replacing three/four/five
cars_data['Doors'].replace('three',3,inplace=True)

cars_data['Doors'].value_counts()

cars_data['Doors'].where(cars_data['Doors']!='four',
         4,inplace=True)

cars_data['Doors']=np.where(cars_data['Doors']=='five',
         5,cars_data['Doors'])
cars_data['Doors'].value_counts()

cars_data['Doors']=cars_data['Doors'].astype('int64')
cars_data['Doors'].value_counts()

cars_data.info()

# Data type conversion
cars_data['MetColor']=cars_data['MetColor'].astype('object')

cars_data['Automatic']=cars_data['Automatic'].astype('object')
cars_data.info()

# statistical description

summary=cars_data.describe()
cars_data.describe(include="O")


describe=cars_data.describe(include="all")


# =============================================================================
# Imputing missing values
# =============================================================================


# To get missing values in each column straightaway

#cars_data.isna().sum()
#or
cars_data.isnull().sum()
# Take a look at the description to know whether numerical
# variables should be imputed with mean or median

# Mean and median of kilometer far away
# Therefore impute with median

# ==================== Replacing 'Age' with mean ==============================
cars_data['Age'].mean()
cars_data['Age'].fillna(cars_data['Age'].mean(),inplace = True)
cars_data['Age'].isnull().sum()

# ==================== Replacing 'KM' with median ==============================
cars_data['KM'].median()
cars_data['KM'].fillna(cars_data['KM'].median(),inplace = True)
cars_data['KM'].isnull().sum()

# ==================== Replacing 'HP' with mean ==============================
cars_data['HP'].mean()
cars_data['HP'].fillna(cars_data['HP'].mean(),inplace = True)
cars_data['HP'].isnull().sum()


# ==================== Replacing 'Fuel Type' with mode ========================

# Frequency table
cars_data['FuelType'].value_counts() 
# or
x=cars_data['FuelType'].mode()

# Using it for imputation
cars_data['FuelType'].fillna(cars_data['FuelType'].mode()[0],inplace = True)
cars_data['FuelType'].isnull().sum()

# ==================== Replacing 'MetColor' with mode ========================
# Frequency table
cars_data['MetColor'].value_counts() 
# or

# To get the mode value of Metcolor
cars_data['MetColor'].mode()

# To get categroy with maximum freq
# Index 0 will get the category
cars_data['MetColor'].mode()[0]cars_data['MetColor'].value_counts().index[0]

# replacing MetColor with mode
cars_data['MetColor'].fillna(cars_data['MetColor'].value_counts().index[0], inplace = True)

## Check for missing data after filling values 
print('Data columns with null values:\n', cars_data.isnull().sum())

# ==================== Imputation using lambda functionss ========================

# Fill all categorical variables at a stretch
cars_data = cars_data.apply(lambda x:x.fillna(x.value_counts().index[0]))
# Fill all numerical variables at a stretch
cars_data = cars_data.apply(lambda x:x.fillna(x.mean()))
print('Data columns with null values:\n', cars_data.isnull().sum())

# Fill numerical and categorial variables at one stretch

cars_data = cars_data.apply(lambda x:x.fillna(x.mean()) \
                              if x.dtype=='float' else \
                              x.fillna(x.value_counts().index[0]))

print('Data columns with null values:\n', cars_data.isnull().sum())

# =============================================================================
#     Visualization using matplotlib
# =============================================================================


import matplotlib.pyplot as plt

# =============================================================================
#     Histogram
# =============================================================================
plt.hist(cars_data['Age'],
         color = 'blue',
         edgecolor = 'white',
         bins =5,
         orientation='vertical')
plt.show()
# for any bin value, the minor tick lables remains the same
# only the no.of bars changes


# =============================================================================
# SCATTER PLOT
# =============================================================================
plt.scatter(cars_data['Age'],
        cars_data['Price'],
        c='BLUE', )
plt.title('Scatter PLot')
plt.xlabel('Age')
plt.ylabel('Price')
plt.show()


 
# =============================================================================
# Visualization using Seaborn Package
# =============================================================================
import seaborn as sns

#1. ***** Basic scatter plot *****#
sns.regplot(x=cars_data['Price'], y=cars_data['Age'])
 
# Without regression fit:
sns.regplot(x=cars_data['Price'], y=cars_data['Age'], 
            fit_reg=False)




# =============================================================================
# Box plot
# =============================================================================
#1. Box plot for a numerical varaible
sns.boxplot(y=cars_data["Price"] )
sns.plt.show()

#2. Box plot for categorical variable vs.numerical variable
sns.boxplot(x = cars_data['Doors'], y = cars_data["Price"])
sns.plt.show()

#3. Box plot for multiple numerical varaibles
sns.boxplot(data = cars_data.ix[:,0:4])
sns.plt.show()

#4. Grouped boxplot
sns.boxplot(x="FuelType",  y = cars_data["Price"], 
            hue="Automatic", data=cars_data, palette="Set2")
sns.plt.show()

# =============================================================================
# Histogram
# =============================================================================
# 1. histogram of HP
sns.distplot(cars_data['HP'] )
sns.plt.show()
 
# 2. histogram without density curve
sns.distplot(cars_data['HP'], hist=True, kde=False)
sns.plt.show()

# 3. fixing the number of bins
sns.distplot(cars_data['HP'], bins=5 )
sns.plt.show()

# 4. Boxplot and histogram on the same page 
# Cut the window in 2 parts
f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
 
# Add two graphs now!
sns.boxplot(cars_data["Price"], ax=ax_box)
sns.distplot(cars_data["Price"], ax=ax_hist, kde = False)
 
# Remove x axis name for the boxplot
ax_box.set(xlabel='')

# =============================================================================
# Bar PLot
# =============================================================================
sns.set(style="darkgrid")

ax = sns.countplot(x="FuelType", data=cars_data)
ax = sns.countplot(x="FuelType", data=cars_data, hue = "Automatic")
ax = sns.countplot(y="FuelType", data=cars_data, hue = "Automatic")
ax = sns.countplot(x="FuelType", data=cars_data, palette="Set2")
# =============================================================================
#
# ============================================================================

# =============================================================================
# END OF SCRIPT
# =============================================================================
