import streamlit as st

def run_introduction():
    st.title("Introduction")

    # Custom CSS for styling the segments with borders and padding
    st.markdown(
        """
        <style>
            .segment-container {
                border: 2px solid #00bfae;
                padding: 15px;
                border-radius: 10px;
                background-color: #f9f9f9;
                margin-bottom: 10px;
            }
            .segment-title {
                font-size: 18px;
                font-weight: bold;
                color: #333;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Loop to create 4 rows with 2 columns each (8 segments)
    segment_number = 1
    for _ in range(4):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"""
                <div class="segment-container">
                    <div class="segment-title">Placeholder {segment_number}</div>
                    <p>This is placeholder content for segment {segment_number}.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            segment_number += 1

        with col2:
            st.markdown(
                f"""
                <div class="segment-container">
                    <div class="segment-title">Placeholder {segment_number}</div>
                    <p>This is placeholder content for segment {segment_number}.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            segment_number += 1
