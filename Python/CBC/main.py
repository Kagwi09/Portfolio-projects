
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

path = r"C:\Users\MWANGI\Desktop\jamwi_logo.jpg"
company_logo = Image.open(path)
st.sidebar.image(company_logo, caption="Jamwi Building Contractors", use_column_width=True)


def run(self):
        # Sidebar navigation menu
        with st.sidebar:
            selected_app = option_menu(
                menu_title="Project Menu",
                options=["Introduction", "Project Gallery", "Total Project Costs",
                         "Labor Costs", "Material Costs", "KPI's"],
                icons=["buildings","image","cash-stack","people","bricks","clipboard-data"]
                menu_icon="cast",  # Optional icon for the sidebar menu
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "#fafafa"},
                    "icon": {"color": "blue", "font-size": "20px"},
                    "nav-link": {"color": "black", "font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "lightblue"},
                    "nav-link-selected": {"background-color": "#00bfae"},
                }
            )