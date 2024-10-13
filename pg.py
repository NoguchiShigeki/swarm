import openai
from swarm import Swarm, Agent
from swarm.types import Response
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key
client = Swarm()

def transfer_a():
    return agent_a

def transfer_b():
    return agent_b

# In Collective Intelligence program, the answers of each node is appended to the

agent_a = Agent(
    name="Agent A",
    instructions="You are one of my agent 'Agent A', you are helphul assistant. You need to put 'Agent A: ' at the beginning of a response message to signify who you are.",
    # If I want the agent to be truthful or not answering unreliable answers
    # instructions="You are one of my agent, you are helphul assistant and not going to answer if the answer is untruthful or unreliable."
    functions=[transfer_b]
)

agent_b = Agent(
    name="Agent B",
    instructions="You are one of my agent 'Agent B', you are helphul assistant. You need to put 'Agent B: ' at the beginning of a response message to signify who you are.",
    functions=[transfer_a]
)

conversation_session = []

messages = [{"role": "user", "content": "Tom has a red marble, a green marble, a blue marble, and three identical yellow marbles. How many different groups of two marbles can Tom choose. If you solved it, hand over the question and make Agent B generate the answer."}]

# count = 0
# debate_threshold = 3

# while count < debate_threshold:
response = client.run(
    agent=agent_a,
    messages=messages
)

conversation_session.append(response.messages[-1]["content"])
print(response.messages[-1]["content"])
# count += 1

print(conversation_session)
