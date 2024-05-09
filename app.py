from langchain_openai import ChatOpenAI,AzureChatOpenAI,AzureOpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
# ## Langmith tracking
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=AzureChatOpenAI(
    streaming=False,
    openai_api_key="d8bd990c34974f8fa34c5e0fe1a37483",
    azure_endpoint="https://caedaoipocaoa0c.openai.azure.com",
    openai_api_type="azure",
    openai_api_version="2023-03-15-preview",
    deployment_name="DDIAIGPT4"
)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))