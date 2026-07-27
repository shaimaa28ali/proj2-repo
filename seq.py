from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os


load_dotenv()
mykey = os.getenv('OPENAI_API_KEY')

print(mykey)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key = mykey
    
)
 

 
summarizer_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Summarize the following text clearly and briefly.
 
Text:
{text}
 
Summary:
"""
)
 
summarizer_chain = summarizer_prompt | llm
 

 
def count_words(summary):
    return len(summary.split())
 

 
classifier_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Classify the following text into ONE of these categories:
 
- Education
- Business
- Health
- Technology
- Personal
- Other
 
Text:
{text}
 
Category:
"""
)
 
classifier_chain = classifier_prompt | llm
 

 
text = """
I am a university student studying computer science.
I need to complete my Python assignment, study for my AI exam,
attend a cybersecurity lecture, and submit my final project by Friday.
"""
 

 
summary_response = summarizer_chain.invoke({
    "text": text
})
 
summary = summary_response.content
 

 
word_count = count_words(summary)
 

 
classification_response = classifier_chain.invoke({
    "text": summary
})
 
classification = classification_response.content
 

 
print("\n==============================")
print("SEQUENTIAL CHAIN RESULTS")
print("==============================")
 
print("\nOriginal Text:")
print(text)
 
print("\nSummary:")
print(summary)
 
print("\nWord Count of Summary:")
print(word_count)
 
print("\nTopic Classification:")
print(classification)