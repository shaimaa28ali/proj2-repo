from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
 
load_dotenv()
 

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
 
summarizer_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
You are a helpful task assistant.
 
Summarize the following tasks clearly and briefly.
 
Tasks:
{text}
 
Summary:
"""
)
 
summarizer_chain = summarizer_prompt | llm
 
tasks = """
I need to finish my Python assignment.
I have to study for my AI exam tomorrow.
I need to attend a cybersecurity lecture at 10 AM.
I must submit my project by Friday.
"""

result = summarizer_chain.invoke({
    "text": tasks
})
 
print("SUMMARY:")
print(result.content)