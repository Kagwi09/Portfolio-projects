import streamlit as st
from streamlit_option_menu import option_menu

def run_project_gallery():
    # Nested navigation within the Project Gallery
    selected_page = option_menu(
        menu_title="Project Gallery",
        options=["Overview", "Site Clearance and Excavation"],
        icons=["info-circle", None],  # Remove icon for "Site Clearance and Excavation"
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

        # Create three columns for the page content
        col1, col2, col3 = st.columns(3)

        # Add placeholders for images in each column
        with col1:
            st.image(
                "https://via.placeholder.com/300x200",  # Replace with your image URL later
                caption="Section 1 Placeholder",
                use_column_width=True
            )

        with col2:
            st.image(
                "https://via.placeholder.com/300x200",  # Replace with your image URL later
                caption="Section 2 Placeholder",
                use_column_width=True
            )

        with col3:
            st.image(
                "https://via.placeholder.com/300x200",  # Replace with your image URL later
                caption="Section 3 Placeholder",
                use_column_width=True
            )
