import pandas as pd
import altair as alt
import plotly.express as px
from vega_datasets import data
import streamlit as st

# Load and prepare the data
url = 'https://raw.githubusercontent.com/dataprofessor/dashboard-v3/master/data/us-population-2010-2019.csv'
df = pd.read_csv(url)

states_abbreviation = {  # Mapping of state names to abbreviations
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
    "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID",
    "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
    "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN",
    "Mississippi": "MS", "Missouri": "MO", "Montana": "MT", "Nebraska": "NE",
    "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM",
    "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH",
    "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI",
    "South Carolina": "SC", "South Dakota": "SD", "Tennessee": "TN",
    "Texas": "TX", "Utah": "UT", "Vermont": "VT", "Virginia": "VA",
    "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY",
    "District of Columbia": "DC", "American Samoa": "AS", "Guam": "GU",
    "Northern Mariana Islands": "MP", "Puerto Rico": "PR", 
    "United States Minor Outlying Islands": "UM", "U.S. Virgin Islands": "VI",
}

df['states_code'] = df['states'].map(states_abbreviation)

# Rearrange columns and reshape
columns_order = ['states', 'states_code', 'id', '2010', '2011', '2012', '2013', '2014', 
                 '2015', '2016', '2017', '2018', '2019']
df = df.reindex(columns=columns_order)

reshaped_df = pd.melt(
    df, id_vars=['states', 'states_code', 'id'], var_name='year', value_name='population'
)
reshaped_df['year'] = reshaped_df['year'].astype(int)
reshaped_df['population'] = reshaped_df['population'].str.replace(',', '').astype(int)

# Dashboard configuration
st.set_page_config(page_title="US Population Dashboard", page_icon="🏂", layout="wide")

# Sidebar
with st.sidebar:
    st.title('🏂 US Population Dashboard')
    year_list = sorted(reshaped_df['year'].unique(), reverse=True)
    selected_year = st.selectbox('Select a year', year_list)

    color_themes = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 
                    'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_themes)

# Filter data for selected year
filtered_df = reshaped_df[reshaped_df['year'] == selected_year]

# Plotting functions
def make_choropleth(data, theme):
    return px.choropleth(
        data, locations='states_code', locationmode='USA-states',
        color='population', scope='usa', color_continuous_scale=theme
    )

def make_heatmap(data, theme):
    return alt.Chart(data).mark_rect().encode(
        x='states:O',
        y='year:O',
        color=alt.Color('population:Q', scale=alt.Scale(scheme=theme))
    ).properties(width=900)

# Main content
col1, col2 = st.columns(2)

with col1:
    st.altair_chart(make_heatmap(reshaped_df, selected_color_theme), use_container_width=True)

with col2:
    st.plotly_chart(make_choropleth(filtered_df, selected_color_theme), use_container_width=True)
