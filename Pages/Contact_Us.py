import streamlit as st


def contact_us_page():
    st.title("Contact Us")

    #st.image(".venv/Scripts/Images/706gw_no_bg.png", use_column_width=True, caption="706 Grey Wolves Logo")
    st.write("Email us at TestEmail@gmail.com")

    st.markdown("""
        <div style="text-align: center;">
            <a href="tel:+19999999999" style="
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                color: white;
                background-color: #4CAF50;
                border: none;
                border-radius: 5px;
                text-decoration: none;
            ">
                1-999-999-9999
            </a>
        </div>
        """, unsafe_allow_html=True
                )

    st.markdown("""
        <style>
            .social-icons img {
                margin-right: 20px;
            }
        </style>
        **Follow us on social media:**
        <div class="social-icons">
            <a href="https://www.facebook.com/p/No-Fly-Zone-7v7-100088382887929/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" width="50" height="50" alt="Facebook">
            </a>
            <a href="https://www.instagram.com/noflyzone_ga/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="50" height="50" alt="Instagram">
            </a>
        </div>
        """, unsafe_allow_html=True
                )