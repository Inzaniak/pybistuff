from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# PARAMETERS (EDIT) ##############################
color_l1 = '#118dff'
color_l2 = '#6b007b'
color_l3 = '#e044a7'

l1_data = dataset['ValueA']
l2_data = dataset['ValueB']
l3_data = dataset['ValueC']

x_label = "Date"
l1_label = "Value A"
l2_label = "Value B"
l3_label = "Value C"
label_density = 10
########################################################

# CHART PARAMETERS ##############################
host = host_subplot(111, axes_class=AA.Axes)

par1 = host.twinx()
par2 = host.twinx()

offset = 60
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par1.axis["right"] = new_fixed_axis(loc="right", axes=par1,
                                        offset=(0, 0))
par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                        offset=(offset, 0))

par2.axis["right"].toggle(all=True)


host.set_xlabel(x_label)
host.set_ylabel(l1_label)
par1.set_ylabel(l2_label)
par2.set_ylabel(l3_label)
plt.tight_layout(pad=4, w_pad=0, h_pad=0)

# DATE MANAGEMENT ##############################
dates = matplotlib.dates.date2num(pd.to_datetime(dataset['Date'],format='%Y/%m/%d'))
dataset['DateT'] = pd.to_datetime(dataset['Date'],format='%Y/%m/%d')
dataset['DateFormat'] = dataset['DateT'].dt.strftime('%d/%m/%Y')

# MISSING DATA ##############################
s1mask = np.isfinite(l1_data)
s2mask = np.isfinite(l2_data)
s3mask = np.isfinite(l3_data)

# X AXIS ##############################
plt.xticks(dates[s1mask][::label_density], dataset['DateFormat'][s1mask][::label_density], rotation='vertical')

# Y AXIS ##############################
p1, = host.plot(dates[s1mask], l1_data[s1mask], label=l1_label, marker="o", linestyle="dotted", color = color_l1)
p2, = par1.plot(dates[s2mask], l2_data[s2mask], label=l2_label, marker="X", linestyle="dashed", color = color_l2)
p3, = par2.plot(dates[s3mask], l3_data[s3mask], marker="d", color = color_l3, label=l3_label)

# LEGEND ##############################
host.legend()

# AXIS COLORS ##############################
host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(color_l3)

# PRINT PLOT ##############################
plt.draw()
plt.show()
