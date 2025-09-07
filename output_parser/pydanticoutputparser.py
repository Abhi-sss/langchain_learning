from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatMistralAI(model="ministral-8b-latest", temperature=0)


class college(BaseModel):
    city : list[str] = Field("City of the college where it is situated")
    year : int = Field("Year of establishment of that college")
    ranking : Optional[int] = Field("Nirf ranking of that college")

parser = PydanticOutputParser(pydantic_object=college)

template = PromptTemplate(
    template="Write the city, year of establisment and ranking of the {college} /n {format_instruction}",
    input_variables=['college'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

chain = template | model | parser

result = chain.invoke({'college':'Manipal Institute of Technology'})

print(result) 

