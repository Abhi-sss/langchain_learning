from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI


load_dotenv()

model = ChatMistralAI()

template2 = PromptTemplate(template="Give the five names of Lord Krishna from {book}",
                          input_variables=['book'])

prompt = template2.invoke({'book':'Mahabharat'})

result = model.invoke(prompt)

print(result.content)