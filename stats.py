def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    counts = {}

    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts


def sort_on(item):
    return item["num"]

def sort_char_counts(char_counts):
    chars_list = []

    for char, count in char_counts.items():
        chars_list.append({"char": char, "num": count})

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
