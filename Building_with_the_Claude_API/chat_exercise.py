from anthropic import Anthropic
from anthropic.types import MessageParam
from typing import Iterable

def call_llm(llm:Anthropic,messages:Iterable[MessageParam]):
    response = llm.messages.create(
        model="gemini",
        max_tokens=5000,
        system="You are a concise assistant. Always respond in exactly one sentence.",
        messages=messages,
        temperature=0.2
    ) 

    return response.content[0].text

def add_user_prompt(messages,prompt):
    user_prompt = {"role":"user","content":prompt}
    messages.append(user_prompt)

def add_assistant_prompt(messages,prompt):
    assistant_prompt = {"role":"assistant","content":prompt}
    messages.append(assistant_prompt)

def call_llm_stream(llm:Anthropic):
    messages=[]
    # prompt = input("> ")
    user_prompt = {"role":"user","content":"what is vector database?"}
    messages.append(user_prompt)

    with llm.messages.stream(
        model='local',
        max_tokens=500,
        messages=messages
    ) as stream:
        for chunk in stream.text_stream:
            print(chunk,end="")

    response = stream.get_final_message()
    add_assistant_prompt(messages,response.content[0].text)

def get_structured_output(llm:Anthropic):
    messages = []
    user_prompt = {"role":"user","content":"generate very short data as json"}
    messages.append(user_prompt)

    assistant_prompt = {"role":"assistant","content":"```json"}
    messages.append(assistant_prompt)

    response = llm.messages.create(
        model='gemini',
        max_tokens=5000,
        messages=messages,
        stop_sequences=["```"]
    )

    print(response.content[0].text)

def chat_exercise(llm):
    # without history
    messages=[]

    while(True):
        inp = input("You > ")
        if(inp=='bye'):
            break

        add_user_prompt(messages,inp)
        response=call_llm(llm,messages)
        print("AI > "+response)
        add_assistant_prompt(messages,response)


    # # print("saying Hi...")
    # # user_prompt = [{"role":"user","content":"Hi! My name is mohit"}]
    # add_user_prompt(messages,"Hi! My name is mohit")
    # response = call_llm(llm,messages)
    # print(response)
    # add_assistant_prompt(messages,response)


    # # print("Asking about vector DB...")
    # # user_prompt = [{"role":"user","content":"tell me something about vector database"}]
    # add_user_prompt(messages,"tell me something about vector database")
    # response = call_llm(llm,messages)
    # print(response)
    # add_assistant_prompt(messages,response)

    # # print("Asking about past details...")
    # # user_prompt = [{"role":"user","content":"what is my name? and we were talking about what?"}]
    # add_user_prompt(messages,"what is my name? and we were talking about what?")
    # response = call_llm(llm,messages)
    # print(response)

    print("\n----------------------------\n")
    print(messages)