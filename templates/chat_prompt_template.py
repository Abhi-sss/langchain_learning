from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'you are HR in the {company}'),
    ('human','you have to tell the hiring process for the {role} in your organization')
])

prompt = chat_template.invoke({'company':'EY', 'role':'Data Scientist'})
print(prompt)