import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API KEY KAHAN HAI BHAI")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="Suggest A name for my food company"
# System
message_System={
    "role":"system",
    "content":"You are a brand manager who suggests name for a company.The name should be of one word."
}

message={
    "role":role,
    "content":prompt
}

messages=[message_System,message]
# Temperature default is zero meaning safe
# Increase the temperature to increase the creativity of the model
response=client.chat.completions.create(model=model,messages=messages,temperature=0)

#print(response)

print("#################################################################################################")

answer=response.choices[0].message.content

print(answer)