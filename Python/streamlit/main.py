import streamlit as st
from streamlit_option_menu import option_menu
#import home
import account
#import trending
#import your_posts
#import about

# Set the page config
st.set_page_config(
    page_title='Pondering App',
    page_icon=':guardsman:',  # Custom icon or emoji
)

# Class to manage multiple pages
class MultiApp:
    def __init__(self):
        self.apps = []
    
    def add_app(self, title, function):
        self.apps.append({
            'title': title,
            'function': function
        })
    
    def run(self):
        # Sidebar navigation menu
        with st.sidebar:
            selected_app = option_menu(
                menu_title="Main Menu",
                options=["Account"],
                icons=["person"],
                menu_icon="cast",  # Optional icon for the sidebar menu
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "#fafafa"},
                    "icon": {"color": "blue", "font-size": "20px"},
                    "nav-link": {"color": "black", "font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "lightblue"},
                    "nav-link-selected": {"background-color": "#00bfae"},
                }
            )
        
        # Based on the selected page, call the respective function
        #if selected_app == "Home": home.app()
        if selected_app == "Account":
            account.app()
        #elif selected_app == "Trending":trending.app()
       # elif selected_app == "Your Posts":your_posts.app()
        # elif selected_app == "About":about.app()

# Run the app
app = MultiApp()
app.run()
