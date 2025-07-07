from agents import Agent, Runner ,function_tool, OpenAIChatCompletionsModel ,AsyncOpenAI
from dotenv import load_dotenv
from agents.run import RunConfig
import os
import asyncio

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",

)

model=OpenAIChatCompletionsModel (
    model="gemini-0.2-flash",
    openai_client=external_client,
)

config=RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
    
)
def get_weather(city):
    return f"The weather in {city} is sunny"

@function_tool
def get_weather(city: str) -> str:
    """Get the current weather in a given city"""
    return f"The weather in {city} is sunny with a temperature of 70 degrees."

async def wether():
    weather_haiku_agent = Agent(
    name="Weather Haiku Agent",
    instructions=
    "You create haikus about the weather. Use the weather tool to get information.",
    tools=[get_weather],
)

    result=await Runner.run(
    weather_haiku_agent,
    input= "What is the weather in Tokyo?",
    run_config=config
    )
    print(result.final_output)

if __name__=="__main__":
    asyncio.run(wether())
        









# ****************************************************** ya kam kar rha h bs weathewr ki open ai key set nh h************************************************************