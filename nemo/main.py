from bot.bot import Bot
import time
import asyncio

"""
need to create venv (or at least have the packages installed):

python -m venv venv
pip install -r requirements.txt

(there might be some broken stuff in there, just install the extra packages manually if it doesn't work)
"""

async def create_user_message(history: [], message: str):
    message_dict = {"role": "user", "content": message}
    history.append(message_dict)
    
async def create_bot_message(history: [], message: {}):
    history.append(message)

async def chat(history: [], dory: Bot):
    return await dory.chat(history)

async def main():
    print("Initializing bot...")
    dory = Bot()
    start = dory.start_time
    print("Bot Created @ ", start)
    message_history = []
    print("Bot initialized\n")

    print("Loading actions...")
    dory.load_actions()
    print("Actions loaded\n")

    print("Running test batch of questions:\n")
    
    await create_user_message(message_history, "Hello there!")
    await create_bot_message(message_history, await chat(message_history, dory))
    
    await create_user_message(message_history, "I'm doing really well today!")
    await create_bot_message(message_history, await chat(message_history, dory))
    
    await create_user_message(message_history, "What are we doing today?")
    await create_bot_message(message_history, await chat(message_history, dory))
    
    await create_user_message(message_history, "What is your name?")
    await create_bot_message(message_history, await chat(message_history, dory))

    print("Chat history:")
    for message in message_history:
        print(f"{message['role']}:\n    {message['content']}\n\n")
    print("Time elapsed since creation ", time.time() - start)
    
async def flow():
    print("Initializing bot...")
    dory = Bot()
    start = dory.start_time
    print("Bot Created @ ", start)
    message_history = []
    print("Bot initialized\n")

    print("Loading actions...")
    dory.load_actions()
    print("Actions loaded\n")

    print("Ready to chat!\n")
    
    while True:
        user_in = input("User: ")
        await create_user_message(message_history, user_in)
        bot_out = await chat(message_history, dory)
        await create_bot_message(message_history, bot_out)
        print("Bot: ", bot_out['content'])
        print("\n")
    
if __name__ == "__main__":
    asyncio.run(main())
    # asyncio.run(flow())
    print("\nDone!")