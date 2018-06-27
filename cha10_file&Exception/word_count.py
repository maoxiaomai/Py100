def count_words(filename):
    """jisuan"""
    try:
        with open(filename) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filenames=['alice.txt', 'programming.txt', 'abc.txt']
for filename in filenames:
    count_words(filename)