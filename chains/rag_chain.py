from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.output_parsers import StrOutputParser

from chains.prompts import support_prompt

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

parser = StrOutputParser()

rag_chain = support_prompt | llm | parser  