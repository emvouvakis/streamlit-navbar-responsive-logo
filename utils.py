import streamlit as st
import base64
from streamlit.components.v1 import html

from PATHS import NAVBAR_PATHS, SETTINGS


def inject_custom_css():
    with open('assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def get_current_route():
    try:
        return st.query_params.get_all('nav')[0]
    except:
        return None


def navbar_component():
    # Function to encode an image to base64
    def encode_image_to_base64(image_path):
        with open(image_path, "rb") as image_file:
            image_as_base64 = base64.b64encode(image_file.read()).decode("utf-8")
        return image_as_base64

    # Encode the image to base64
    logo_image_as_base64 = encode_image_to_base64("./assets/images/logo.png")  # Replace with the actual path or URL of your image
    settings_image_as_base64 = encode_image_to_base64("./assets/images/settings.png")  # Replace with the actual path or URL of your image

    # Function to generate navigation bar items
    def generate_navbar_items(navbar_paths):
        navbar_items = ''.join(
            f'<a href="/?nav={value}" class="navitem" target="_self">{key}</a>'
            for key, value in navbar_paths.items()
        )
        return navbar_items

    # Function to generate settings dropdown items
    def generate_settings_items(settings):
        settings_items = ''.join(
            f'<a href="/?nav={value}" class="settingsitem" target="_self">{key}</a>'
            for key, value in settings.items()
        )
        return settings_items

    # Generate navigation bar items and settings dropdown items
    navbar_items = generate_navbar_items(NAVBAR_PATHS)
    settings_items = generate_settings_items(SETTINGS)

    # HTML structure for the navigation bar with the image and items
    component = f'''
        <nav class="navbar" id="navbar">
            <div class="nav-dropdown" id="navDropDown" >
                <img class="nav-btn" src="data:image/png;base64, {logo_image_as_base64}"/>
                <div class="nav-content" id="navContent" >
                    {navbar_items}
                </div>
            </div>
            <div class="settings-dropdown" id="settingsDropDown">
                <img class="settings-btn" src="data:image/png;base64, {settings_image_as_base64}"/>
                <div class="settings-content" id="settingsContent">
                    {settings_items}
                </div>
            </div>
        </nav>
    '''
    st.markdown(component, unsafe_allow_html=True)

    js = '''
    <script>
        
        // Dropdown hide / show Settings
        var settings_drop_down = window.parent.document.getElementById("settingsDropDown");
        settings_drop_down.onclick = function() {
            var dropWindow = window.parent.document.getElementById("settingsContent");
            if (dropWindow.style.visibility == "hidden"){
                dropWindow.style.visibility = "visible";
            }else{
                dropWindow.style.visibility = "hidden";
            }
        };

        // Dropdown hide / show Navbar
        var nav_drop_down = window.parent.document.getElementById("navDropDown");
        nav_drop_down.onclick = function() {
            var dropWindow = window.parent.document.getElementById("navContent");
            if (dropWindow.style.visibility == "hidden"){
                dropWindow.style.visibility = "visible";
            }else{
                dropWindow.style.visibility = "hidden";
            }
        };
    </script>
    '''
    html(js)