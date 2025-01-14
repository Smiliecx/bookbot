def num_words(all_text):
    text_to_array = all_text.split()
    return len(text_to_array)

def character_count(all_text):
    lower = all_text.lower()
    char_dicts = {}

    for char in lower:
        if (char in char_dicts):
            char_dicts[char] += 1
        else:
            char_dicts[char] = 1
    
    return char_dicts

def sort_on(dict):
    return dict["num"]

def to_char_count_list(character_count):
    list_of_counts = []
    for key, value in character_count.items():
        if not key.isalpha():
            continue
        list_of_counts.append({"name": key, "num": value})
    
    list_of_counts.sort(reverse=True, key=sort_on)
    return list_of_counts

def print_char_list(char_list):
    for dict in char_list:
        print(f"The '{dict["name"]}' character was found {dict["num"]} times")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        nw = num_words(file_contents)
        cc = character_count(file_contents)
        char_list = to_char_count_list(cc)
        print("--- Begin report of books/frankenstein.txt")
        print(f"{nw} words found in the document")
        print_char_list(char_list)
        print("--- End report ---")

main()