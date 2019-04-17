#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 14:54:37 2018

@author: deborahkhider

This makes a particular figure for the main manuscript using the same question
for a legacy and a new dataset.
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

# Get the two textstrings
textstr = 'For new datasets, should the depth/distance/position in the'+\
            ' archive be considered essential, recommended, or desired?'
#textstr = 'For legacy datasets, should the depth/distance/position in the'+\
#            ' archive be considered essential, recommended, or desired?'

# Get the data for new datasets (E,R,D)
twitter = np.array([11,2,2])
wiki = np.array([22,5,0])
survey = np.array([64,20,8])

#Get the data for the legacy datasets (E, R,D)
#twitter = np.array([3,1,1])
#wiki = np.array([5,2,0])
#survey = np.array([46,30,12])

barHeight=wiki+twitter # not elegant but need that sum for the bottom of the bar
#figure specification
fig = plt.figure(figsize=(7.5,6))
# Make the plot
ax1 = plt.subplot2grid((12,3),(1,0),colspan=1, rowspan=11)
p1 = ax1.bar(ind,wiki,width,color=color_scheme[6],label='Wiki')
p2 = ax1.bar(ind,twitter,width,bottom=wiki,color=color_scheme[3],label='Twitter')
p3 = ax1.bar(ind,survey,width,bottom=barHeight,color=color_scheme[0],label='Survey')

# Pretty this thing up
ax1.set_ylabel('Number of votes', fontsize=10)
ax1.set_title('Votes per platform')
ax1.set_xticks(ind)
ax1.set_xticklabels(('Essential','Recommended','Desired'),rotation=30, fontsize=10)
ax1.legend()

# Do the pie chart
ax2 = plt.subplot2grid((12,3),(1,1), colspan=2, rowspan=11)
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
plt.suptitle("\n".join(wrap(textstr,100)), wrap=True, fontsize=14, style = 'italic')

#Save the figure as a PDF
dirFig = './Figures'
fig.savefig(dirFig+'/'+'STD_newDataset.pdf')
#fig.savefig(dirFig+'/'+'STD_legacyDataset.pdf')
