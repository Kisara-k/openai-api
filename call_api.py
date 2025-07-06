from dotenv import load_dotenv
import os

load_dotenv()
openai_key = os.getenv('OPENAI_KEY')

from openai import OpenAI
client = OpenAI(api_key=openai_key)

import importlib
import config

config = importlib.reload(config)
globals().update({k: getattr(config, k) for k in ['system_prompt', 'user_prompt', 'user_prompt_2', 'clean']})

import time
start = time.time()

completion = client.chat.completions.create(
    model="gpt-4.1-mini",  # Use "gpt-4o" for the latest turbo model
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.3,  # Adjust for more creative or deterministic output
    max_tokens=10000,  # Increase this if responses are getting cut off
    top_p=0.3,
    frequency_penalty=0,
    presence_penalty=0
)

elapsed = time.time() - start
print(f"Completion took {elapsed:.2f} seconds")

from IPython.display import Markdown, display
display(Markdown(clean(completion.choices[0].message.content)))

# Save Content

filepath = os.path.join("outputs", "DM 00 Introduction.md")

content = clean(completion.choices[0].message.content)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

text_1 = completion.choices[0].message.content

completion_2 = client.chat.completions.create(
    model="gpt-4.1-mini",  # Use "gpt-4o" for the latest turbo model
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
        {"role": "assistant", "content": text_1},
        {"role": "user", "content": user_prompt_2},
    ],
    temperature=0.3,  # Adjust for more creative or deterministic output
    max_tokens=10000,  # Increase this if responses are getting cut off
    top_p=0.3,
    frequency_penalty=0,
    presence_penalty=0
)

from IPython.display import Markdown, display
display(Markdown(completion_2.choices[0].message.content))

# Save Content

filepath = os.path.join("outputs", "DM 00 Lec.md")

content = clean(completion_2.choices[0].message.content)
with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

