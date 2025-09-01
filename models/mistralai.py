from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os


load_dotenv()

model = ChatMistralAI(model="mistral-large-latest",
    temperature=0,
    max_retries=2, max_tokens= 100)

result = model.invoke("Who is the president of USA")

print(result.content)