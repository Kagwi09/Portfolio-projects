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
            padding-top: 30px; /* Top padding */
            padding-right: 20px; /* Right padding */
            padding-bottom: 30px; /* Bottom padding */
            padding-left: 20px; /* Left padding */
            display: flex;
            flex-direction: column; /* Stack items vertically */
            justify-content: flex-start; /* Align to top of container */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Full-Screen Container that takes up the entire screen
    st.markdown('<div class="full-screen-container">', unsafe_allow_html=True)

    # Content inside the full-screen container
    st.write("This is the full-screen container.")

    # Closing the full-screen container div
    st.markdown('</div>', unsafe_allow_html=True)
