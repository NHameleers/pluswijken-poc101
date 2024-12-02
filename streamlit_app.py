import streamlit as st
import plotly.graph_objects as go

st.title("Pluswijken Wijkscan")

wijken = ['Kerkrade Rolduckerveld',
          'Eijsden']

wijk = st.selectbox('Selecteer uw wijk', options=wijken)

# Data for the chart
valuedict = {'Kerkrade Rolduckerveld': [10, 4, 6, 8, 3, 3, 2],
             'Eijsden': [7, 2, 5, 9, 4, 3, 2]}
labels = ["Eigen kracht en persoonlijke sociale basis", "Child A1", "Child A2", "Gemeenschappelijke sociale basis", "Child B1", "Child B2", "Child B3"]
parents = ["", "Eigen kracht en persoonlijke sociale basis", "Eigen kracht en persoonlijke sociale basis", "", "Gemeenschappelijke sociale basis", "Gemeenschappelijke sociale basis", "Gemeenschappelijke sociale basis"]
values = valuedict[wijk]

# Create the Sunburst chart
fig = go.Figure(go.Sunburst(
    labels=labels,
    parents=parents,
    values=values,
    branchvalues="total",  # Use "total" or "remainder" for value computation
    sort=False  # Ensure consistent positioning
))

fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

# Display the chart in Streamlit
st.plotly_chart(fig)
