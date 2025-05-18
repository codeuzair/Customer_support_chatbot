# from config.config_loader import load_config

# config=load_config()

# collection_name = config["astra_db"]["collection_name"]
# embedding_model_name = config["embedding_model"]["model_name"]
# top_k = config["retriever"]["top_k"]

# print(collection_name)
# print(embedding_model_name)
# print(top_k)

from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Set API key directly (not recommended for production)
os.environ["GOOGLE_API_KEY"] = "AIzaSyDCf5DanxUoQwzGKZrvBv8q4UIHGJsysb0"

# Initialize the model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.5
)

# Invoke the model
res = llm.invoke("Tell me a joke.")
print(res)
