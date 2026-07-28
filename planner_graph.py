from typing import TypedDict
 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
import os
 
load_dotenv()

k=os.getenv("OPENAI_API_KEY")
print(k)
 
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key= k
)
 

class PlannerState(TypedDict):
    tasks: str
    summary: str
    category: str
    priority: str
    smart_plan: str
 
def summarize_node(state: PlannerState):
 
    response = llm.invoke(f"""
Summarize these tasks:
 
{state["tasks"]}
""")
 
    return {
        **state,
        "summary": response.content
    }
 
 
def classify_node(state: PlannerState):
 
    response = llm.invoke(f"""
Classify these tasks into ONE category:
 
- Work
- Study
- Personal
 
Tasks:
 
{state["summary"]}
 
Category:
""")
 
    return {
        **state,
        "category": response.content
    }
 
def priority_node(state: PlannerState):
 
    response = llm.invoke(f"""
Prioritize these tasks.
 
Return High, Medium or Low priority with a short explanation.
 
Tasks:
 
{state["summary"]}
""")
 
    return {
        **state,
        "priority": response.content
    }
 
 
def plan_node(state: PlannerState):
 
    response = llm.invoke(f"""
Using the following information:
 
Summary:
{state["summary"]}
 
Category:
{state["category"]}
 
Priority:
{state["priority"]}
 
Create a smart plan in the best order.
""")
 
    return {
        **state,
        "smart_plan": response.content
    }
 
 
graph = StateGraph(PlannerState)
 
graph.add_node("summarize", summarize_node)
graph.add_node("classify", classify_node)
graph.add_node("priority", priority_node)
graph.add_node("plan", plan_node)
 
graph.add_edge(START, "summarize")
graph.add_edge("summarize", "classify")
graph.add_edge("classify", "priority")
graph.add_edge("priority", "plan")
graph.add_edge("plan", END)
 
planner = graph.compile()
 
 
 
result = planner.invoke(
    {
        "tasks": """
Finish Python assignment.
Study AI.
Buy groceries.
Submit project Friday.
Attend cybersecurity lecture.
""",
        "summary": "",
        "category": "",
        "priority": "",
        "smart_plan": "",
    }
)
 
 
print("\n========== AI TASK PLANNER ==========\n")
 
print("SUMMARY\n")
print(result["summary"])
 
print("\nCATEGORY\n")
print(result["category"])
 
print("\nPRIORITY\n")
print(result["priority"])
 
print("\nSMART PLAN\n")
print(result["smart_plan"])