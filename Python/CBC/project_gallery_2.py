import streamlit as st
from streamlit_option_menu import option_menu

def run_project_gallery():
    # Nested navigation within the Project Gallery
    selected_page = option_menu(
        menu_title="Project Gallery",
        options=["Overview", "Site Clearance and Excavation"],
        icons=["info-circle", "wrench"],
        menu_icon="images",
        default_index=0,
        orientation="horizontal",  # Displays the menu horizontally
        styles={
            "container": {"padding": "0!important", "background-color": "#f8f9fa"},
            "icon": {"color": "blue", "font-size": "18px"},
            "nav-link": {"color": "black", "font-size": "16px", "margin": "0px", "--hover-color": "#e8e8e8"},
            "nav-link-selected": {"background-color": "#00bfae"},
        }
    )

    # Display content based on the selected nested page
    if selected_page == "Overview":
        st.subheader("Project Gallery Overview")
        st.write("This section provides an overview of all ongoing and completed projects.")
    elif selected_page == "Site Clearance and Excavation":
        st.subheader("Site Clearance and Excavation")
        st.write("Details about site clearance and excavation work.")


