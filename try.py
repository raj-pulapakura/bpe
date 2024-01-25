from train import BPETokenizer

tokenizer = BPETokenizer()
tokenizer.load_from_json("tokenizer.json")

print("\n==================")
print("Byte Pair Encoding")
print("==================\n")

while True:
    text = input("Enter your text: ")
    if text == "":
        continue
    tokens = tokenizer.tokenize(text)
    print(f"Integer Tokens: {tokens}")
    print(f"Text Tokens: {[tokenizer.itotok[i] for i in tokens]}")
    print()