from agents import Agent, AsyncOpenAI,Runner ,OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv
import os
import asyncio


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
print(gemini_api_key)

if not gemini_api_key:
    print("if api is not valid")
    
    
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model= model,
    model_provider=external_client,
    tracing_disabled=True,
)


agent = Agent(
    name="You are Agent",
    instructions="You are a helpfull agent",
    model=model,
)
async def abc ():
    result=await Runner.run(
        agent,"who is presentend of pakistan?",
    )
    print(result.final_output)
    
    
    if __name__=="__main__":
        asyncio.run(abc())





