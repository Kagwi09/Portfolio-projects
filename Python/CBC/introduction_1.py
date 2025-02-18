import streamlit as st

def run_introduction():
    # Custom CSS to ensure columns fill the width
    st.markdown(
        """
        <style>
            .segment-box-small {
                border: 2px solid #00bfae;
                padding: 15px;
                border-radius: 10px;
                background-color: #f9f9f9;
                margin-bottom: 15px;
                height: 100px; /* Height for the top row segments */
                text-align: center;
            }
            .segment-box-large {
                border: 2px solid #00bfae;
                padding: 15px;
                border-radius: 10px;
                background-color: #f9f9f9;
                margin-bottom: 15px;
                height: 250px; /* Height for the bottom row segments */
                text-align: center;
            }
            .segment-title {
                font-size: 16px;
                font-weight: bold;
                color: #333;
                margin-bottom: 5px;
            }
            .stColumns > div {
                flex: 1;  /* Ensure equal distribution of width for each column */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    placeholder_number = 1

    # First 2 Rows - Smaller Boxes (evenly distributed across the width)
    for _ in range(2):  # 2 rows
        col1, col2, col3, col4 = st.columns(4)  # 4 equal columns

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

    # Last Row - Larger Boxes (still 4 columns)
    col1, col2, col3, col4 = st.columns(4)  # 4 equal columns

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
