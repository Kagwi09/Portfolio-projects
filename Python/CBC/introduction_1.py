import streamlit as st

def run_introduction():
    # Custom CSS for the main segment and sub-segments
    st.markdown(
        """
        <style>
        .full-screen-container {
            height: 100vh;
            width: 100%;
            padding: 20px;
            border: 3px solid #000;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }
        .sub-segment {
            margin: 10px 0;
            padding: 15px;
            border: 2px dashed #4CAF50;  /* Dash border for child segments */
        }
        .sub-segment-large {
            margin: 10px 0;
            padding: 20px;
            border: 2px dashed #4CAF50;
            flex-grow: 1;  /* This will take up more space */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Main full-screen container
    st.markdown('<div class="full-screen-container">', unsafe_allow_html=True)
    
    # First nested segment (standard size)
    st.markdown('<div class="sub-segment">', unsafe_allow_html=True)
    st.write("This is the first nested segment inside the full-screen container.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Second nested segment (standard size)
    st.markdown('<div class="sub-segment">', unsafe_allow_html=True)
    st.write("This is the second nested segment inside the full-screen container.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Third nested segment (larger size)
    st.markdown('<div class="sub-segment-large">', unsafe_allow_html=True)
    st.write("This is the third nested segment, which takes up more space inside the container.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Fourth nested segment (standard size)
    st.markdown('<div class="sub-segment">', unsafe_allow_html=True)
    st.write("This is the fourth nested segment inside the full-screen container.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

