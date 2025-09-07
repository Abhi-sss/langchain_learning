from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()



model = ChatMistralAI(model="ministral-8b-latest")

parser = StrOutputParser()

topic = 'CrewAI'


# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

# prompt1 = template1.invoke({'topic':'crewai'})

# result = model.invoke(prompt1)

# prompt2 = template2.invoke({'text':result.content})

# result1 = model.invoke(prompt2)


chain = template1 | model | parser | template2 | model | parser 

result = chain.invoke({'topic':'CrewAI'})

print(result)
