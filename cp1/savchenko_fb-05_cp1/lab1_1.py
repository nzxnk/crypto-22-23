import math

def frequency_letter(text):
    text = text.lower()
    letter_counts = {}
    for letter in text:
        if letter.isalpha():
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    total_letters = sum(letter_counts.values())
    letter_freqs = {letter: count/total_letters for letter, count in letter_counts.items()}
    return letter_freqs


def frequency_bigram(text):
    text = text.lower()
    bigram_counts = {}
    for i in range(len(text)-1):
        if text[i].isalpha() and text[i+1].isalpha():
            bigram = text[i] + text[i+1]
            if bigram in bigram_counts:
                bigram_counts[bigram] += 1
            else:
                bigram_counts[bigram] = 1
    total_bigrams = sum(bigram_counts.values())
    bigram_freqs = {bigram: count/total_bigrams for bigram, count in bigram_counts.items()}
    return bigram_freqs

def entropy(freqs):
    entropy = 0
    for freq in freqs.values():
        if freq > 0:
            entropy -= freq * math.log2(freq)
    return entropy

text = "Этот текст содержит в себе какие-то странные штуки, не смотрите сюда и не испугаетесь. А ещё я люблю котиков <3"
letter_freqs = frequency_letter(text)
bigram_freqs = frequency_bigram(text)
letter_entropy = entropy(letter_freqs)
bigram_entropy = entropy(bigram_freqs)

print("Частота букавок:", letter_freqs)
print("Частота биграмм:", bigram_freqs)
print("Энтропия букавок:", letter_entropy)
print("Энтропия биграм:", bigram_entropy)

input("Тыкни лапкой что бы закрыть консоль...")