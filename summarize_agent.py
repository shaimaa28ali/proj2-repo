from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
 
# Load the API key
load_dotenv()
 
# Create the AI model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
 
# Read the text file
with open("tasks.txt", "r") as file:
    tasks = file.read()
 
# Prompt
prompt = PromptTemplate(
    input_variables=["tasks"],
    template="""
You are an AI Task Planner.
 
Read the following tasks and provide a short summary.
 
Tasks:
{tasks}
 
Summary:
"""
)
 
# Create the chain
chain = prompt | llm
 
# Run it
result = chain.invoke({"tasks": tasks})
 
print("\n===== TASK SUMMARY =====\n")
print(result.content)