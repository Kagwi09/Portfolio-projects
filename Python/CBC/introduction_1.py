import streamlit as st

def run_introduction():
    st.title("Introduction")

    # Custom CSS for segment borders and styling
    st.markdown(
        """
        <style>
            .segment-box {
                border: 2px solid black;  /* Changed border color to black */
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
            /* Row-specific styles */
            .row-1, .row-2 {
                display: flex;
                gap: 20px; /* Gap between columns */
            }
            .row-3 {
                display: flex;
                gap: 20px;
                height: 50vh; /* Make the third row occupy half of the screen height */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    placeholder_number = 1

    # First and second row (top half of the screen)
    for row_class in ['row-1', 'row-2']:  # 2 rows
        with st.container():
            st.markdown(f'<div class="{row_class}">', unsafe_allow_html=True)

            # Create 4 columns for each row
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

            st.markdown(f'</div>', unsafe_allow_html=True)

    # Third row (bottom half of the screen)
    with st.container():
        st.markdown('<div class="row-3">', unsafe_allow_html=True)

        # Create 4 columns for the bottom row
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

        st.markdown('</div>', unsafe_allow_html=True)
