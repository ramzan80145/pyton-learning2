sentence = "apple banana apple orange banana apple"
words = sentence.split()  # Splits the text into a list of words

counts = {}

for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

print(counts)