import streamlit as st

def run_introduction():
    # Custom CSS for the full-screen container and the grid layout
    st.markdown(
        """
        <style>
        /* Full-screen container */
        .full-screen-container {
            height: 100vh;  /* Full screen height */
            width: 100%;    /* Full screen width */
            display: grid;
            grid-template-columns: repeat(4, 1fr);  /* 4 equal columns */
            grid-template-rows: 1fr 1fr 0.5fr;  /* 2 equal rows at the top, 1 half-sized row at the bottom */
            gap: 20px;  /* Space between containers */
            padding: 20px;
        }

        /* Style for each segment */
        .segment {
            border: 2px solid #333;  /* Solid border for each segment */
            text-align: center;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Full-Screen Container that takes up the entire screen
    st.markdown('<div class="full-screen-container">', unsafe_allow_html=True)

    # 12 containers within the full screen container
    for i in range(12):
        st.markdown(f'<div class="segment">Segment {i+1}</div>', unsafe_allow_html=True)

    # Closing the full-screen container div
    st.markdown('</div>', unsafe_allow_html=True)

