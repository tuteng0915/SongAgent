from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen3-8B"

tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    cache_dir='/data/guozl/models',
    trust_remote_code=True,
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="cuda",
    trust_remote_code=True,
    cache_dir='/data/guozl/models'
)
