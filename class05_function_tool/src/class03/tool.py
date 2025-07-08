from dotenv import load_dotenv
from agents import Agent, Runner,function_tool ,FunctionTool, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import os
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",

)

model = OpenAIChatCompletionsModel (
     model="gemini-2.0-flash",
    openai_client=external_client
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


weather_haiku_agent = Agent(
    name="Weather Haiku Agent",
    instructions=
    "You create haikus about the weather. Use the weather tool to get information.",
    tools=[get_weather],
)

result= Runner.run_sync(
    weather_haiku_agent,
    input="What is the weather in Tokyo?",
    run_config=config,
)
print(result.final_output)


        









# ****************************************************** ya kam kar rha h bs weathewr ki open ai key set nh h************************************************************