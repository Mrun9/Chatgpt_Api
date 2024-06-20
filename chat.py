#py -m pip install openai : //do this in terminal
import openai

def chat_function(prompt, model):
    #openai.api_key = 'secret key goes here'

    response = openai.chat.completions.create(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
        stream=True
    )  


    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")

# Usage
if __name__ == "__main__":
    prompt = "hello"
    chat_function(prompt, 'gpt-4o')