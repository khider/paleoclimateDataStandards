#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:15:08 2018

@author: deborahkhider

This script goes over the responses to the survey in the Excel spreadsheet and
collates the responses over the various platforms

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap


#borrow a color palette
from pylab import *

cmap = cm.get_cmap('Dark2', 10)    # PiYG

color_scheme = []
for i in range(cmap.N):
    rgb = cmap(i)[:3] # will return rgba, we take only first 3 so we get rgb
    color_scheme.append(matplotlib.colors.rgb2hex(rgb))

# Borrow a second palette for the pie chart
cmap = cm.get_cmap('Set3', 10)
color_scheme2 = []
for i in range(cmap.N):
    rgb = cmap(i)[:3] # will return rgba, we take only first 3 so we get rgb
    color_scheme2.append(matplotlib.colors.rgb2hex(rgb))

# Other plot settings
# Bar plot
N = 3
ind = np.arange(N) #The x locations for the groups
width = 0.35 # The width of the bar
# Pie chart
colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0)  # explode 1st slice
labels = 'Essential', 'Recommended', 'Desired'

# Read the Excel file
xl = pd.ExcelFile('./Paleoclimate Data Standards Concatenated Reponses.xlsx')
# Get the names of the excel sheets
sheetNames = xl.sheet_names
#Open them one by one

for sheetName in sheetNames:
    data = xl.parse(sheetName)
    # Get the working group for the string
    if "_" in sheetName:
        n = sheetName.split("_")
        qual = n[1]
        if n[0] == "chronologies":
            arch = "chronologies"
        elif n[0] == "uncertainties":
            arch = "uncertainties"
        elif n[0] == "marine":
            arch = 'marine sediments archives'
        elif n[0] == 'lake':
            arch = 'lake sediments archives'
        else:
            arch = n[0] + " archives"
        if "foram" in qual:
            qual = qual.replace('foram','foraminiferal')
        if "geochem" in qual:
            qual = qual.replace('geochem','geochemistry')
        if "iso" in qual:
            qual = qual.replace('iso','isotope')
        if "micropaleo" in qual:
            qual = qual.replace('micropaleo','micropaleontological')
        if "mod cave condi" in qual:
            qual = qual.replace('mod cave condi','modern cave conditions')
        if "chron" in qual:
            qual = qual.replace('chron','chronologies')
    else:
        n = sheetName
        qual = ''
        if n == "chronologies":
            arch = "chronologies"
        elif n == "uncertainties":
            arch = "uncertainties"
        elif n == "marine":
            arch = 'marine sediments archives'
        elif n == 'lake':
            arch = 'lake sediments archives'
        else:
            arch = n + " archives"

    # Start the loop on each row into the sheet name
    for index in np.arange(0,data.shape[0]):
        # Place the question as a text

        if len(qual) == 0:
            textstr = 'When reporting datasets based on ' + arch + ', for ' + \
                    data['Dataset status'][index] + ', should the ' +\
                    data['Question'][index] + \
                    ' be considered essential, recommended or desired?'
        else:
            textstr = 'When reporting datasets based on ' + arch +\
                    ' ('+ qual+ '), for ' + \
                    data['Dataset status'][index] + ', should the ' +\
                    data['Question'][index] + \
                    ' be considered essential, recommended or desired?'

        # Gather the responses per platform and replace NaN by zero
        twitter = np.nan_to_num(np.array([data['Essential Twitter'][index], data['Recommended Twitter'][index],\
                   data['Desired Twitter'][index]])) #Twitter responses
        wiki = np.nan_to_num(np.array([data['Essential Wiki'][index], data['Recommended Wiki'][index],\
                   data['Desired Wiki'][index]])) #Wiki responses
        survey = np.nan_to_num(np.array([data['Essential Survey'][index], data['Recommended Survey'][index],\
                   data['Desired Survey'][index]])) #Survey responses

        barHeight=wiki+twitter # not elegant but need that sum for the bottom of the bar

        # Figure specification
        fig = plt.figure(figsize=(11,8))

        # Make the plot
        ax1 = plt.subplot2grid((12,3),(2,0),colspan=1, rowspan=10)
        p1 = ax1.bar(ind,wiki,width,color=color_scheme[6],label='Wiki')
        p2 = ax1.bar(ind,twitter,width,bottom=wiki,color=color_scheme[3],label='Twitter')
        p3 = ax1.bar(ind,survey,width,bottom=barHeight,color=color_scheme[0],label='Survey')

        # Pretty this thing up
        ax1.set_ylabel('Number of the votes')
        ax1.set_title('Votes per platform')
        ax1.set_xticks(ind)
        ax1.set_xticklabels(('Essential','Recommended','Desired'),rotation=45)
        ax1.legend()

        # Do the pie chart
        ax2 = plt.subplot2grid((12,3),(2,1), colspan=2, rowspan=10)
        # Get the data together
        tot_essential = twitter[0]+wiki[0]+survey[0]
        tot_recommended = twitter[1]+wiki[1]+survey[1]
        tot_desired = twitter[2]+wiki[2]+survey[2]

        sizes = [tot_essential,tot_recommended,tot_desired]

        # Plot
        ax2.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        #plt.tight_layout() #tight layouts help sometimes

        # Add the question as a title
        #plt.suptitle(textstr, wrap=True, fontsize=16, style = 'italic')
        plt.suptitle("\n".join(wrap(textstr,100)), wrap=True, fontsize=16, style = 'italic')


        #Save the figure as a PDF
        dirFig = './SuppFigures'
        if "/" in data['Question'][index]:
            question = data['Question'][index].replace('/','_')
        else:
            question = data['Question'][index]
        figName = sheetName+'_'+data['Dataset status'][index]+'_'+question
        #fig.savefig(dirFig+'/'+figName+'.pdf',bbox_inches='tight')
        fig.savefig(dirFig+'/'+figName+'.pdf')
