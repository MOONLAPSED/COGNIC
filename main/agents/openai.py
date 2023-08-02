import openai

openai.api_base = "http://localhost:8080/v1"

# create a chat completion
def local_chat_completion(model, messages):
    # Replace with local API call
    return openai.ChatCompletion.create(model=model, messages=messages)

chat_completion = local_chat_completion(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

# create a search
def local_search(documents, query):
    # Replace with local API call
    return openai.Search.create(documents=documents, query=query)

search_result = local_search(documents=["Document 1", "Document 2"], query="Query")

# print the completion
print(chat_completion.choices[0].message.content)