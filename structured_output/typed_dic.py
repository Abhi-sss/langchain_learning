from langchain_mistralai import ChatMistralAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Annotated, Literal, Optional, TypedDict


load_dotenv()


model = ChatMistralAI(model="ministral-8b-latest")

class Summary(TypedDict):

    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    key_discussion: Annotated[list[str], "Write down all the main topic discussed in the conversation in the list"]
    summary: Annotated[str, "A brief summary of the conversation"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]
    name: Annotated[list[str], "Write the name of the persons having conversation"]


structured_model = model.with_structured_output(Summary)

result = structured_model.invoke(""" Rahul: Hey Shubham! Long time no see. How have you been?

Shubham: Hey Rahul! I’ve been good, just busy with work. What about you?

Rahul: Same here. Work’s been hectic lately. We definitely need a break.

Shubham: Totally agree. How about we catch up this weekend? Maybe grab a coffee?

Rahul: That sounds perfect. Saturday afternoon?

Shubham: Done. I’ll text you the place. Looking forward to it!

Rahul: Me too, bro. See you then!""")

print(result)