import streamlit as st
import utils as utl
from views import  page1, page2, page3, page4, page5, page6
from pathlib import Path

st.set_page_config(layout="wide", page_title='Template', page_icon=Path('./assets/images/logo.png').read_bytes(), menu_items=None)
utl.inject_custom_css()
utl.navbar_component()


def navigation():
    route = utl.get_current_route()

    # Define home page
    if (route==None or route == "page6"):
        page6.load_view()

    # Define a dictionary to map routes to functions
    route_functions = {
        "page1": page1.load_view,
        "page2": page2.load_view,
        "page3": page3.load_view,
        "page4": page4.load_view,
        "page5": page5.load_view
    }

    # Get the function corresponding to the route and execute it
    route_function = route_functions.get(route)
    if route_function:
        route_function()

        
navigation()