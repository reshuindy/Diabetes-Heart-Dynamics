import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
csv_path = "/Users/utkarsh/Desktop/Atlas data download/ATLAS Concept Sets _source code.csv"

try:
    data = pd.read_csv(csv_path)
    st.success("CSV file loaded successfully!")
except FileNotFoundError:
    st.error(f"File not found: {csv_path}")
    st.stop()

# Title of the Streamlit app
st.title("Atlas Concepts Visualization")

# Display the raw data
st.header("Raw Data")
st.write(data)

# Visualization: Count of Concepts by Class
st.header("Count of Concepts by Class")
class_counts = data['Class'].value_counts().reset_index()
class_counts.columns = ['Class', 'Count']
fig1 = px.bar(class_counts, x='Class', y='Count', title="Count of Concepts by Class")
st.plotly_chart(fig1)

# Visualization: Count of Concepts by Domain
st.header("Count of Concepts by Domain")
domain_counts = data['Domain'].value_counts().reset_index()
domain_counts.columns = ['Domain', 'Count']
fig2 = px.bar(domain_counts, x='Domain', y='Count', title="Count of Concepts by Domain")
st.plotly_chart(fig2)

# Visualization: Standard vs Non-Standard Concepts
st.header("Standard vs Non-Standard Concepts")
standard_counts = data['Standard Concept Caption'].value_counts().reset_index()
standard_counts.columns = ['Standard Concept Caption', 'Count']
fig3 = px.pie(standard_counts, values='Count', names='Standard Concept Caption', title="Standard vs Non-Standard Concepts")
st.plotly_chart(fig3)

# Visualization: Concepts by Vocabulary
st.header("Concepts by Vocabulary")
vocab_counts = data['Vocabulary'].value_counts().reset_index()
vocab_counts.columns = ['Vocabulary', 'Count']
fig4 = px.bar(vocab_counts, x='Vocabulary', y='Count', title="Concepts by Vocabulary")
st.plotly_chart(fig4)

# Filter data by Domain
st.header("Filter Data by Domain")
selected_domain = st.selectbox("Select a Domain", data['Domain'].unique())
filtered_data = data[data['Domain'] == selected_domain]
st.write(filtered_data)
