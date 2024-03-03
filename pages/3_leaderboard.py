import streamlit as st
import matplotlib.pyplot as plt

# Data for the bars
labels = ['Jackson', 'Sneha', 'Guniet']
values = [10, 7, 5]
colors = ['green', 'blue', 'orange']  # Specify the colors for each bar

# Plotting the bar graph
fig, ax = plt.subplots()
bars = ax.bar(range(len(labels)), values, color=colors, edgecolor='black', linewidth=1)

# Adding text labels on top of the bars
ax.bar_label(bars, labels=labels, fontsize='large', color='black', fontweight='bold')

# Adding labels
ax.set_ylabel('Points')
ax.set_xlabel('Top 3')

# Set the background color to white
ax.set_facecolor('white')

# Remove unnecessary chart elements
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Set the x-axis ticks and labels
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(['1', '2', '3'])  # Change labels to '1', '2', '3'

# Display the plot in Streamlit
st.pyplot(fig)
