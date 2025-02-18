import streamlit as st

def run_introduction():
    # Custom CSS for the full-screen container and nested containers (segments)
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
        .nested-container {
            margin: 10px 0;
            padding: 20px;
            border: 2px dashed #4CAF50;
            flex-shrink: 0;
        }
        .nested-container-large {
            margin: 10px 0;
            padding: 30px;
            border: 2px dashed #4CAF50;
            flex-grow: 1;  /* This takes up more space inside the full-screen container */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Full-Screen Container that takes up the entire screen
    st.markdown('<div class="full-screen-container">', unsafe_allow_html=True)
    
    # First nested container (Standard size)
    st.markdown('<div class="nested-container">', unsafe_allow_html=True)
    st.write("This is the first nested container inside the full-screen container.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Second nested container (Standard size)
    st.markdown('<div class="nested-container">', unsafe_allow_html=True)
    st.write("This is the second nested container inside the full-screen container.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Third nested container (Larger size)
    st.markdown('<div class="nested-container-large">', unsafe_allow_html=True)
    st.write("This is the third nested container, which takes up more space inside the container.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Fourth nested container (Standard size)
    st.markdown('<div class="nested-container">', unsafe_allow_html=True)
    st.write("This is the fourth nested container inside the full-screen container.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
