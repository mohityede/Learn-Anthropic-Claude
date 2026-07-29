from anthropic import Anthropic
from anthropic.types import MessageParam
from typing import Iterable

def call_llm(llm:Anthropic,messages:Iterable[MessageParam]):
    response = llm.messages.create(
        model="gemini",
        max_tokens=5000,
        system="You are a concise assistant. Always respond in exactly one sentence.",
        messages=messages
    ) 

    return response.content[0].text

def add_user_prompt(messages,prompt):
    user_prompt = {"role":"user","content":prompt}
    messages.append(user_prompt)

def add_assistant_prompt(messages,prompt):
    assistant_prompt = {"role":"assistant","content":prompt}
    messages.append(assistant_prompt)

def chat_exercise(llm):
    # without history
    messages=[]

    print("saying Hi...")
    # user_prompt = [{"role":"user","content":"Hi! My name is mohit"}]
    add_user_prompt(messages,"Hi! My name is mohit")
    response = call_llm(llm,messages)
    print(response)
    add_assistant_prompt(messages,response)


    print("Asking about vector DB...")
    # user_prompt = [{"role":"user","content":"tell me something about vector database"}]
    add_user_prompt(messages,"tell me something about vector database")
    response = call_llm(llm,messages)
    print(response)
    add_assistant_prompt(messages,response)

    print("Asking about past details...")
    # user_prompt = [{"role":"user","content":"what is my name? and we were talking about what?"}]
    add_user_prompt(messages,"what is my name? and we were talking about what?")
    response = call_llm(llm,messages)
    print(response)

    print("\n----------------------------\n")
    print(messages)