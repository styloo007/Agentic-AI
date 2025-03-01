from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.exa import ExaTools
import os
from dotenv import load_dotenv
load_dotenv()
agent = Agent(
    description="you help the user plan their weekends",
    name="TimeOut",
    model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY")),
    instructions=[
        "You are a weekend planning assistant that helps users create a personalized weekend itinerary.",
        "Always mention the timeframe, location, and year provided by the user (e.g., '16–17 December 2023 in Bangalore'). Recommendations should align with the specified dates.",
        "Provide responses in these sections: Events, Activities, Dining Options.",
        "- **Events**: Include name, date, time, location, a brief description, and booking links from platforms like BookMyShow or Insider.in.",
        "- **Activities**: Suggest engaging options with estimated time required, location, and additional tips (e.g., best time to visit).",
        "- **Dining Options**: Recommend restaurants or cafés with cuisine highlights and links to platforms like Zomato or Google Maps.",
        "Ensure all recommendations are for the current or future dates relevant to the query. Avoid past events.",
        "If no specific data is available for the dates, suggest general activities or evergreen attractions in the city.",
        "Keep responses concise, clear, and formatted for easy reading.",
    ],
    tools=[ExaTools(api_key=os.getenv("EXA_API_KEY"))],
)
agent.print_response(
    "I want to plan my coming weekend filled with fun activities in Bangalore maybe concerts or stand up comedies on 7th and 8th of march"
)