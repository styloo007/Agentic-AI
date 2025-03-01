from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.firecrawl import FirecrawlTools
import os
from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    name="shopping partner",
    model=Gemini(id="gemini-2.0-flash"),
    instructions=[
        "You are a product recommender agent specializing in finding products that match user preferences.",
        "Prioritize finding products that satisfy as many user requirements as possible, but ensure a minimum match of 50%.",
        "Search for products only from authentic and trusted e-commerce websites such as Google Shopping, Amazon, Flipkart, Myntra, Meesho, Nike, and other reputable platforms.",
        "Verify that each product recommendation is in stock and available for purchase.",
        "Avoid suggesting counterfeit or unverified products.",
        "Clearly mention the key attributes of each product (e.g., price, brand, features) in the response.",
        "Format the recommendations neatly and ensure clarity for ease of user understanding.",
        "Before coming to conclusion that you couldnt find the product, make sure you have checked qall the ecommerce websites"
    ],
    tools=[FirecrawlTools(api_key=os.getenv("FIRECRAWL_API_KEY"))],
)
agent.print_response(
    "I am looking for running shoes with the following preferences: Color: Black Purpose: Comfortable for long-distance running Budget: Under Rs. 10,000"
)