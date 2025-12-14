from langchain_tavily.tavily_search import TavilySearch
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return list of tools to be used in chatbot
    """

    return [TavilySearch(max_results=2)]

def create_tool_node(tools):
    """
    CReate and return the tool node.
    """

    return ToolNode(tools=tools)