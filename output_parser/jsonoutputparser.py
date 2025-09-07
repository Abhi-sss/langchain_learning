from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatMistralAI(model="ministral-8b-latest")

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me five names of {lord} and 5 main temples \n {format_instruction}",
    input_variables=['lord'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'lord':'Shree Krishna'})

print(result)

