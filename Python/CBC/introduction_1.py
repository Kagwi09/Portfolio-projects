import streamlit as st

def run_introduction():
    st.title("Introduction")

    # Custom CSS for segment borders and styling
    st.markdown(
        """
        <style>
            .segment-box {
                border: 2px solid #00bfae;
                padding: 15px;
                border-radius: 10px;
                background-color: #f9f9f9;
                margin-bottom: 15px;
                height: 100px; /* Adjust height as needed */
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

    # Loop to create 4 rows with 2 segments each (8 segments total)
    placeholder_number = 1
    for _ in range(4):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"""
                <div class="segment-box">
                    <div class="segment-title">Placeholder {placeholder_number}</div>
                    <p>This is the content for Placeholder {placeholder_number}.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            placeholder_number += 1

        with col2:
            st.markdown(
                f"""
                <div class="segment-box">
                    <div class="segment-title">Placeholder {placeholder_number}</div>
                    <p>This is the content for Placeholder {placeholder_number}.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            placeholder_number += 1
