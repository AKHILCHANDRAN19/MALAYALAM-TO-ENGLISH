from googletrans import Translator

# Initialize translator
translator = Translator()

# Function to split text into manageable chunks
def split_text(text, max_length=5000):
    words = text.split()
    chunks = []
    chunk = ""
    for word in words:
        if len(chunk) + len(word) + 1 > max_length:
            chunks.append(chunk.strip())
            chunk = word
        else:
            chunk += " " + word
    chunks.append(chunk.strip())
    return chunks

# Prompt user for input
print("Enter your Malayalam text line by line. Type 'done' when you're finished:")

# Collect user input
input_lines = []
while True:
    line = input()
    if line.strip().lower() == "done":
        break
    input_lines.append(line)

# Combine all input lines into one paragraph
malayalam_text = " ".join(input_lines)

# Split text into manageable chunks
text_chunks = split_text(malayalam_text)

# Translate each chunk and combine results
translated_chunks = [translator.translate(chunk, src='ml', dest='en').text for chunk in text_chunks]
translated_text = " ".join(translated_chunks)

# Show the result
print("\nTranslated Text:")
print(translated_text)
