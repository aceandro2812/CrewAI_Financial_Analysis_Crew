from crewai import Agent, Task, Crew , Process ,LLM
import os
from typing import List, Dict
from pydantic import BaseModel, Field
from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import BaseTool
from crewai_tools import ScrapeWebsiteTool
import json
from pprint import pprint


# LLM for agents
gemini_llm  = LLM(
    model="openai/gemini-2.0-flash-exp",
    temperature=0.7,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=""
)
# reasoning LLm for manager
gemini_thinking_llm  = LLM(
    model="openai/gemini-2.0-flash-thinking-exp",
    temperature=0.7,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=""
)

# Search tool init
class SearchToolInput(BaseModel):
    query: str = Field(..., description="Search query string")

class SearchTool(BaseTool):
    name: str = "web_search"
    description: str = "Search for real-time information about companies and industries"
    args_schema = SearchToolInput
        
    def _run(self, query: str) -> str:
        search = DuckDuckGoSearchRun(region="pt-br")
        return search.run(query)
# tool initialization
search_tool = SearchTool()
scrape_tool = ScrapeWebsiteTool()


# creating agents 
data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Monitor and analyze market data in real-time "
         "to identify trends and predict market movements.",
    backstory="Specializing in financial markets, this agent "
              "uses statistical modeling and machine learning "
              "to provide crucial insights. With a knack for data, "
              "the Data Analyst Agent is the cornerstone for "
              "informing trading decisions.",
    verbose=True,
    allow_delegation=True,
    tools = [scrape_tool, search_tool],
    llm=gemini_llm
)

# Take a carefull look of how the below agent takes into consideration the analysis from the previous agent
trading_strategy_agent = Agent(
    role="Trading Strategy Developer",
    goal="Develop and test various trading strategies based "
         "on insights from the Data Analyst Agent.",
    backstory="Equipped with a deep understanding of financial "
              "markets and quantitative analysis, this agent "
              "devises and refines trading strategies. It evaluates "
              "the performance of different approaches to determine "
              "the most profitable and risk-averse options.",
    verbose=True,
    allow_delegation=True,
    tools = [scrape_tool, search_tool],
    llm=gemini_llm
)
execution_agent = Agent(
    role="Trade Advisor",
    goal="Suggest optimal trade execution strategies "
         "based on approved trading strategies.",
    backstory="This agent specializes in analyzing the timing, price, "
              "and logistical details of potential trades. By evaluating "
              "these factors, it provides well-founded suggestions for "
              "when and how trades should be executed to maximize "
              "efficiency and adherence to strategy.",
    verbose=True,
    allow_delegation=True,
    tools = [scrape_tool, search_tool],
    llm=gemini_llm
)
risk_management_agent = Agent(
    role="Risk Advisor",
    goal="Evaluate and provide insights on the risks "
         "associated with potential trading activities.",
    backstory="Armed with a deep understanding of risk assessment models "
              "and market dynamics, this agent scrutinizes the potential "
              "risks of proposed trades. It offers a detailed analysis of "
              "risk exposure and suggests safeguards to ensure that "
              "trading activities align with the firm’s risk tolerance.",
    verbose=True,
    allow_delegation=True,
    tools = [scrape_tool, search_tool],
    llm=gemini_llm
)


# Tasks

# Task for Data Analyst Agent: Analyze Market Data
data_analysis_task = Task(
    description=(
        "Continuously monitor and analyze market data for "
        "the selected stock ({stock_selection}). "
        "Use statistical modeling and machine learning to "
        "identify trends and predict market movements."
    ),
    expected_output=(
        "Insights and alerts about significant market "
        "opportunities or threats for {stock_selection}."
    ),
    output_file="analysis_results.txt",
    agent=data_analyst_agent,
)
# Task for Trading Strategy Agent: Develop Trading Strategies
# see how the output of data analyst agent is given to the trade strat agent in words
strategy_development_task = Task(
    description=(
        "Develop and refine trading strategies based on "
        "the insights from the Data Analyst and "
        "user-defined risk tolerance ({risk_tolerance}). "
        "Consider trading preferences ({trading_strategy_preference})."
    ),
    expected_output=(
        "A set of potential trading strategies for {stock_selection} "
        "that align with the user's risk tolerance."
    ),
    output_file="strategy.md",
    agent=trading_strategy_agent,
)


# Task for Trade Advisor Agent: Plan Trade Execution
execution_planning_task = Task(
    description=(
        "Analyze approved trading strategies to determine the "
        "best execution methods for {stock_selection}, "
        "considering current market conditions and optimal pricing."
    ),
    expected_output=(
        "Detailed execution plans suggesting how and when to "
        "execute trades for {stock_selection}."
    ),
    output_file="execution_plans.md",
    agent=execution_agent,
)

# Task for Risk Advisor Agent: Assess Trading Risks
risk_assessment_task = Task(
    description=(
        "Evaluate the risks associated with the proposed trading "
        "strategies and execution plans for {stock_selection}. "
        "Provide a detailed analysis of potential risks "
        "and suggest mitigation strategies."
    ),
    expected_output=(
        "A comprehensive risk analysis report detailing potential "
        "risks and mitigation recommendations for {stock_selection}."
    ),
    output_file="risk_mitigation_plan.md",
    agent=risk_management_agent,
)


# from crewai import Crew, Process
# from langchain_openai import ChatOpenAI

# Define the crew with agents and tasks
# HERE HIERARCHICAL process is used so there is a manager_llm that manages the other agents , this is to ensure that the context doesnt fade out with multiple agents working on the same task
financial_trading_crew = Crew(
    agents=[data_analyst_agent, 
            trading_strategy_agent, 
            execution_agent, 
            risk_management_agent],
    
    tasks=[data_analysis_task, 
           strategy_development_task, 
           execution_planning_task, 
           risk_assessment_task],
    
    manager_llm=gemini_thinking_llm,
    process=Process.hierarchical,
    verbose=True
)

# Example data for kicking off the process
financial_trading_inputs = {
    'stock_selection': 'Reliance Industries',
    'initial_capital': '100000',
    'risk_tolerance': 'High',
    'trading_strategy_preference': 'Day Trading',
    'news_impact_consideration': True
}

### this execution will take some time to run
result = financial_trading_crew.kickoff(inputs=financial_trading_inputs)
