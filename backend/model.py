from transformers import pipeline

# Load a pre-trained text-generation model (fine-tuning can be done later)
generator = pipeline("text-generation", model="gpt2")

def generate_folk_tale(region, theme):
    prompt = f"A folk tale from {region} about {theme}:"
    response = generator(prompt, max_length=300, num_return_sequences=1)
    return response[0]["generated_text"]
