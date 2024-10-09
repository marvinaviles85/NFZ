import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_carousel import carousel
import streamlit.components.v1 as components
import pandas as pd
import os

from Pages.Team_Members import team_members_page
from Pages.Upcoming_Matches import upcoming_matches_page
#from Pages.Sponsorship_and_Donation import sponsorship_and_donation_page
#from Pages.Registration import registration_page
from Pages.Contact_Us import contact_us_page

custom_css = """
<style>
    .centered-title {
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 2.5em;
        color: white;
    }
    .team-member img, .photo-gallery img {
        width: 100%; /* Set a Consistent Width */
        height: 100%; /* Maintain aspect ratio */
        object-fit: contain;
    }
     .carousel-title {
        position: absolute;
        bottom: 20px;
        left: 20px;
        font-size: 1.5em;
        color: white;
    }
    .carousel-text {
        position: absolute;
        bottom: 20px;
        left: 20px;
        font-size: 1em;
        color: white;
    }
    .iframe-container {
        width: 100%;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: rgb(0, 110, 51);
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .iframe-container iframe {
        width: 100%;
        border: none;
    }
        .section-content {
        font-family: 'Arial', sans-serif;
        font-size: 1.2em;
        color: white;
        margin-bottom: 20px;
    }
    .sponsor-level {
        font-family: 'Arial', sans-serif;
        font-size: 1.5em;
        color: white;
        margin-top: 10px;
    }
    .sponsor-details {
        font-family: 'Arial', sans-serif;
        font-size: 1em;
        color: white;
        margin-bottom: 10px;
    }
    .donate-button {
        background-color: rgb(0, 110, 51);
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius:12px;
    }
    .venmo-inf {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.2em;
        color: #333;
        margin-top: 20px;
    }
    .centered-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .title {
        text-align: center;
        font-family: 'Bebas Neue', sans-serif;
        font-size: 50px;
        text-shadow: 2px 2px 0 #000000, 4px 4px 0 #000000;
    }
    .centered-text {
        text-align: center;
    }
     #sponsors {
        text-align: center;
        padding: 20px;
    }
    .sponsor-logos {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 20px;
    }
    .sponsor-logos a img {
        max-width: 150px;
        transition: transform 0.3s;
    }
    .sponsor-logos a img:hover {
        transform: scale(1.1);
    }
    @media (max-width: 768px) {
            .stMarkdown div {
                text-align: center;
            }
            .stMarkdown img {
                width: 100% !important;
                height: auto !important;
            }
        }
    .centered-title {
            text-align: center;
            font-family: 'Arial', sans-serif;
            color: white; /* Change this color to match your theme */
            padding: 20px;
            border-bottom: 2px solid white; /* Optional: Add a bottom border */
        }
        .subtext {
            text-align: center;
            font-family: 'Arial', sans-serif;
            color: white; /* Change this color to match your theme */
            font-size: 14px; /* Smaller font size */
        }
        .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px;
        background-color: None;
        flex-wrap: wrap;
        position: -webkit-sticky;
        position: fixed;
        top: 0;
        z-index: 1000, /* Ensure it stays on top of other content */
    }
    .top-bar img {
        height: 50px;
    }
    .top-bar select {
        padding: 5px;
        font-size: 16px;
    }
    @media (max-width: 600px) {
        .top-bar {
            flex-direction: column;
            align-items: flex-start;
        }
        .top-bar img {
            margin-bottom: 10px;
        }
        .top-bar select {
            width: 100%;
        }
        body {
            padding-top: 70px;
        }
        @import url('style.css');
        }
        .fixed-bottom-button {
                position: fixed;
                bottom: 10px;
                right: 10px;
                padding: 10px 20px;
                font-size: 16px;
                color: white;
                background-color:  rgb(0, 110, 51);
                border: none;
                border-radius: 5px;
                text-decoration: none;
                cursor: pointer;
            }
</style>
"""
# st.set_page_config(layout="wide")
st.set_page_config(
    page_title="NFZ 7v7",
    page_icon="NfzImages/YellowLogo.jpg",
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid='stSidebarNav'] {
            display: none;
        }
    </style>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const sidebar = document.querySelector("[data-testid='stSidebarNav']");
            if (sidebar) {
                sidebar.style.display = 'none';
            }
        });
    </script>
    """,
        unsafe_allow_html=True,
    )

# Add the image and navigation bar to the top of the page
st.markdown("""
    <div class="top-bar">
        <div id="dropdown-container"></div>
    </div>
    """, unsafe_allow_html=True)

st.image("NfzImages/YellowLogo.jpg", caption=" ")

# Dropdown menu for pages selection
# Dropdown menu for pages selection
page = st.selectbox(
    "Select a Page",
    ["Home", "Upcoming Matches", "Team Members", "Contact Us"]
)

#st.markdown("""
#<script>
#    const dropdownContainer = document.getElementbyId('drowndown-container');
#    const selectbox = document.querySelector('select[data-testid="stSelectbox"]');
#    dropdownContainer.appendChild(selectbox);
#</script>
#""", unsafe_allow_html=True)
# Page title and description
# Navigation Logic
if page == "Home":
    st.write("Welcome to the Home Page")
elif page == "Team Members":
    team_members_page()
elif page == "Upcoming Matches":
    upcoming_matches_page()
#elif page == "Sponsorship and Donation":
#    sponsorship_and_donation_page()
#elif page == "Registration":
#    registration_page()
elif page == "Contact Us":
    contact_us_page()

# Home section
if page == "Home":
    #st.markdown("<h1 class='title'>No Fly Zone</h1>", unsafe_allow_html=True)
    st.markdown(
        "<h1 class='centered-text'>Welcome to the home of NFZ (No Fly Zone)!\n\nExplore our team members, schedule, and photos.</h1>",
        unsafe_allow_html=True)
    # st.write("Welcome to the home page!")
    st.image("NfzImages/NFZ.jpg", use_column_width=True)
    st.write(
        "<h3 class='centered-text'>Registration is now open for age groups 11U to 18U! Spots are limited, so secure your place today!</h3>",
        unsafe_allow_html=True)

    # Add a scrolling image gallery
    images = [
        {'img': 'NfzImages/NFZ1.jpg', 'title': '', 'text': ''},
        {'img': 'NfzImages/NFZ2.jpg', 'title': '', 'text': ''},
        {'img': 'NfzImages/NFZ3.jpg', 'title': '', 'text': ''},
        {'img': 'NfzImages/NFZ4.jpg', 'title': '', 'text': ''},
        {'img': 'NfzImages/NFZ5.jpg', 'title': '', 'text': ''},
        {'img': 'NfzImages/NFZ6.jpg', 'title': '', 'text': ''},
        {'img': 'NfzImages/NFZ7.jpg', 'title': '', 'text': ''},
        {'img': 'NfzImages/NFZ8.jpg', 'title': '', 'text': ''},
        {'img': 'NfzImages/NFZ9.jpg', 'title': '', 'text': ''},
        {'img': 'NfzImages/NFZ10.jpg', 'title': '', 'text': ''},
        {'img': 'NfzImages/NfzCLT.jpg', 'title': '', 'text': ''},
        {'img': 'NfzImages/NfzCLT2.jpg', 'title': '', 'text': ''},
        {'img': 'NfzImages/NfzGloves.jpg', 'title': '', 'text': ''},
        {'img': 'NfzImages/NFZOG.jpg', 'title': '', 'text': ''},
        {'img': 'NfzImages/NFZOG1.jpg', 'title': '', 'text': ''},
    ]

    carousel(images)
    st.header("Latest News")
    st.write("Stay tuned for the latest news and updates.")

    # Add sponsors section
#    st.markdown("""
#    <h1 class='centered-title'>Our Valued Sponsors</h1>
#    <p class='subtext'>Click on the images to visit their websites</p>
#""", unsafe_allow_html=True)
#    sponsors_donors = [
#        {"name": "", "position": "", "photo": ""}
#    ]

    # Create outer columns
   # col1, col2, col3 = st.columns(3)

    # First and third images in the first outer column
   # with col1:
   #     st.markdown("""
   #         <div>
   #             <a href="" target="_blank">
   #                 <img src="" width="200">
   #             </a>
   #         </div>
   #     """, unsafe_allow_html=True)

   # with col2:
   #     st.markdown("""
   #         <div style="display: flex; justify-content: center; align-items: center; height: 100;">
   #             <a href="" target="_blank">
   #                 <img src="" width="200">
   #             </a>
   #         </div>
   #     """, unsafe_allow_html=True)

   # with col3:
   #     st.markdown("""
   #         <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
   #             <a href="" target="_blank">
   #                 <img src="" width="200">
   #             </a>
   #         </div>
   #     """, unsafe_allow_html=True)
