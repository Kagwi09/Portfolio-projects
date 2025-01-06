import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# Load company logo
image_url = "https://raw.githubusercontent.com/username/repository/branch/path/to/jamwi_logo.jpg"

# Display the image in the sidebar
st.sidebar.image(image_url, caption="Jamwi Building Contractors", use_column_width=True)

def run():
    # Sidebar navigation menu
    with st.sidebar:
        selected_app = option_menu(
            menu_title="Project Menu",
            options=["Introduction", "Project Gallery", "Total Project Costs",
                     "Labor Costs", "Material Costs", "KPI's"],
            icons=["house", "image", "cash", "people", "bricks", "clipboard-data"],  # Ensure valid Bootstrap icons
            menu_icon="cast",  # Optional icon for the sidebar menu
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": "#fafafa"},
                "icon": {"color": "blue", "font-size": "20px"},
                "nav-link": {"color": "black", "font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "lightblue"},
                "nav-link-selected": {"background-color": "#00bfae"},
            }
        )
    
    # Display content based on the selected menu item
    if selected_app == "Introduction":
        st.write("Welcome to the project dashboard!")
    elif selected_app == "Project Gallery":
        st.write("Here is the project gallery.")
    elif selected_app == "Total Project Costs":
        st.write("Total project costs overview.")
    elif selected_app == "Labor Costs":
        st.write("Details about labor costs.")
    elif selected_app == "Material Costs":
        st.write("Breakdown of material costs.")
    elif selected_app == "KPI's":
        st.write("Key Performance Indicators for the project.")

# Run the app
run()
