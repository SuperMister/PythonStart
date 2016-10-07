"""Acronym making"""




def not_allowed_characters_check(text, chars):
    text = text.lower()
    for i in text:
        if(i not in chars and  i != " "):
            return True
    return False


def len_of_list(text):
    return len(text.split())


def acronym(text, chars, nr_of_words_limit):
    if not_allowed_characters_check(text, chars):
        return "Input: " + "\"" + text + "\"" + " contains not allowed characters!"
    if len_of_list(text) > nr_of_words_limit:
        return "Input: " + "\"" + text + "\"" + " is too long (max length is " + str(nr_of_words_limit) + " words)!"
    text = text.split()
    letters = ""
    for every_word in text:
        letters += every_word[0]
    letters = letters.upper()
    return letters

def main():
    nr_of_words_limit = 2
    chars = "abcdefghijklmnopqrstuvwõäöüxyz"
    print(acronym("Kas Kersti Kaljulaid saab 228Eesti uueks presidendiks", chars, nr_of_words_limit))
main()