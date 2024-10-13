import openai
from swarm import Swarm, Agent
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key
client = Swarm()

# Define Agents
agent_1 = Agent(
    name="Agent 1",
    instructions="You are the first node. Generate a response based on the user inputs and pass it to Agent 2."
)

agent_2 = Agent(
    name="Agent 2",
    instructions="You are the second node. Reflect on the user inputs and Agent 1's response, then generate a new response and pass it to Agent 3."
)

agent_3 = Agent(
    name="Agent 3",
    instructions="You are the final node. Generate the conclusion based on the previous agents' responses."
)

# The ansewer grader
grader = Agent(
    name="Grader",
    instructions="You are a grader of the answers. What you do is compare the Agents responses with the correct answer and grade them. If the answer is correct, you output 'True', otherwise 'False'."
)

# Define Messages and Labels for evaluations
messages = [{"role": "user", "content": "Tom has a red marble, a green marble, a blue marble, and three identical yellow marbles. How many different groups of two marbles can Tom choose?"}]

label = "The answer is 7."

# Conversation history
conversation_history = []

# Step 1: Agent 1 generates a response
response_1 = client.run(
    agent=agent_1,
    messages=messages
)

conversation_history.append({
    "agent": agent_1.name,
    "response": response_1.messages[-1]["content"]
})

# Step 2: Agent 2 reflects on Agent 1's response and generates its own
response_2 = client.run(
    agent=agent_2,
    messages=response_1.messages  # Include the conversation history
)

conversation_history.append({
    "agent": agent_2.name,
    "response": response_2.messages[-1]["content"]
})

# Step 3: Agent 3 reflects on Agent 1 and Agent 2's responses and provides a conclusion
response_3 = client.run(
    agent=agent_3,
    messages=response_2.messages  # Include the updated conversation history
)

conversation_history.append({
    "agent": agent_3.name,
    "response": response_3.messages[-1]["content"]
})

# Print the conversation history
for  entry in conversation_history:
    print(f"{entry['agent']}:\n{entry['response']}")

# Print the final conclusion from Agent 3
print("The conclusion from Agent 3:\n", response_3.messages[-1]["content"])

# The grading process
grading_messages = [
    {"role": "system", "content": "You are tasked with grading the answer."},
    {"role": "user", "content": "Answer: " + label},
    {"role": "assistant", "content": response_3.messages[-1]["content"]}
]

grading = client.run(
    agent=grader,
    messages=grading_messages
)

# I put here the grading result for the convinience of the evaluators
grading_result = grading.messages[-1]["content"]

print("Grading result:", grading.messages[-1]["content"])
print(grading_result)
