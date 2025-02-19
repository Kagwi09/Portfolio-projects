import streamlit as st

def run_introduction():
    # Custom CSS for different row heights and segment styles
    st.markdown(
        """
        <style>
            .segment-box-small {
                border: 2px solid #00bfae;
                padding: 5px;
                border-radius: 10px;
                background-color: #f9f9f9;
                margin-bottom: 15px;
                height: 100px; /* Smaller height for top rows */
                text-align: center;
            }
            .segment-box-large {
                border: 2px solid #00bfae;
                padding: 5px;
                border-radius: 10px;
                background-color: #f9f9f9;
                margin-bottom: 15px;
                height: 250px; /* Larger height for bottom row */
                text-align: center;
            }
            .segment-title {
                font-size: 16px;
                font-weight: bold;
                color: #333;
                margin-bottom: 5px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    placeholder_number = 1

    # First 2 Rows - Smaller Boxes
    for _ in range(2):  # 2 rows
        col1, col2, col3, col4 = st.columns(4)

        for col in [col1, col2, col3, col4]:
            with col:
                st.markdown(f'<div class="segment-title">Placeholder {placeholder_number}</div>', unsafe_allow_html=True)
                st.markdown(
                    f"""
                    <div class="segment-box-small">
                        <!-- Content Here -->
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                placeholder_number += 1

    # Last Row - Larger Boxes
    col1, col2, col3, col4 = st.columns(4)

    for col in [col1, col2, col3, col4]:
        with col:
            st.markdown(f'<div class="segment-title">Placeholder {placeholder_number}</div>', unsafe_allow_html=True)
            st.markdown(
                f"""
                <div class="segment-box-large">
                    <!-- Content Here -->
                </div>
                """,
                unsafe_allow_html=True
            )
            placeholder_number += 1
