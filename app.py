
import openai
import gradio as gr


client = openai.AzureOpenAI(
      azure_endpoint = "https://caedaoipocaoa0c.openai.azure.com",
      api_key="d8bd990c34974f8fa34c5e0fe1a37483", # api_key is required, but unused for local models
      api_version="2023-03-15-preview", # version
      
      
  )

def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})
  
    response = client.chat.completions.create(model='DDIAIGPT4',
    messages= history_openai_format,
    temperature=1.0,
    stream=True)

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
              partial_message = partial_message + chunk.choices[0].delta.content
              yield partial_message

gr.ChatInterface(predict).launch()
