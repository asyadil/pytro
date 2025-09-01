import os
os.system('cls' if os.name == 'nt' else 'clear')
# Make sure to install the transformers library first:
#pip install transformers

from transformers import AutoModelForCausalLM, AutoTokenizer

# Inisialisasi pipeline NLP untuk question-answering/chat
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def chatbot(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=128, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    class Response:
        generated_responses = [response]
    return Response()

def jawab(pertanyaan):
    # Menggunakan model NLP untuk menjawab pertanyaan
    response = chatbot(pertanyaan)
    return response.generated_responses[-1]

def main():
    print("Halo! Saya adalah model bahasa sederhana. Ketik 'keluar' untuk berhenti.")
    while True:
        user_input = input("Anda: ")
        if user_input.lower() == "keluar":
            print("Sampai jumpa!")
            break
        print("Bot:", jawab(user_input))

if __name__ == "__main__":
    main()
