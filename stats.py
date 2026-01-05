def count_words(text):
    words = len(text.split())
    return f"Found {words} total words"

def count_characters(text):
    characters = {}
    for i in range(0, len (text)):
        c = text[i].lower()
        if c not in characters:
            characters[c] = 0
        characters[c] += 1
    return characters

def sort_count_characters(count_dict):
    sorted_count = []
    for c in count_dict:
        sorted_count.append({"char": c, "num": count_dict[c]})
    def sort_on(items):
        return items["num"]
    sorted_count.sort(reverse = True, key = sort_on)
    return sorted_count