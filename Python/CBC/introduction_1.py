import streamlit as st

def run_introduction():
    st.title("Introduction")

    # Create 4 rows with 2 segments each (8 segments in total)
    for i in range(1, 5):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f"Segment {2 * i - 1}")
            st.write(f"Placeholder text for Segment {2 * i - 1}.")

        with col2:
            st.subheader(f"Segment {2 * i}")
            st.write(f"Placeholder text for Segment {2 * i}.")

