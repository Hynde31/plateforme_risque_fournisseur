
import streamlit as st
import pandas as pd

# Sample data for suppliers
data = {
    'Supplier': ['Supplier A', 'Supplier B', 'Supplier C'],
    'Country': ['France', 'Germany', 'USA'],
    'Risk Score': [0.2, 0.5, 0.8],
    'Risk Level': ['Low', 'Medium', 'High'],
    'Average Delay': [5, 10, 15],
    'Stock Level': [100, 50, 20],
    'Incidents': [1, 3, 5],
    'latitude': [48.8566, 52.5200, 37.7749],
    'longitude': [2.3522, 13.4050, -122.4194]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title('Supplier Risk Management Platform')

# Map visualization
st.map(df)

# Supplier selector
supplier = st.selectbox('Select a supplier:', df['Supplier'])

# Display supplier details
supplier_data = df[df['Supplier'] == supplier].iloc[0]
st.write(f"**Country:** {supplier_data['Country']}")
st.write(f"**Risk Score:** {supplier_data['Risk Score']}")
st.write(f"**Risk Level:** {supplier_data['Risk Level']}")
st.write(f"**Average Delay:** {supplier_data['Average Delay']} days")
st.write(f"**Stock Level:** {supplier_data['Stock Level']}")
st.write(f"**Incidents:** {supplier_data['Incidents']}")

# Dashboard
st.bar_chart(df[['Supplier', 'Risk Score']].set_index('Supplier'))
st.line_chart(df[['Supplier', 'Average Delay']].set_index('Supplier'))
st.area_chart(df[['Supplier', 'Stock Level']].set_index('Supplier'))
