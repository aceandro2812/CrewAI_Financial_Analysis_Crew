<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financial Trading CrewAI Project</title>
    <style>
        body {
            font-family: sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            font-weight: 600;
        }
        h1 { font-size: 2em; }
        h2 { font-size: 1.5em; }
        h3 { font-size: 1.2em; }
        code {
            background-color: #f0f0f0;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: monospace;
        }
        pre {
          background-color: #f0f0f0;
          padding: 10px;
          border-radius: 4px;
          overflow-x: auto;
        }
    </style>
</head>
<body>

    <h1>Financial Trading with CrewAI</h1>

    <p>This project demonstrates a financial trading workflow using the CrewAI framework. It simulates a team of specialized agents working together to analyze market data, develop trading strategies, plan trade execution, and manage risks.</p>

    <h2>Project Overview</h2>

    <p>The project uses several key components:</p>
    <ul>
        <li><strong>Agents:</strong> Specialized AI agents with specific roles and goals (Data Analyst, Trading Strategy Developer, Trade Advisor, Risk Advisor).</li>
        <li><strong>Tasks:</strong> Specific tasks assigned to each agent, defining their responsibilities and expected outputs.</li>
        <li><strong>Crew:</strong> A team of agents working together to achieve a common goal (financial trading).</li>
        <li><strong>LLMs:</strong> Large Language Models (Gemini 2.0) used to power the agents' reasoning and decision-making.</li>
        <li><strong>Tools:</strong> External tools (web search, website scraping) used by the agents to gather information.</li>
    </ul>

    <h2>Code Structure</h2>
    <p>The Python code is structured as follows:</p>
    <ul>
        <li>Agent definitions with roles, goals, and backstories.</li>
        <li>Task definitions with descriptions, expected outputs, and assigned agents.</li>
        <li>Crew definition, combining agents and tasks into a collaborative workflow.</li>
        <li>Input data for the trading process.</li>
        <li>Execution of the CrewAI process.</li>
    </ul>

    <h2>Usage</h2>
    <p>To run this project:</p>
    <ol>
        <li>Install the required libraries: <code>pip install crewai langchain pydantic duckduckgo-search</code></li>
        <li>Replace <code>YOUR_API_KEY</code> with your actual Gemini API key.</li>
        <li>Run the Python script: <code>python your_script_name.py</code></li>
    </ol>
    <pre><code>pip install crewai langchain pydantic duckduckgo-search</code></pre>
    <pre><code>python your_script_name.py</code></pre>

    <h2>Key Improvements</h2>
    <ul>
        <li>Comprehensive docstrings and comments for improved code readability.</li>
        <li>Detailed README.md file for project documentation.</li>
        <li>Clearer explanations of the project's purpose and functionality.</li>
    </ul>

    <h2>Example Input</h2>
    <pre><code>
financial_trading_inputs = {
    "stock_selection": "Reliance Industries",
    "initial_capital": "100000",
    "risk_tolerance": "High",
    "trading_strategy_preference": "Day Trading",
    "news_impact_consideration": True,
}
    </code></pre>

    <h2>Output</h2>
    <p>The output of the script will be printed to the console and also saved in output files specified in the Task definitions (e.g., <code>analysis_results.txt</code>, <code>strategy.md</code>, etc.).</p>
    <p>This output will contain the results of the analysis, the developed trading strategies, the execution plans, and the risk assessment.</p>

</body>
</html>
