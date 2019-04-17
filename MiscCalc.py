#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:34:58 2018

@author: deborahkhider

Misc: Standard ms misc calculations
"""

#%% Number of essential/recommended/desired questions
import pandas as pd
import numpy as np

# Read the Excel file
xl = pd.ExcelFile('./Paleoclimate Data Standards Concatenated Reponses.xlsx')
# Get the names of the excel sheets
sheetNames = xl.sheet_names
#Open them one by one and count
count = 0
for sheetName in sheetNames:
    data = xl.parse(sheetName)
    count =  count + data.shape[0]

#%% Percentage of questions answered as recommended/essential/desired
import pandas as pd
import numpy as np

# Read the Excel file
xl = pd.ExcelFile('./Paleoclimate Data Standards Concatenated Reponses.xlsx')
# Get the names of the excel sheets
sheetNames = xl.sheet_names

# Broad categories: Cross-archive, Archive-Specific, Uncertainties, Chronologies
# Arrays contain the count for Essential, Recommended, Desired in that order
new_archiveType =[]
legacy_archiveType = []
new_rec = []
legacy_rec = []

choice = ["essential","recommended","desired"]

for sheetName in sheetNames:
    data = xl.parse(sheetName)
    # Get the type of archive from the sheet name
    if "_" in sheetName:
        n = sheetName.split("_")
        archiveType = n[0]
    else:
        archiveType = sheetName
    # Flip through each property and determined if it's essential, recommended or desired
    for index in np.arange(0,data.shape[0]):

        # Gather the responses per platform and replace NaN by zero
        twitter = np.nan_to_num(np.array([data['Essential Twitter'][index], data['Recommended Twitter'][index],\
                   data['Desired Twitter'][index]])) #Twitter responses
        wiki = np.nan_to_num(np.array([data['Essential Wiki'][index], data['Recommended Wiki'][index],\
                   data['Desired Wiki'][index]])) #Wiki responses
        survey = np.nan_to_num(np.array([data['Essential Survey'][index], data['Recommended Survey'][index],\
                   data['Desired Survey'][index]])) #Survey responses

        # add them up
        total = twitter+wiki+survey
        # pick the final answer
        max_val = np.max(total)
        if max_val == 0:
            ans ='desired'
        else:
            idx = np.argmax(total)
            ans = choice[idx]

        # Update the recommendation + archiveType counters
        if 'new' in data['Dataset status'][index]:
            new_archiveType.append(archiveType)
            new_rec.append(ans)
        else:
            legacy_archiveType.append(archiveType)
            legacy_rec.append(ans)

# Concatenate the answers into panda dataframes
new_dataframe = pd.DataFrame({'WG':new_archiveType,'rec':new_rec})
legacy_dataframe = pd.DataFrame({'WG':legacy_archiveType,'rec':legacy_rec})
# Calculate the number of essential/recommended/desired across all platforms
new_rec = new_dataframe.groupby('rec').size()
leg_rec = legacy_dataframe.groupby('rec').size()
# Print out the recommendations:
print('New datasets Recommendation: ')
for item in choice:
    print(item+": "+str(new_rec[item]))
    print(item+": "+str(new_rec[item]/new_dataframe.shape[0]*100)+"%")

print('Legacy datasets Recommendation: ')
for item in choice:
    print(item+": "+str(leg_rec[item]))
    print(item+": "+str(leg_rec[item]/legacy_dataframe.shape[0]*100)+"%")

# Number of questions from each working group
new_dataframe.groupby('rec').size()
legacy_dataframe.groupby('rec').size()

# Number of answers from each WG
WGs = new_dataframe['WG'].unique()
print('New Datasets: ')
for WG in WGs:
    # filter
    temp = new_dataframe.loc[new_dataframe['WG']==WG]
    print(WG)
    print(temp.groupby('rec').size())

print('legacy Datasets: ')
for WG in WGs:
    # filter
    temp = legacy_dataframe.loc[legacy_dataframe['WG']==WG]
    print(WG)
    print(temp.groupby('rec').size())
