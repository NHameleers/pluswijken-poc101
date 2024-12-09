import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.title("Pluswijken Wijkscan")
'LET OP: Dit is een prototype in ontwikkeling dat gebruikt maakt van fictieve data'


wijken = ['Kerkrade Rolduckerveld',
          'Eijsden']

wijk = st.selectbox('Selecteer uw wijk', options=wijken)

# Data for the chart
valuedict = {'Kerkrade Rolduckerveld': [15, 9, 6, 15, 5, 5, 5, 15, 15],
             'Eijsden': [7, 2, 5, 9, 4, 3, 2, 3, 3]}
labels = ["Eigen kracht en persoonlijke sociale basis",
                "Gemiddeld aantal uur mantelzorg geven per week",
                "Percentage zeer eenzaam",
            "Gemeenschappelijke sociale basis",
                "Child B1",
                "Child B2",
                "Child B3",
            "Zorg en welzijn",
                "Child C1"]
parents = ["",
                "Eigen kracht en persoonlijke sociale basis",
                "Eigen kracht en persoonlijke sociale basis",
            "",
                "Gemeenschappelijke sociale basis",
                "Gemeenschappelijke sociale basis",
                "Gemeenschappelijke sociale basis",
            "",
                "Zorg en welzijn"]
values = valuedict[wijk]

# Create the Sunburst chart
fig = go.Figure(go.Sunburst(
    labels=labels,
    parents=parents,
    values=values,
    branchvalues="total",  # Use "total" or "remainder" for value computation
    sort=False,  # Ensure consistent positioning
    # marker=dict(
    #     colors=values,  # Use values to determine the color intensity
    #     colorscale="RdYlGn"  # Use a predefined color scale
    # )
))

fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

# Display the chart in Streamlit
st.plotly_chart(fig)


'## Alternatieve weergave'

treemap_df = pd.DataFrame({
    "Category": parents,  # Parent category
    "Subcategory": labels,  # Child category
    "Values": values  # Values
})
treemap_df = treemap_df.loc[treemap_df['Category'] != "", ]

# Plot the Treemap
fig = px.treemap(
    treemap_df,
    path=["Category", "Subcategory"],  # Define hierarchy
    values="Values",  # Sizes of rectangles
    color="Values",  # Use values to set color intensity
    # color_continuous_scale="RdYlGn"
)

# Update layout
fig.update_layout(margin=dict(t=30, l=0, r=0, b=0))

# Display the chart in Streamlit
st.plotly_chart(fig)

'## Overwegingen'

'''Let op: Voor beide weergaven geldt het volgende:
Normaal gesproken laat een taartdiagram of een treemap de proporties zien van bepaalde onderdelen.
De ene taartpunt kan dan groter zijn dan de andere.
In het voorbeeld dat we eerder zagen van GGD Hollands midden zijn de afmetingen van de taartpunten echter vastgezet (https://eengezonderhollandsmidden.nl/ghm-profieltaart.aspx).
Het zijn daar de kleuren en de tooltips die de informatie over de waarden geven.'''
