path = "books/frankenstein.txt"

def sort_on(dict):
    return dict["value"]

with open(path) as f:
    file_contents = f.read()
    file_contents = file_contents.lower()
    words = file_contents.split()
    word_count =dict()
    for word in words:
        for w in word:
            if not w.isalpha():
                continue
            if w not in word_count:
                word_count[w] =1
            else:
                word_count[w] = word_count[w] + 1
    list_of_dicts = [{'key': k, 'value': v} for k, v in word_count.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path} ---")
    print(f"{len(words)} words found in the document\n")
    for dict in list_of_dicts:
        print(f"The '{dict['key']}' character was found {dict['value']} times")
    
    print("--- End report ---")