# -*- coding: utf-8 -*-
"""
Spyder Editor

Makes the radar figure
"""


from math import pi
import matplotlib.pyplot as plt
import pandas as pd

# Get the data from the csv file
xl = pd.ExcelFile('./MD982181_CompletenessCheck.xlsx')
# Get the names of the excel sheets
cat = xl.sheet_names
# Get the values
evalues = []
rvalues = []
for c in cat:
    data = xl.parse(c)
    #filter essential
    df1 = data[(data['Recommendation']=='Essential')]
    evalues.append(df1['Provided on LinkedEarth'].sum()/df1.shape[0]*100)
    # filter recommended
    df2 = data[(data['Recommendation']=='Recommended')]
    rvalues.append(df2['Provided on LinkedEarth'].sum()/df2.shape[0]*100)

# Make the plot
fig = plt.figure(figsize=(8,4))
fig.subplots_adjust(wspace=0.45)

N = len(cat)
x_as = [n / float(N) * 2 * pi for n in range(N)]

# Because our chart will be circular we need to append a copy of the first
# value of each list at the end of each list with data
evalues += evalues[:1]
rvalues += rvalues[:1]
x_as += x_as[:1]

# Set color of axes
plt.rc('axes', linewidth=0.5, edgecolor="#888888")

# Create polar plot
ax1 = plt.subplot(121, polar=True)
# Set clockwise rotation. That is:
ax1.set_theta_offset(pi / 2)
ax1.set_theta_direction(-1)
# Set position of y-labels
ax1.set_rlabel_position(0)

# Set color and linestyle of grid
ax1.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
ax1.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)


# Set number of radial axes and remove labels
plt.xticks(x_as[:-1], [])

# Set yticks
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"])


# Plot data
ax1.plot(x_as, evalues, linewidth=0, linestyle='solid', zorder=3)

# Fill area
ax1.fill(x_as, evalues, 'b', alpha=0.3)

# Set axes limits
plt.ylim(0, 100)


# Draw ytick labels to make sure they fit properly
for i in range(N):
    angle_rad = i / float(N) * 2 * pi

    if angle_rad == 0:
        ha, distance_ax = "center", 10
    elif 0 < angle_rad < pi:
        ha, distance_ax = "left", 1
    elif angle_rad == pi:
        ha, distance_ax = "center", 1
    else:
        ha, distance_ax = "right", 1

    ax1.text(angle_rad, 100 + distance_ax, cat[i], size=10, horizontalalignment=ha, verticalalignment="center")
ax1.set_title('a. Essential',weight = 'bold',pad=15)

# Create polar plot
ax2 = plt.subplot(122, polar=True)
# Set clockwise rotation. That is:
ax2.set_theta_offset(pi / 2)
ax2.set_theta_direction(-1)
# Set position of y-labels
ax2.set_rlabel_position(0)

# Set color and linestyle of grid
ax2.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
ax2.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)


# Set number of radial axes and remove labels
plt.xticks(x_as[:-1], [])

# Set yticks
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"])


# Plot data
ax2.plot(x_as, rvalues, linewidth=0, linestyle='solid', zorder=3)

# Fill area
ax2.fill(x_as, rvalues, 'b', alpha=0.3)


# Set axes limits
plt.ylim(0, 100)


# Draw ytick labels to make sure they fit properly
for i in range(N):
    angle_rad = i / float(N) * 2 * pi

    if angle_rad == 0:
        ha, distance_ax = "center", 10
    elif 0 < angle_rad < pi:
        ha, distance_ax = "left", 1
    elif angle_rad == pi:
        ha, distance_ax = "center", 1
    else:
        ha, distance_ax = "right", 1

    ax2.text(angle_rad, 100 + distance_ax, cat[i], size=10, horizontalalignment=ha, verticalalignment="center")

ax2.set_title('b. Recommended', weight = 'bold',pad=15)

#Save polar plot
fig.savefig('./Figures/radar_plot.pdf')
