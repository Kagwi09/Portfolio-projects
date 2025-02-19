import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from project_gallery_2 import run_project_gallery
from introduction_1 import run_introduction  # <- ADD THIS
st.set_page_config(layout="wide")


# Corrected image URL (direct raw link from GitHub)
image_url = "https://raw.githubusercontent.com/username/repo/branch/path/to/jamwi_logo.jpg"

# Display the image in the sidebar
st.sidebar.image(image_url, caption="Jamwi Building Contractors", use_container_width=True)

def run():
    # Sidebar navigation menu
    with st.sidebar:
        selected_app = option_menu(
            menu_title="Project Menu",
            options=["Introduction", "Project Gallery", "Total Project Costs",
                     "Labor Costs", "Material Costs", "KPI's"],
            icons=["house", "image", "cash", "people", "bricks", "clipboard-data"],
            menu_icon="cast",
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
        run_introduction()  # <- CALL THIS FUNCTION
    elif selected_app == "Project Gallery":
        run_project_gallery()
    elif selected_app == "Total Project Costs":
        st.write("Total project costs overview.")
    elif selected_app == "Labor Costs":
        st.write("Details about labor costs.")
    elif selected_app == "Material Costs":
        st.write("Breakdown of material costs.")
    elif selected_app == "KPI's":
        st.write("Key Performance Indicators for the project.")

# Run the app
if __name__ == "__main__":
    run()
