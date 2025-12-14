from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode():
    def __init__(self, model):
        self.llm = model

    def process(self, tools):
        llm_with_tool = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            return {"messages": [llm_with_tool.invoke(state['messages'])]}

        return chatbot_node 