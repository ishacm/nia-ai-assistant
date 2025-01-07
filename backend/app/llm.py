from .config import Config
from transformers import pipeline
from huggingface_hub import login
import os
from .config import Config
from huggingface_hub import HfApi

# Replace with your token
token = "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"

# Initialize the API
api = HfApi(token=token)

# Test the token
try:
    user_info = api.whoami()
    print("Logged in as:", user_info["name"])
except Exception as e:
    print("Error:", e)

# Log in to Hugging Face
login(token=Config.HUGGINGFACE_API_KEY)

# Load the LLAMA 2 model
llm_pipeline = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")

def generate_response(query, context=None):
    prompt = f"User: {query}\nContext: {context}\nAssistant:"
    response = llm_pipeline(prompt, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']

