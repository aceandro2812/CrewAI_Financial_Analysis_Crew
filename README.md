<div align="center">

# AI-Powered Financial Trading Crew

**Automated, Intelligent, and Collaborative Trading Strategy Development**

</div>

## Overview

This project leverages the power of CrewAI, an advanced agent-based orchestration framework, to create a collaborative team of AI agents dedicated to financial trading. These agents work in synergy to analyze market data, develop trading strategies, plan trade executions, and assess risks, providing a comprehensive solution for navigating the complexities of the stock market.

<br>

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*v5dD_4jK4Hl07H1IrsYqJw.png" width="600">
</p>

<br>

## Features

-   **Modular AI Agents**: Specialized agents for data analysis, strategy development, trade execution planning, and risk assessment.
-   **Real-time Market Analysis**: Utilizes DuckDuckGo Search and website scraping tools for up-to-the-minute market insights.
-   **Customizable Strategies**: Tailors trading approaches based on user-defined risk tolerance and trading preferences.
-   **Hierarchical Process Management**: Employs a hierarchical task execution process, ensuring efficient and organized collaboration among agents.
-   **Advanced Language Models**: Powered by the latest Gemini language models for sophisticated decision-making and analysis.

## Agents

-   **Data Analyst Agent**: Monitors and analyzes market data to identify trends and predict movements.
-   **Trading Strategy Developer Agent**: Develops and tests trading strategies based on data insights.
-   **Trade Advisor Agent**: Suggests optimal trade execution strategies.
-   **Risk Advisor Agent**: Evaluates and provides insights on the risks associated with potential trading activities.

## Tools

-   **Web Search Tool**: Leverages DuckDuckGo Search for real-time information gathering.
-   **Website Scraper Tool**: Extracts data from websites to enhance analysis.

## Getting Started

### Prerequisites

-   Python 3.9+
-   CrewAI library
-   Langchain community tools
-   Pydantic
-   Gemini API Key (Make sure to set up your API Key correctly, replace `AIzaSyA6Gd_kJL0g8XCMZXJ-uJwbTDYcac1zqGk` with your actual API key)


### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  Install the required packages:

    ```bash
    pip install crewai langchain-community pydantic crewai-tools
    ```

### Usage

1.  **Configure API Keys**:
    - Replace `AIzaSyA6Gd_kJL0g8XCMZXJ-uJwbTDYcac1zqGk` in the script with your actual Gemini API Key.

2.  **Run the script**:

    ```bash
    python your_script_name.py
    ```

    This will initiate the trading crew with the predefined inputs. The agents will perform their tasks sequentially and output results to designated files (`analysis_results.txt`, `strategy.md`, `execution_plans.md`, `risk_mitigation_plan.md`).

### Example Inputs

```python
financial_trading_inputs = {
    'stock_selection': 'Reliance Industries',
    'initial_capital': '100000',
    'risk_tolerance': 'High',
    'trading_strategy_preference': 'Day Trading',
    'news_impact_consideration': True
}
