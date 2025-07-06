# from agents import Agent, Runner ,AsyncOpenAI , OpenAIChatCompletionsModel
# from dotenv import load_dotenv
# from agents import set_default_openai_key
# import os
# import asyncio

# load_dotenv()

# gemini_api_key = os.environ.get("GEMINI_API_KEY")
# set_default_openai_key(gemini_api_key)




# if not gemini_api_key:
#     raise ValueError("OPENAI_API_KEY is not set in the environment variables.")


# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=external_client
# )


# def main():
#     agent = Agent(
#         name="Assistant", 
#         instructions="You are a helpful assistant", 
#         model="gpt-4o"
#     )

#     result = Runner.run_sync(agent, "What is a capital or pakistan.")
#     print(result.final_output)

# if __name__ == "__main__":
#     asyncio.run(main())
    
    
    
def main():
    print("Hello, World!")
    
if __name__ == "__main__":
    main()