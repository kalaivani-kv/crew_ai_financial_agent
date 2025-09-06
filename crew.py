from crewai import Crew

from agents.analyst_agent import Analyst
from agents.trader_agent import Trader
from tasks.analyse_task import get_stock_analysis
from tasks.trader_task import trade_decision

stock_crew = Crew(
    agents=[Analyst, Trader],
    tasks=[get_stock_analysis, trade_decision],
    verbose=True
)