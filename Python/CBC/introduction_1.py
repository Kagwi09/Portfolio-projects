import streamlit as st

def run_introduction():
    # Custom CSS for the main segment
    st.markdown(
        """
        <style>
        .full-screen-container {
            height: 100vh;
            width: 100%;
            padding-top: 3px;
            padding-bottom: 3px;
            border: 1px solid #000;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }
        .sub-segment {
            margin: 10px;
            padding: 10px;
            border: 2px dashed #4CAF50;  /* Dash border for child segments */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Main segment container
    st.markdown('<div class="full-screen-container">', unsafe_allow_html=True)
    st.write("Main Segment")
    
    # First nested segment
    st.markdown('<div class="sub-segment">', unsafe_allow_html=True)
    st.write("This is the first nested segment")
    st.markdown('</div>', unsafe_allow_html=True)

    # Second nested segment
    st.markdown('<div class="sub-segment">', unsafe_allow_html=True)
    st.write("This is the second nested segment")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Third nested segment (in columns)
    st.markdown('<div class="sub-segment">', unsafe_allow_html=True)
    st.write("This is the third nested segment")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Segment 1 in column 1")
    with col2:
        st.write("Segment 2 in column 2")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
