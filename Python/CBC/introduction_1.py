import streamlit as st

def run_introduction():
    # Custom CSS for the full-screen container and the nested segments
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
            gap: 20px; /* Space between nested segments */
        }
        
        /* Style for the nested segments */
        .nested-segment {
            border: 2px dashed #333;  /* Dashed border for the nested segments */
            padding: 20px;
            text-align: center;
            width: 100%; /* Ensure the nested segments fill the container width */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Full-Screen Container that takes up the entire screen
    st.markdown('<div class="full-screen-container">', unsafe_allow_html=True)

    # First Nested Segment
    st.markdown('<div class="nested-segment">', unsafe_allow_html=True)
    st.write("This is the first nested segment inside the full-screen container.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Second Nested Segment
    st.markdown('<div class="nested-segment">', unsafe_allow_html=True)
    st.write("This is the second nested segment inside the full-screen container.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Closing the full-screen container div
    st.markdown('</div>', unsafe_allow_html=True)
