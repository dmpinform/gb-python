def _upper(word):
    if len(word) == 0:
        return ""
    return word[0].upper() + word[1:]
    # return word.capitalize()


def upper_words(words):
    return " ".join(map(_upper, words.split(" ")))


mys = input("Enter words separated by a space : ")
print(upper_words(mys))
