def get_num_words(text: str) -> int:
    return len(text.split())

def get_char_counts(text: str) -> dict:
    char_dict = {}
    for char in text:
        c = char.lower()
        if not char_dict.get(c):
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    return char_dict

def sort_dict(d: dict) -> list:
    l = [{"char": k, "num": v} for k, v in d.items() if k.isalpha()]
    sort_val = lambda d: d["num"]
    l.sort(reverse=True, key=sort_val)
    return l