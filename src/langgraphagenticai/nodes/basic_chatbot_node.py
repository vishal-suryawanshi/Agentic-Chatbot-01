from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot node implementation
    """
    def __init__(self, model):
        self.llm = model

    def process(self, State)-> dict:
        """
        Process the input state and generate the LLM repsonse
        """

        return {"messages": self.llm.invoke(State['messages'])}