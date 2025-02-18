import streamlit as st

def run_introduction():
    # Custom CSS to remove Streamlit padding and fill entire screen
    st.markdown(
        """
        <style>
            /* Remove Streamlit's default padding and margin */
            .appview-container .main .block-container {
                padding-top: 0;
                padding-right: 0;
                padding-left: 0;
                padding-bottom: 0;
            }

            /* Optional: Remove sidebar padding as well (if you want full-page view) */
            [data-testid="stSidebar"] {
                display: none;
            }

            body, html {
                margin: 0;
                padding: 0;
                height: 100%;
            }

            .full-page-segment {
                width: 100vw;  /* Full viewport width */
                height: 100vh; /* Full viewport height */
                border: 3px solid #00bfae;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #f0f0f0;
                box-sizing: border-box; /* Include border in width/height */
            }

            .placeholder-text {
                position: absolute;
                top: 10px;
                left: 10px;
                font-size: 24px;
                font-weight: bold;
                color: black;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Placeholder text above the segment
    st.markdown('<div class="placeholder-text">Placeholder Text Above Segment</div>', unsafe_allow_html=True)

    # Full page segment
    st.markdown(
        """
        <div class="full-page-segment">
            <!-- Optional: Content Inside Segment -->
            <p>This is the giant segment filling the entire page.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
