import streamlit as st
from streamlit_option_menu import option_menu

def run_project_gallery():
    st.title("Project Gallery")
    
    # Sub-menu for nested pages
    selected_sub_page = option_menu(
        menu_title="Gallery Sub-menu",
        options=["Site Clearance and Excavation", "Substructure", 
                 "Superstructure", "Finishes"],
        icons=["house", "building", "factory", "list-task"],  # Ensure valid icons
        menu_icon="images",  # Optional icon for the sub-menu
        default_index=0,
        orientation="horizontal",  # Display sub-menu horizontally (optional)
        styles={
            "container": {"padding": "5!important", "background-color": "#f9f9f9"},
            "icon": {"color": "green", "font-size": "20px"},
            "nav-link": {"color": "black", "font-size": "16px", "text-align": "center", "--hover-color": "lightblue"},
            "nav-link-selected": {"background-color": "#00bfae"},
        }
    )
    
    # Display content for the selected sub-page
    if selected_sub_page == "Residential Projects":
        st.subheader("Residential Projects")
        st.write("Details and images of residential projects go here.")
    elif selected_sub_page == "Commercial Projects":
        st.subheader("Commercial Projects")
        st.write("Details and images of commercial projects go here.")
    elif selected_sub_page == "Industrial Projects":
        st.subheader("Industrial Projects")
        st.write("Details and images of industrial projects go here.")
    elif selected_sub_page == "Miscellaneous Projects":
        st.subheader("Miscellaneous Projects")
        st.write("Details and images of miscellaneous projects go here.")
