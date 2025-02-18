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
                height: 100px;
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
    for _ in range(3):  # 3 rows
        col1, col2, col3, col4 = st.columns(4)

        for col in [col1, col2, col3, col4]:
            with col:
                # Placeholder Title ABOVE the segment box
                st.markdown(f'<div class="segment-title">Placeholder {placeholder_number}</div>', unsafe_allow_html=True)

                # Segment Box
                st.markdown(
                    f"""
                    <div class="segment-box">
                        <!-- Segment Content Here -->
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                placeholder_number += 1
