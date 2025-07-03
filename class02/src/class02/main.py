from agents import Agent, Runner
from dotenv import load_dotenv
from agents import set_default_openai_key
import os

load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")
set_default_openai_key(openai_api_key)


if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
# 
agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant", 
    model="gpt-4o"
)

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")

print(result.final_output)