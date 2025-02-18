import streamlit as st
from streamlit_option_menu import option_menu

def run_project_gallery():
    # Nested navigation within the Project Gallery
    selected_page = option_menu(
        menu_title="Project Gallery",
        options=["Site Clearance and Excavation", "Substructure", "Superstructure", "Finishes"],
        icons=["info-circle", None],  # Remove icon for "Site Clearance and Excavation"
        menu_icon="images",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#f8f9fa"},
            "icon": {"color": "blue", "font-size": "18px"},
            "nav-link": {"color": "black", "font-size": "16px", "margin": "0px", "--hover-color": "#e8e8e8"},
            "nav-link-selected": {"background-color": "#00bfae"},
        }
    )

    # Helper function to display images in 3 columns
    def display_images():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/clearance.jpg",
                caption="Section 1 Placeholder",
                use_container_width=True
            )
        with col2:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/exc1.jpg",
                caption="Section 2 Placeholder",
                use_container_width=True
            )
        with col3:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/exc2.jpg",
                caption="Section 3 Placeholder",
                use_container_width=True
            )

    # Display content based on the selected nested page
    if selected_page == "Site Clearance and Excavation":
        st.subheader("Site Clearance and Excavation")
        display_images()

    elif selected_page == "Substructure":
        st.subheader("Substructure")
        display_images()

    elif selected_page == "Superstructure":
        st.subheader("Superstructure")
        display_images()

    elif selected_page == "Finishes":
        st.subheader("Finishes")
        display_images()
