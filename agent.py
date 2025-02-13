from phi.agent import Agent 
from phi.model.groq import Groq 
from phi.tools.yfinance import  YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

load_dotenv()
os.environ['PHI_API_KEY']=os.getenv('PHI_API_KEY')
os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')


websearch_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,

)

# Financial Agent 

financial_agent=Agent(
    name="Financial AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(
                    stock_price=True,
                    analyst_recommendations=True,
                    stock_fundamentals=True,
                    company_news=True 
                    )
        ],
    instructions=["use tables to display the data"],
    show_tools_calls=True,
    markdown=True,

)

multi_ai_agent=Agent(
    team=[websearch_agent,financial_agent],
    instructions=["Always include sources","Use Tables to display the data"],
    show_tool_calls=True,
    markdown=True,

)

multi_ai_agent.print_response("Suggest me the best stock to invest $1000 in between  NVDA and MSFT ",stream=True)