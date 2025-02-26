from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv
load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY")),
    tools=[DuckDuckGo()],
    instructions=["Strictly for every single query, use the Duck Duck go Search to fetch the accurate real time results"],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("Who won India vs Pak match", stream=True)