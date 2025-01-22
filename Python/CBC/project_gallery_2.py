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

        # Create three columns for the page content
        col1, col2, col3 = st.columns(3)

        # Add content to the first column
        with col1:
            st.subheader("Title 1")
            st.write("Content for the first section.")
            st.markdown(
                "<div style='border: 1px solid black; padding: 10px;'>"
                "This is the outlined content for Section 1."
                "</div>",
                unsafe_allow_html=True,
            )

        # Add content to the second column
        with col2:
            st.subheader("Title 2")
            st.write("Content for the second section.")
            st.markdown(
                "<div style='border: 1px solid black; padding: 10px;'>"
                "This is the outlined content for Section 2."
                "</div>",
                unsafe_allow_html=True,
            )

        # Add content to the third column
        with col3:
            st.subheader("Title 3")
            st.write("Content for the third section.")
            st.markdown(
                "<div style='border: 1px solid black; padding: 10px;'>"
                "This is the outlined content for Section 3."
                "</div>",
                unsafe_allow_html=True,
            )
