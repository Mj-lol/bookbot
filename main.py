def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    list = file_contents.split()
    num = list.__len__()
    dic = {}
    alphabet = "qwertyuioplkjhgfdsazxcvbnm"
    for char in alphabet:
        dic[char]=0;
    for char in file_contents.lower():
        if char not in alphabet:
            continue
        dic[char]+=1
    print(f"--- Begin report of {path} ---")
    print(f"{num} words found in the document")
    for char in alphabet:
        print(f"The '{char}' character was found {dic[char]} times")
    # i prefer reading them in qwerty order but alternative in frequency order:
    # sordic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    # for key in sordic:
    #     print(f"the '{key}' character was found {sordic[key]} times")

main()
