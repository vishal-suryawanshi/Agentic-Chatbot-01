import streamlit as st
import os
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_results import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model, 
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("ERROR: Failed to load the user input from UI.")
        return
    
    user_message = st.chat_input("Enter Your message: ")

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("LLM Model could not be initialized. ")
                return
            
            usecase = user_input["selected_usecase"]

            if not usecase:
                st.error("Usecase is not selected.")
                return
            
            graph_builder = GraphBuilder(model=model)
            try:
                graph = graph_builder.setup_graph(usecase=usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()

            except Exception as e:
                raise ValueError(f"ERROR: Graph set up failed - {e}")
                return

        except Exception as e:
            raise ValueError(f"Error with exception: {e}")
            return
