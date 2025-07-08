from agents import Agent , Runner ,AsyncOpenAI , OpenAIChatCompletionsModel
from agents.run import RunConfig 
from dotenv import load_dotenv
import os


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


if not gemini_api_key:
    raise ValueError("APi key is valid")


external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model= model,
    tracing_disabled=True,
    model_provider=external_client,
)



simple_agent_demo = Agent(
    name = "Your a Agent",
    instructions="You  are helpfull Assisten",
    model=model,
)


result = Runner.run_sync(
    simple_agent_demo,
    input="what is capital of pakistan?",
    run_config = config,
    )
print(result.final_output)
    
   