import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as gen

load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGSMITH_TRACING_V2']="true"

## Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "You are Sherlock Holmes, an experienced detective. "
        "Stick to the charecter of sherlock holmes as described by sir aurther conan doyle."
        "Answer queries directly and concisely. Do not include internal reasoning or any section labeled <think>...</think>. "
        "Only return the final answer."
    )),
    ("user", "Query: {question}")
])

## streamlit framework
gen.title('The Dying Detective')
input_text=gen.text_input('Whats your problem????')


#LLM
llm = ChatGroq(
    model='llama3-70b-8192'
)
outparser=StrOutputParser()
chain=prompt|llm|outparser

if input_text:
    gen.write(chain.invoke({"question":input_text}))
