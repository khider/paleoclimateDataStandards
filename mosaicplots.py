#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 12:42:40 2018

@author: deborahkhider

Manipulate the data of survey answers for various plots

"""

## First figure out the most answered question on all platforms

import pandas as pd
import numpy as np
from colormap import rgb2hex

#open the Excel file and dump the content
xl = pd.ExcelFile('./Paleoclimate Data Standards Concatenated Reponses.xlsx')
# Get the names of the excel sheets
sheetNames = xl.sheet_names

choice = ["essential","recommended","desired"]

# Set the counters to zero
count_twitter = 0
count_wiki = 0
count_survey = 0

# Set the placeholder to empty
twitter_sheet = ''
wiki_sheet = ''
survey_sheet = ''

twitter_question = ''
wiki_question = ''
survey_question =''

for sheetName in sheetNames:
    # Get the data in pandas dataframe for each sheet
    data = xl.parse(sheetName)
    # Loop around each row in the dataframe
    for index in np.arange(0,data.shape[0]):
        twitter_tot = np.sum(np.nan_to_num(np.array([data['Essential Twitter'][index],\
                                          data['Recommended Twitter'][index],\
                                          data['Desired Twitter'][index]]))) #Twitter responses
        wiki_tot = np.sum(np.nan_to_num(np.array([data['Essential Wiki'][index],\
                                          data['Recommended Wiki'][index],\
                                          data['Desired Wiki'][index]]))) #Wiki responses
        survey_tot = np.sum(np.nan_to_num(np.array([data['Essential Survey'][index],\
                                          data['Recommended Survey'][index],\
                                          data['Desired Survey'][index]]))) #Wiki responses

        ## Compare and update
        # Twitter
        if twitter_tot>count_twitter:
            count_twitter = twitter_tot
            twitter_sheet = sheetName
            twitter_question = data['Dataset status'][index] + ', '+ data['Question'][index]

        # Wiki
        if wiki_tot>count_wiki:
            count_wiki = wiki_tot
            wiki_sheet = sheetName
            wiki_question = data['Dataset status'][index] + ', '+ data['Question'][index]

        # survey
        if survey_tot>count_survey:
            count_survey = survey_tot
            survey_sheet = sheetName
            survey_question = data['Dataset status'][index] + ', '+ data['Question'][index]

#%% Make the mosaic plot

import pandas as pd
import numpy as np
from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt
from colormap import rgb2hex

#open the Excel file and dump the content
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

# Replace historical documents by docs
df1 = new_dataframe.replace('historical documents', 'docs')
# Make sure that a recommended appears before a desired (trick for the plot)
df1['rec'][12] = 'recommended'
df1['rec'][24] = 'desired'
df2 = legacy_dataframe.replace('historical documents', 'docs')
# Create the color coding scheme
def colorCode(key):
    if 'cross' in key:
        if "essential" in key:
            scheme = {'color':rgb2hex(44,160,44)}
        elif "desired" in key:
            scheme = {'color':rgb2hex(152,223,138)}
        elif "recommended" in key:
            scheme = {'color':rgb2hex(103,191,92)}
    elif 'docs' in key:
        if "essential" in key:
            scheme = {'color':rgb2hex(148,103,189)}
        elif "desired" in key:
            scheme = {'color':rgb2hex(197,176,213)}
        elif "recommended" in key:
            scheme = {'color':rgb2hex(173,139,201)}
    elif 'ice core' in key:
        if "essential" in key:
            scheme = {'color':rgb2hex(23,190,207)}
        elif "desired" in key:
            scheme = {'color':rgb2hex(158,218,229)}
        elif "recommended" in key:
            scheme = {'color':rgb2hex(109,204,218)}
    elif 'lake' in key:
        if "essential" in key:
            scheme = {'color':rgb2hex(31,119,180)}
        elif "desired" in key:
            scheme = {'color':rgb2hex(174,199,232)}
        elif "recommended" in key:
            scheme = {'color':rgb2hex(114,158,206)}
    elif 'marine' in key:
        if "essential" in key:
            scheme = {'color':rgb2hex(140,86,75)}
        elif "desired" in key:
            scheme = {'color':rgb2hex(196,156,148)}
        elif "recommended" in key:
            scheme = {'color':rgb2hex(168,120,110)}
    elif 'MARPA' in key:
        if "essential" in key:
            scheme = {'color':rgb2hex(214,39,40)}
        elif "desired" in key:
            scheme = {'color':rgb2hex(255,152,150)}
        elif "recommended" in key:
            scheme = {'color':rgb2hex(237,102,93)}
    elif 'speleothem' in key:
        if "essential" in key:
            scheme = {'color':rgb2hex(255,127,14)}
        elif "desired" in key:
            scheme = {'color':rgb2hex(255,187,120)}
        elif "recommended" in key:
            scheme = {'color':rgb2hex(255,158,74)}
    elif 'trees' in key:
        if "essential" in key:
            scheme = {'color':rgb2hex(188,189,34)}
        elif "desired" in key:
            scheme = {'color':rgb2hex(219,219,141)}
        elif "recommended" in key:
            scheme = {'color':rgb2hex(205,204,93)}
    elif 'chronologies' in key:
        if "essential" in key:
            scheme = {'color':rgb2hex(227,119,194)}
        elif "desired" in key:
            scheme = {'color':rgb2hex(247,182,210)}
        elif "recommended" in key:
            scheme = {'color':rgb2hex(237,151,202)}
    elif 'uncertainties' in key:
        if "essential" in key:
            scheme = {'color':rgb2hex(127,127,127)}
        elif "desired" in key:
            scheme = {'color':rgb2hex(199,199,199)}
        elif "recommended" in key:
            scheme = {'color':rgb2hex(162,162,162)}
    return  scheme

def letterCode(key):
#    if recs[key][1]==1:
#        letter = ""
#    else:
    if "essential" in key:
        letter = "e"
    elif "recommended" in key:
        letter = "r"
    elif "desired" in key:
        letter = "d"
    return letter

# Make the figure
#props = lambda key: colorCode(key)
props = lambda k: colorCode(k)
#fig, rects =  mosaic(data, ['WG','rec'], title='Mosaic Plot _ no freqs')

fig, recs = mosaic(df1, ['WG','rec'], title='Recommendation for new datasets', \
       properties = props, gap=0.015)

labels = lambda k: letterCode(k) if recs[k][1] !=1 else ""
fig, ax  = plt.subplots(figsize=(7.5, 3.5))
mosaic(df1, ['WG','rec'], title='a. Recommendation for new datasets', \
       properties = props, gap=0.015, ax=ax,labelizer=labels)

for tick in ax.get_xticklabels():
    tick.set_rotation(30)
    tick.set_horizontalalignment('right')
for tick in ax.get_yticklabels():
    tick.set_rotation(30)

plt.savefig('./Figures/new_datasets_rec.png',\
            dpi =300, bbox_inches='tight', pad_inches=0.25)

# Legacy datasets

fig, recs =  mosaic(df2, ['WG','rec'], title='Recommendation for legacy datasets', \
       properties = props, gap=0.015)
fig, ax  = plt.subplots(figsize=(7.5, 3.5))
labels = lambda k: letterCode(k) if recs[k][1] !=1 else ""
mosaic(df2, ['WG','rec'], title='b. Recommendation for legacy datasets', \
       properties = props, gap=0.015, ax=ax,labelizer=labels )

for tick in ax.get_xticklabels():
    tick.set_rotation(30)
    tick.set_horizontalalignment('right')
for tick in ax.get_yticklabels():
    tick.set_rotation(30)

plt.savefig('./Figures/legacy_datasets_rec.png',\
            dpi =300, bbox_inches='tight', pad_inches=0.25)
