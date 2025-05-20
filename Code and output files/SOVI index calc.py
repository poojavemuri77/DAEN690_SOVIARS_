#!/usr/bin/env python
# coding: utf-8

# # SOVI Index Calculation
# 

# In[1]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


#Load the Data
social_df = pd.read_csv("/Users/poojavemuri/Downloads/SOVIAR 2025/Social_data.csv")
economic_df = pd.read_csv("/Users/poojavemuri/Downloads/SOVIAR 2025/Economic_data.csv")
demographic_df = pd.read_csv("/Users/poojavemuri/Downloads/SOVIAR 2025/Demographic_data.csv")
housing_df = pd.read_csv("/Users/poojavemuri/Downloads/SOVIAR 2025/Housing_data.csv")

#Clean and Prepare the Data

# Clean Social Data
social_df['Male_HH_Kids'] = social_df['Male_HH_Kids'].str.replace(',', '').astype(float)
social_df['Female_HH_Kids'] = social_df['Female_HH_Kids'].str.replace(',', '').astype(float)
social_df = social_df.drop(['Bachelors_or_higher_PE', 'housing_cost_burden'], axis=1)
social_df.head()



# In[2]:


social_df.info()


# In[3]:


# Clean Economic Data
economic_df['Blw_Pov_Lvl_PE'] = economic_df['Blw_Pov_Lvl_PE'].astype(float)
economic_df['Unemployment_PE'] = economic_df['Unemployment_PE'].astype(float)
economic_df = economic_df.drop(['Total_population', 'Govt_Assistance', 'Govt_Assistance_PE','Med_Inc_H'], axis=1)
economic_df.head()


# In[4]:


# Clean Demographic Data
#economic_df['Total_population'] = economic_df['Total_population'].astype(float)
demographic_df = demographic_df.drop(['White', 'American Indian and Alaska Native', 'Asian', 'Native Hawaiian and Other Pacific Islander', 'Some Other Race'], axis=1)
demographic_df.head()
demographic_df.info()


# In[5]:


# Clean Housing Data
housing_df['No_Vehicle_PE'] = housing_df['No_Vehicle_PE'].astype(float)
housing_df = housing_df.drop(['Area Per Sq Mile','Poplation Density per sq mile','Owner occupied','Renter occupied','Structured Built before 1980','Total Structured Build','Built 1970 to 1979', 'Built 1960 to 1969' , 'Built 1950 to 1959', 'Built 1940 to 1949', 'Built 1939 or earlier'], axis=1)
housing_df.head()
housing_df.info()


# In[7]:


# Define weights for each sub-index
weights = {
    "social": 0.35,
    "economic": 0.30,
    "demographic": 0.20,
    "housing": 0.15
}

# Function to normalize and apply weights
def process_index(df, var_weights):
    scaler = MinMaxScaler()
    df_scaled = df.copy()
    
    # Normalize all numerical columns
    numeric_cols = [col for col in df.columns if col not in ["Fips_code", "Municipality"]]
    df_scaled[numeric_cols] = scaler.fit_transform(df_scaled[numeric_cols])
    
    # Apply weights
    weighted_scores = []
    for var, weight in var_weights.items():
        if var in df_scaled.columns:
            weighted_scores.append(df_scaled[var] * weight)

    
    
    # Compute sub-index score
    df_scaled["Sub_Index_Score"] = sum(weighted_scores)
    return df_scaled[["Municipality", "Sub_Index_Score"]]


# In[8]:


# Define variable weights for each dataset
social_weights = {
    "Male_HH_Kids": 0.10,
    "Female_HH_Kids": 0.15,
    "HS_Grad_or_Higher_PE": 0.10,
    "Disability < 18": 0.10,
    "Disability 18-64": 0.15,
    "Disability 65+": 0.20,
    "Broadband_access_per": 0.20
}

economic_weights = {
    "Unemployment_PE": 0.40,
    "Blw_Pov_Lvl_PE": 0.60
}

demographic_weights = {
    "Male": 0.05,
    "Female": 0.15,
    "Under 5 years": 0.30,
    "65 years and over": 0.30,
    "Black or African American": 0.20
}

housing_weights = {
    "Total Housing Units": 0.10,
    "Percentage of Units Built Before 1980": 0.15,
    "Owner_Percentage": 0.05,
    "Renter_Percentage": 0.30,
    "No_Vehicle_PE": 0.25,
    "No_Phone_percentage": 0.15
}


# In[9]:


# Process each index
social_index = process_index(social_df, social_weights)
economic_index = process_index(economic_df, economic_weights)
demographic_index = process_index(demographic_df, demographic_weights)
housing_index = process_index(housing_df, housing_weights)

# Merge all indices
sovi_df = social_index.merge(economic_index, on="Municipality", suffixes=("_social", "_economic")) \
                      .merge(demographic_index, on="Municipality") \
                      .merge(housing_index, on="Municipality", suffixes=("_demographic", "_housing"))

# Compute final SOVI score
sovi_df["SOVI"] = (
    (weights["social"] * sovi_df["Sub_Index_Score_social"]) +
    (weights["economic"] * sovi_df["Sub_Index_Score_economic"]) +
    (weights["demographic"] * sovi_df["Sub_Index_Score_demographic"]) +
    (weights["housing"] * sovi_df["Sub_Index_Score_housing"])
)

# Save the output
sovi_df.to_csv("SOVI_index.csv", index=False)
print(sovi_df.head())


# In[10]:


import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the SOVI_index.csv file
df = pd.read_csv("SOVI_index.csv")


# Sort by normalized SOVI score and select top 10 municipalities
top_10 = df.sort_values(by="SOVI", ascending=False).head(10)

# Plot
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.barplot(x="SOVI", y="Municipality", data=top_10, palette="viridis")
plt.title("Top 10 Most Vulnerable Municipalities by SOVI Score", fontsize=16)
plt.xlabel("SOVI Score", fontsize=12)
plt.ylabel("Municipality", fontsize=12)
plt.xlim(0, 1)  # Ensure x-axis ranges from 0 to 1
plt.show()


# In[11]:


import matplotlib.pyplot as plt

# Data
labels = ["Social", "Economic", "Demographic", "Housing"]
sizes = [0.35, 0.30, 0.20, 0.15]
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]

# Plot
plt.figure(figsize=(2, 2))
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
plt.title("Distribution of Weights Across Sub-Indices", fontsize=8)
plt.axis("equal")  # Equal aspect ratio ensures the pie is circular.
plt.show()


# In[12]:


import matplotlib.pyplot as plt

# Data for each sub-index
sub_indices = {
    "Social": {
        "Male Households with Kids": 0.10,
        "Female Households with Kids": 0.15,
        "High School Graduation Rate": 0.10,
        "Disability (<18)": 0.10,
        "Disability (18-64)": 0.15,
        "Disability (65+)": 0.20,
        "Broadband Access": 0.20,
    },
    "Economic": {
        "Below Poverty Level (%)": 0.60,
        "Unemployment Rate (%)": 0.40,
    },
    "Demographic": {
        "Male Population (%)": 0.05,
        "Female Population (%)": 0.15,
        "Population Under 5 Years (%)": 0.30,
        "Population 65+ Years (%)": 0.30,
        "Black or African American (%)": 0.20,
    },
    "Housing": {
        "Total Housing Units": 0.10,
        "Percentage of Units Built Before 1980": 0.15,
        "Owner-Occupied Housing (%)": 0.05,
        "Renter-Occupied Housing (%)": 0.30,
        "No Vehicle Access (%)": 0.25,
        "No Phone Access (%)": 0.15,
    },
}

# Create a figure with 4 subplots (one for each sub-index)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Distribution of Weights Across Sub-Indices and Variables", fontsize=14)

# Colors for pie charts
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6", "#c2f0c2"]

# Plot pie charts for each sub-index
for i, (sub_index, variables) in enumerate(sub_indices.items()):
    ax = axes[i // 2, i % 2]  # Position in the 2x2 grid
    labels = list(variables.keys())
    sizes = list(variables.values())
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors[:len(labels)])
    ax.set_title(f"{sub_index} Sub-Index", fontsize=12)

# Adjust layout

plt.tight_layout()
plt.show()


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("SOVI_index.csv")

# Categorize SOVI scores
bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
labels = ['Very Low', 'Low', 'Medium', 'High', 'Very High']
df['Vulnerability Category'] = pd.cut(df['SOVI'], bins=bins, labels=labels, include_lowest=True)

# 1. Bar Plot of Category Distribution
plt.figure(figsize=(10, 6))
category_counts = df['Vulnerability Category'].value_counts().sort_index()
sns.barplot(x=category_counts.index, y=category_counts.values, palette="YlOrRd_r")
plt.title("Distribution of Municipalities by Vulnerability Level", fontsize=16)
plt.xlabel("Vulnerability Category", fontsize=12)
plt.ylabel("Number of Municipalities", fontsize=12)
plt.show()

# 2. Top 10 Municipalities by Category
top_10 = df.nlargest(10, 'SOVI')
plt.figure(figsize=(10, 6))
sns.barplot(x='SOVI', y='Municipality', hue='Vulnerability Category', 
            data=top_10, palette="YlOrRd_r", dodge=False)
plt.title("Top 10 Most Vulnerable Municipalities", fontsize=16)
plt.xlabel("SOVI Score", fontsize=12)
plt.ylabel("Municipality", fontsize=12)
plt.legend(title='Vulnerability Level')
plt.show()


# In[ ]:




