import streamlit as st
import matplotlib.pyplot as plt

# Create a section for the pie chart
st.header("Nutrients in Chocolate")

# Define the data for the pie chart
labels = ['Fat', 'Carbohydrates', 'Protein', 'Fiber', 'Sugar']
sizes = [35, 45, 10, 5, 5]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc00', '#663300']

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart
st.pyplot(fig)