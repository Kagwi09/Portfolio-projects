import streamlit as st

def run_introduction():
    # Custom CSS for the full-screen container and nested containers (segments)
    st.markdown(
        """
        <style>
        /* Full-screen container */
        .full-screen-container {
            height: 100vh;
            width: 100%;
            padding: 20px;
            border: 3px solid #000;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }
        /* Default nested container */
        .nested-container {
            margin: 10px 0;
            padding: 20px;
            border: 2px dashed #4CAF50;
            flex-shrink: 0;
        }
        /* Larger nested container */
        .nested-container-large {
            margin: 10px 0;
            padding: 30px;
            border: 2px dashed #4CAF50;
            flex-grow: 1;  /* Takes up more space */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Full-Screen Container that takes up the entire screen
    st.markdown('<div class="full-screen-container">', unsafe_allow_html=True)
    
    # Nested Container 1
    st.markdown('<div class="nested-container">', unsafe_allow_html=True)
    st.write("This is the first nested container inside the full-screen container.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Nested Container 2
    st.markdown('<div class="nested-container">', unsafe_allow_html=True)
    st.write("This is the second nested container inside the full-screen container.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Larger Nested Container (takes more space)
    st.markdown('<div class="nested-container-large">', unsafe_allow_html=True)
    st.write("This is the larger nested container inside the full-screen container, which takes up more space.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Nested Container 3
    st.markdown('<div class="nested-container">', unsafe_allow_html=True)
    st.write("This is the third nested container inside the full-screen container.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Closing the full-screen container div
    st.markdown('</div>', unsafe_allow_html=True)
