import os
import time
import importlib

from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display

import config

load_dotenv()
openai_key = os.getenv('OPENAI_KEY')
client = OpenAI(api_key=openai_key)

# Reload and import configuration - directly import in production

config = importlib.reload(config)
globals().update({k: getattr(config, k) for k in [
    'system_prompt', 'user_prompt_1', 'user_prompt_2', 'lecture_content', 'clean']})

user_prompt_1 += lecture_content

def generate(messages, model='gpt-4.1-mini'):
    start = time.time()
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.3,  # Adjust for more creative or deterministic output
        max_tokens=10000,  # Increase this if responses are getting cut off
        top_p=0.3,
        frequency_penalty=0,
        presence_penalty=0
    )

    elapsed = time.time() - start
    print(f"Completion took {elapsed:.2f} seconds")

    return completion.choices[0].message.content, completion

text_1, completion_1 = generate([
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt_1}])

display(Markdown(clean(text_1)))

# Save Content

filepath = os.path.join("outputs", "DM 00 Introduction.md")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(clean(text_1))

text_2, completion_2 = generate([
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt_1},
    {"role": "assistant", "content": text_1},
    {"role": "user", "content": user_prompt_2},])

display(Markdown(text_2))

# Save Content

filepath = os.path.join("outputs", "DM 00 Lec.md")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(text_2)

