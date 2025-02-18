import streamlit as st

def run_introduction():
    # Custom CSS to remove margin/padding and ensure the segment fills the screen
    st.markdown(
        """
        <style>
            /* Remove default margin and padding from the body and html */
            body, html {
                margin: 0;
                padding: 0;
                height: 100%;  /* Ensure the body takes up the full height of the screen */
            }
            
            .full-page-segment {
                width: 100%;
                height: 100vh;  /* Ensure the segment takes up 100% of the viewport height */
                border: 3px solid #00bfae;  /* Border color */
                border-radius: 10px;
                background-color: #f9f9f9;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
                box-sizing: border-box;  /* Include padding in the element's total width/height */
            }

            .placeholder-text {
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 10px;  /* Space between text and segment */
            }
        </style>
        """, unsafe_allow_html=True
    )

    # Placeholder text above the segment
    st.markdown('<div class="placeholder-text">This is a placeholder text above the giant segment</div>', unsafe_allow_html=True)

    # The large segment
    st.markdown(
        """
        <div class="full-page-segment">
            <!-- Content of the giant segment goes here -->
        </div>
        """, unsafe_allow_html=True
    )
