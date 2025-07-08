from agents import Agent , AsyncOpenAI, Runner , OpenAIChatCompletionsModel , RunConfig
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

model = OpenAIChatCompletionsModel (
    model ="gemini-2.0-flash",
    openai_client=external_client,
)
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

async def main():
    # English Agent Exapmle
    english_agent = Agent (
        name="English Agent",
        model=model,
        handoff_description="You are a language expert. Answer the following questions in English with detailed explanations.",
        instructions="You are a language expert. Answer the following questions in English with detailed explanations.",
    )
    # Urdu Agent Example
    urdu_agent = Agent(
        name="Urdu Agent",
        model=model,
        handoff_description="آپ ایک زبان کے ماہر ہیں۔ درج ذیل سوالات کے جوابات اردو میں تفصیلی وضاحت کے ساتھ دیں۔",
        instructions="آپ ایک زبان کے ماہر ہیں۔ درج ذیل سوالات کے جوابات اردو میں تفصیلی وضاحت کے ساتھ دیں۔",
    )
    
    
    agent = Agent(
    name = "Math Agent",
    model=model,
    handoffs={
        "english": english_agent,
        "urdu": urdu_agent
    },
    instructions = "You are a math expert. Answer the following questions with detailed explanations.",
)

 


    result = await Runner.run(
        agent,
        input="define python code?",
        run_config=config
    )
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())
    
