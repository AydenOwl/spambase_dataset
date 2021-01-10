# percentage of words in the e-mail that match WORD, i.e. 100 * (number of times the WORD appears in the e-mail) / total number of words in e-mail.
# A "word" in this case is any string of alphanumeric characters bounded by non-alphanumeric characters or end-of-string.
def get_frequency_of_word(word: str, text: str):
    text_splitted = text.split()
