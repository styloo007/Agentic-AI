from exa_py import Exa
from dotenv import load_dotenv
load_dotenv()
import os

exa = Exa(os.getenv("EXA_API_KEY"))


response = exa.search(
    "ALTECH CORP. 002565000",
    num_results=10
)

print(response)  
