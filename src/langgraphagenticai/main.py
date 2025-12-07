import streamlit as st
import os
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model, 
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui( )

    if not user_input:
        st.error("ERROR: Failed to load the user input from UI.")
        return
    
    user_message = st.chat_input("Enter Your message: ")
