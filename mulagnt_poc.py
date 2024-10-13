"""
Fully Connected Network
"""

import openai
from pydantic.functional_validators import ModelWrapValidator
from swarm import Swarm, Agent
from swarm.types import Response
from dotenv import load_dotenv
import os


# You have to add an OPENAI_API_KEY in .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key
client = Swarm()


agent_1 = Agent(
    name="Agent 1",
    instructions="You are tasked with generating responses based on the user inputs and the other agents."
)

agent_2 = Agent(
    name="Agent 2",
    instructions="You are tasked with generating responses based on the user inputs and the other agents."
)

agent_3 = Agent(
    name="Agent 3",
    instructions="You are tasked with generating responses based on the user inputs and the other agents."
)

# Moderator is an agent that summarize the responses after devate rounds
moderator = Agent(
    name="Moderator",
    instructions="You are tasked with generating the conclusion of the agents' debate and output the most common opinion or response among the agents."
)

# Responses
conversation_session = []

# content_input = input("Please input your user prompt: ")
# messages = [{"role": "user", "content": content_input}]
