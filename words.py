def print_upper_words(words_list):
    # print("hello")
    for word in words_list:
        print(word.upper())


# print_upper_words(["Programming", "is", "pretty", "fun"])


def print_upper_words(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word)


def print_upper_words3(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break


                # break
print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
                   must_start_with=["A", "E"])
