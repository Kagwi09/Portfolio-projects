import streamlit as st
from streamlit_option_menu import option_menu

def run_project_gallery():
    # Nested navigation within the Project Gallery
    selected_page = option_menu(
        menu_title="Project Gallery",
        options=["Site Clearance and Excavation","Substructure","Superstructure","Finishes"],
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
    if selected_page == "Substructure":
        st.subheader("Substructure")

        # Create three columns for the page content
        col1, col2, col3 = st.columns(3)

        # Add placeholders for images in each column with corrected URLs
        with col1:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/clearance.jpg",  # Raw image URL
                caption="Section 1 Placeholder",
                use_container_width=True
            )

        with col2:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/exc1.jpg",  # Raw image URL
                caption="Section 2 Placeholder",
                use_container_width=True
            )

        with col3:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/exc2.jpg",  # Raw image URL
                caption="Section 3 Placeholder",
                use_container_width=True
            )


    elif selected_page == "Site Clearance and Excavation":
        st.subheader("Site Clearance and Excavation")

        # Create three columns for the page content
        col1, col2, col3 = st.columns(3)

        # Add placeholders for images in each column with corrected URLs
        with col1:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/clearance.jpg",  # Raw image URL
                caption="Section 1 Placeholder",
                use_container_width=True
            )

        with col2:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/exc1.jpg",  # Raw image URL
                caption="Section 2 Placeholder",
                use_container_width=True
            )

        with col3:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/exc2.jpg",  # Raw image URL
                caption="Section 3 Placeholder",
                use_container_width=True
            )
     elif selected_page == "Superstructure":
        st.subheader("Superstructure")

        # Create three columns for the page content
        col1, col2, col3 = st.columns(3)

        # Add placeholders for images in each column with corrected URLs
        with col1:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/clearance.jpg",  # Raw image URL
                caption="Section 1 Placeholder",
                use_container_width=True
            )

        with col2:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/exc1.jpg",  # Raw image URL
                caption="Section 2 Placeholder",
                use_container_width=True
            )

        with col3:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/exc2.jpg",  # Raw image URL
                caption="Section 3 Placeholder",
                use_container_width=True
            )
    elif selected_page == "Superstructure":
    st.subheader("Superstructure")

        # Create three columns for the page content
        col1, col2, col3 = st.columns(3)

        # Add placeholders for images in each column with corrected URLs
        with col1:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/clearance.jpg",  # Raw image URL
                caption="Section 1 Placeholder",
                use_container_width=True
            )

        with col2:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/exc1.jpg",  # Raw image URL
                caption="Section 2 Placeholder",
                use_container_width=True
            )

        with col3:
            st.image(
                "https://raw.githubusercontent.com/Kagwi09/Portfolio-projects/main/Python/CBC/exc2.jpg",  # Raw image URL
                caption="Section 3 Placeholder",
                use_container_width=True
            )
