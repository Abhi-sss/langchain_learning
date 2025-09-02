from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv


load_dotenv()

model = ChatMistralAI()

messages = [SystemMessage(content='you are a helpful chat assistant'),
            HumanMessage(content='How to learn about langchain')]

result = model.invoke(messages)

print(result.content)