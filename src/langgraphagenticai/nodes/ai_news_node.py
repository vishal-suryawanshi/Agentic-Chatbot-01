from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

class AINewsNode:
    def __init__(self, llm):
        self.llm = llm
        self.tavily = TavilyClient()
        self.state = {}

    def fetch_news(self, state: dict):
        """
        Docstring for fetch_news
        
        :param self: Description
        :param state: Description
        :type state: dict
        """
        print(f"=======================>{state}")
        frquency = state['messages'][0].content.lower()
        self.state['frequency'] = frquency
        time_range_map = {'daily': 'd', 'weekly': 'w', "monthly": 'm', 'year':'y'}
        days_map = {'daily': 1, 'weekly':7, "monthly":30, 'year': 366}

        response = self.tavily.search(
            query="Top Artificial Intellligence (AI) technology news India and globally",
            topic='news',
            time_range=time_range_map[frquency],
            include_answer='advanced',
            max_results=15,
            days=days_map[frquency]
        )

        state['news_data'] = response.get('results', [])
        self.state['news_data'] = state['news_data']
        return state
    
    def summarize_news(self, state: dict)-> dict:
        """
        Docstring for summarize_news
        
        :param self: Description
        :param state: Description
        :type state: dict
        :return: Description
        :rtype: dict
        """
        news_items = self.state['news_data']
        prompt_template = ChatPromptTemplate.from_messages([
        ("system", """Summarize AI news articles into markdown format. For each item include:
        Date in **YYYY-MM-DD** format in IST timezone
        Concise sentences summary from latest news
        Sort news by date wise (latest first)
        Source URL as link
        Use Format:
        ### [Date]
        -[Summary] (URL)"""),
        ("user", "Articles: \n{articles}")])

        articles_str = "\n\n".join([
            f"Content: {item.get('content', '')}\nURL: {item.get('url', '')}\nDate: {item.get('published_date', '')}"
            for item in news_items
        ])

        response = self.llm.invoke(prompt_template.format(articles=articles_str))
        state['summary'] = response.content
        self.state['summary'] = state['summary']
        return self.state
    
    def save_results(self, state):
        frequency = self.state['frequency']
        summary = self.state['summary']
        filename = f"./src/langgraphagenticai/AINews/{frequency}_summary.md"
        with open(filename, 'w') as f:
            f.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            f.write(summary)

        self.state['filename'] = filename
        return self.state