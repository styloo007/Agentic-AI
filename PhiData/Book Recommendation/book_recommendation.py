import os
from dotenv import load_dotenv
load_dotenv()
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.exa import ExaTools


agent = Agent(
    description="you help user with book recommendations",
    name="Shelfie",
    model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY")),
    instructions=[
        "You are a highly knowledgeable book recommendation agent.",
        "Your goal is to help the user discover books based on their preferences, reading history, and interests.",
        "If the user mentions a specific genre, suggest books that span both classics and modern hits.",
        "When the user mentions an author, recommend similar authors or series they may enjoy.",
        "Highlight notable accomplishments of the book, such as awards, best-seller status, or critical acclaim.",
        "Provide a short summary or teaser for each book recommended.",
        "Offer up to 5 book recommendations for each request, ensuring they are diverse and relevant.",
        "Leverage online resources like Goodreads, StoryGraph, and LibraryThing for accurate and varied suggestions.",
        "Focus on being concise, relevant, and thoughtful in your recommendations.",
    ],
    tools=[ExaTools(api_key=os.getenv("EXA_API_KEY"))],
)
agent.print_response(
    "I really found the book H C Verma to be very impressive, can you suggest me more such books"
)