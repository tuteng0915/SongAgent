from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
import torch

tokenizer = AutoTokenizer.from_pretrained(
    "Qwen/Qwen-Audio-Chat",
    trust_remote_code=True,
)

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-Audio-Chat",
    device_map="cuda",
    trust_remote_code=True,
)

def ask_qwen_audio(audio, text):
    query = tokenizer.from_list_format([
        {'audio': audio},
        {'text': text},
    ])

    response, history = model.chat(tokenizer, query=query, history=None)
    return response
