
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/dashboard-v3/master/data/us-population-2010-2019.csv')

states_abbreviation = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}
df['states_code'] = [states_abbreviation[x] for x in df.states]


new_columns = ['states', 'states_code', 'id', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
       '2017', '2018', '2019']
df = df.reindex(columns=new_columns)

path = r"C:\Users\MWANGI\Desktop\us-population-2010-2019-states-code.csv"
df.to_csv(path, index=False)

df_reshaped = pd.melt(df, id_vars=['states', 'states_code', 'id'], var_name='year', value_name='population')

df_reshaped['states'] = df_reshaped['states'].astype(str)
df_reshaped['year'] = df_reshaped['year'].astype(int)
df_reshaped['population'] = df_reshaped['population'].str.replace(',', '').astype(int)

path2 = r"C:\Users\MWANGI\Desktop\us-population-2010-2019-reshaped.csv"
df_reshaped.to_csv(path2)

selected_year = 2019
df_selected_year = df_reshaped[df_reshaped.year == selected_year]

df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)

def calculate_population_difference(input_df, input_year):
  selected_year_data = input_df[input_df['year'] == input_year].reset_index()
  previous_year_data = input_df[input_df['year'] == input_year - 1].reset_index()
  selected_year_data['population_difference'] = selected_year_data.population.sub(previous_year_data.population, fill_value=0)
  selected_year_data['population_difference_absolute'] = abs(selected_year_data['population_difference'])
  return pd.concat([selected_year_data.states, selected_year_data.id, selected_year_data.population, selected_year_data.population_difference, selected_year_data.population_difference_absolute], axis=1).sort_values(by="population_difference", ascending=False)

df_population_difference_sorted = calculate_population_difference(df_reshaped, selected_year)

df_greater_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference_absolute > 50000]

import altair as alt

alt.themes.enable("dark")
# Change the theme to "dark", applying dark backgrounds and lighter text colors to charts.


heatmap = alt.Chart(df_reshaped).mark_rect().encode(
        y=alt.Y('year:O', axis=alt.Axis(title="Year", titleFontSize=16, titlePadding=15, titleFontWeight=900, labelAngle=0)),
        x=alt.X('states:O', axis=alt.Axis(title="States", titleFontSize=16, titlePadding=15, titleFontWeight=900)),
        color=alt.Color('max(population):Q',
                         legend=alt.Legend(title=" "),
                         scale=alt.Scale(scheme="blueorange")),
        stroke=alt.value('black'),
        strokeWidth=alt.value(0.25),
        #tooltip=[
        #    alt.Tooltip('year:O', title='Year'),
        #    alt.Tooltip('population:Q', title='Population')
        #]
    ).properties(width=900
    #).configure_legend(orient= 'bottom', titleFontSize=16, labelFontSize=14, titlePadding=0
    ).configure_axisX(labelFontSize=14).configure_axis(
    labelFontSize=12,
    titleFontSize=12
    )

heatmap

# %%
# Choropleth via Altair
import altair as alt
from vega_datasets import data

alt.themes.enable("dark")

states = alt.topo_feature(data.us_10m.url, 'states')

alt.Chart(states).mark_geoshape().encode(
    color=alt.Color('population:Q', scale=alt.Scale(scheme='blues')),   # scale=color_scale
    stroke=alt.value('#154360')
).transform_lookup(
    lookup='id',
    from_=alt.LookupData(df_selected_year, 'id', list(df_selected_year.columns))
).properties(
    width=500,
    height=300
).project(
    type='albersUsa'
)

import altair as alt
from vega_datasets import data

# Load dataset
cars = data.cars()

# Create a scatter plot
chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color='Origin:N'
).properties(
    width=600,
    height=400
)

# Display the chart
chart


# %%
# Choropleth via Plotly
import plotly.express as px

choropleth = px.choropleth(df_selected_year, locations='states_code', color='population', locationmode="USA-states",
                               color_continuous_scale='blues',
                               range_color=(0, max(df_selected_year.population)),
                               scope="usa",
                               labels={'population':'Population'}
                              )
choropleth.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=350
    )

choropleth

import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_title="US Population Dashboard", # page_title: Sets the browser tab title to "US Population Dashboard."
    page_icon="🏂", # page_icon: Displays a snowboard emoji as the page icon.
    layout="wide", # layout: Uses a wide layout for better visual spacing.
    initial_sidebar_state="expanded") # initial_sidebar_state: Expands the sidebar by default.



alt.themes.enable("dark") # alt.themes.enable("dark"): Activates the dark theme for Altair visualizations.

st.markdown(
    """
    <style>
    [data-testid="block-container"] {
        padding-left: 2rem;
        padding-right: 2rem;
        padding-top: 1rem;
        padding-bottom: 0rem;
        margin-bottom: -7rem;
    }

    [data-testid="stVerticalBlock"] {
        padding-left: 0rem;
        padding-right: 0rem;
    }

    [data-testid="stMetric"] {
        background-color: #393939;
        text-align: center;
        padding: 15px 0;
    }

    [data-testid="stMetricLabel"] {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    [data-testid="stMetricDeltaIcon-Up"] {
        position: relative;
        left: 38%;
        -webkit-transform: translateX(-50%);
        -ms-transform: translateX(-50%);
        transform: translateX(-50%);
    }

    [data-testid="stMetricDeltaIcon-Down"] {
        position: relative;
        left: 38%;
        -webkit-transform: translateX(-50%);
        -ms-transform: translateX(-50%);
        transform: translateX(-50%);
    }
    </style>
    """,
    unsafe_allow_html=True, # enables the injection of raw HTML and CSS. Without this, the custom styling would not be applied.
)
 


#######################
# Load data
df_reshaped = pd.read_csv(path2)


#######################
# Sidebar
with st.sidebar: # Contains two interactive widgets:

    st.title('🏂 US Population Dashboard')
    
    year_list = list(df_reshaped.year.unique())[::-1]
    
    
    selected_year = st.selectbox('Select a year', year_list)
    # Year Selection (st.selectbox): Allows users to select a year. The data is filtered based on the selected year.
    
    df_selected_year = df_reshaped[df_reshaped.year == selected_year]
    df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']

    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
    # Color Theme Selection (st.selectbox): Lets users choose a color theme for the visualizations.


#######################
# Plots

# Heatmap
def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    # Plots population data by year and state using a color-coded grid.
    # Encodes data as rectangular cells, where colors represent population values.
    heatmap = alt.Chart(input_df).mark_rect().encode(
            y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
            x=alt.X(f'{input_x}:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
            color=alt.Color(f'max({input_color}):Q',
                             legend=None,
                             scale=alt.Scale(scheme=input_color_theme)),
            stroke=alt.value('black'),
            strokeWidth=alt.value(0.25),
        ).properties(width=900
        ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
        ) 
    # height=300
    return heatmap

# Choropleth map
def make_choropleth(input_df, input_id, input_column, input_color_theme):
    # Visualizes state-level population on a U.S. map.
    # Uses states_code for mapping and applies the selected color theme.
    choropleth = px.choropleth(input_df, locations=input_id, color=input_column, locationmode="USA-states",
                               color_continuous_scale=input_color_theme,
                               range_color=(0, max(df_selected_year.population)),
                               scope="usa",
                               labels={'population':'Population'}
                              )
    choropleth.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=350
    )
    return choropleth


# Donut chart
def make_donut(input_response, input_text, input_color):
    # Displays inbound and outbound migration percentages.
    # Uses color-coding to differentiate between high and low migration.
  if input_color == 'blue':
      chart_color = ['#29b5e8', '#155F7A']
  if input_color == 'green':
      chart_color = ['#27AE60', '#12783D']
  if input_color == 'orange':
      chart_color = ['#F39C12', '#875A12']
  if input_color == 'red':
      chart_color = ['#E74C3C', '#781F16']
    
  source = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100-input_response, input_response]
  })
  source_bg = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100, 0]
  })
    
  plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          #domain=['A', 'B'],
                          domain=[input_text, ''],
                          # range=['#29b5e8', '#155F7A']),  # 31333F
                          range=chart_color),
                      legend=None),
  ).properties(width=130, height=130)
    
  text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
  plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          # domain=['A', 'B'],
                          domain=[input_text, ''],
                          range=chart_color),  # 31333F
                      legend=None),
  ).properties(width=130, height=130)
  return plot_bg + plot + text

# Convert population to text 
def format_number(num):
    # format_number: Converts large numbers into a more readable format (e.g., 2 M for 2 million).
    if num > 1000000:
        if not num % 1000000:
            return f'{num // 1000000} M'
        return f'{round(num / 1000000, 1)} M'
    return f'{num // 1000} K'


# Calculation year-over-year population migrations
def calculate_population_difference(input_df, input_year):
    # calculate_population_difference: Computes year-over-year population changes for each state.
  selected_year_data = input_df[input_df['year'] == input_year].reset_index()
  previous_year_data = input_df[input_df['year'] == input_year - 1].reset_index()
  selected_year_data['population_difference'] = selected_year_data.population.sub(previous_year_data.population, fill_value=0)
  return pd.concat([selected_year_data.states, selected_year_data.id, selected_year_data.population, selected_year_data.population_difference], axis=1).sort_values(by="population_difference", ascending=False)


#######################
# Dashboard Main Panel

col = st.columns((1.5, 4.5, 2), gap='medium')
# The main dashboard consists of three columns, each focusing on specific aspects of the data:

with col[0]:
    # Column 1: Gains/Losses and Migration
    # Gains/Losses: Shows metrics for states with the largest population gain and loss.
    st.markdown('#### Gains/Losses')

    df_population_difference_sorted = calculate_population_difference(df_reshaped, selected_year)

    if selected_year > 2010:
        first_state_name = df_population_difference_sorted.states.iloc[0]
        first_state_population = format_number(df_population_difference_sorted.population.iloc[0])
        first_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[0])
    else:
        first_state_name = '-'
        first_state_population = '-'
        first_state_delta = ''
    st.metric(label=first_state_name, value=first_state_population, delta=first_state_delta)

    if selected_year > 2010:
        last_state_name = df_population_difference_sorted.states.iloc[-1]
        last_state_population = format_number(df_population_difference_sorted.population.iloc[-1])   
        last_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[-1])   
    else:
        last_state_name = '-'
        last_state_population = '-'
        last_state_delta = ''
    st.metric(label=last_state_name, value=last_state_population, delta=last_state_delta)

    
    st.markdown('#### States Migration')
    # Migration: Displays donut charts showing the percentage of states with significant inbound and outbound migration 
    # (> 50,000).
   

    if selected_year > 2010:
        # Filter states with population difference > 50000
        # df_greater_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference_absolute > 50000]
        df_greater_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference > 50000]
        df_less_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference < -50000]
        
        # % of States with population difference > 50000
        states_migration_greater = round((len(df_greater_50000)/df_population_difference_sorted.states.nunique())*100)
        states_migration_less = round((len(df_less_50000)/df_population_difference_sorted.states.nunique())*100)
        donut_chart_greater = make_donut(states_migration_greater, 'Inbound Migration', 'green')
        donut_chart_less = make_donut(states_migration_less, 'Outbound Migration', 'red')
    else:
        states_migration_greater = 0
        states_migration_less = 0
        donut_chart_greater = make_donut(states_migration_greater, 'Inbound Migration', 'green')
        donut_chart_less = make_donut(states_migration_less, 'Outbound Migration', 'red')

    migrations_col = st.columns((0.2, 1, 0.2))
    with migrations_col[1]:
        st.write('Inbound')
        st.altair_chart(donut_chart_greater)
        st.write('Outbound')
        st.altair_chart(donut_chart_less)

with col[1]:
    st.markdown('#### Total Population')
     # 2: Total Population
    # Choropleth Map: Highlights state-wise population for the selected year.
    # Heatmap: Compares population trends across years and states.
    
    choropleth = make_choropleth(df_selected_year, 'states_code', 'population', selected_color_theme)
    st.plotly_chart(choropleth, use_container_width=True)
    
    heatmap = make_heatmap(df_reshaped, 'year', 'states', 'population', selected_color_theme)
    st.altair_chart(heatmap, use_container_width=True)
    

with col[2]:
    st.markdown('#### Top States')
    # Column 3: Top States
    # Data Table: Lists states sorted by population, with a progress bar for visualization.
    # "About" Section: Provides metadata and source links for the dashboard.

    st.dataframe(df_selected_year_sorted,
                 column_order=("states", "population"),
                 hide_index=True,
                 width=None,
                 column_config={
                    "states": st.column_config.TextColumn(
                        "States",
                    ),
                    "population": st.column_config.ProgressColumn(
                        "Population",
                        format="%f",
                        min_value=0,
                        max_value=max(df_selected_year_sorted.population),
                     )}
                 )
    
    with st.expander('About', expanded=True):
        st.write('''
            - Data: [U.S. Census Bureau](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html).
            - :orange[**Gains/Losses**]: states with high inbound/ outbound migration for selected year
            - :orange[**States Migration**]: percentage of states with annual inbound/ outbound migration > 50,000
            ''')



# %%
st.write('Hello world')


