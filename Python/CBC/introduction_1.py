import streamlit as st

def run_introduction():
    # Custom CSS for the full-screen container
    st.markdown(
        """
        <style>
        /* Full-screen container */
        .full-screen-container {
            height: 100vh;  /* Full screen height */
            width: 100%;    /* Full screen width */
            border: 3px solid #000;  /* Border around the segment */
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Full-Screen Container that takes up the entire screen
    st.markdown('<div class="full-screen-container">', unsafe_allow_html=True)

    # Placeholder text inside the full-screen container
    st.write("This is your full-screen segment.")

    # Closing the full-screen container div
    st.markdown('</div>', unsafe_allow_html=True)
