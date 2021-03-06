from histogram import histogram_dict, read_file
# file = './data/fish.txt'
file = './data/socrates-apology.txt'
word_list = read_file(file).replace(',', '').replace('.', '').replace('?', '').replace('"', '').replace('”', '').replace('’', '').replace('`', '').replace('!', '').replace('/', '').replace(';', '').replace(':', '').lower().split()

from dictogram import Dictogram

def dict_of_histograms_generator(word_list):
    start = word_list[0]
    dict_of_histograms = {}
    for i in range(len(word_list) - 1):
        word = word_list[i]
        next_word = word_list[i + 1]
        if word not in dict_of_histograms:
            histogram = Dictogram()
            histogram.add_count(next_word)
            dict_of_histograms[word] = histogram
        else:
            dict_of_histograms[word].add_count(next_word)
    return dict_of_histograms

def tweet_generator(markov_chain_dict):
    tweet = ''
    start = next(iter(markov_chain_dict))
    tweet += start
    char_limit = 140

    while len(tweet) < char_limit:
        tweet_list = tweet.split()
        last_word = tweet_list[-1]
        last_word_histogram = markov_chain_dict[last_word]
        next_word = last_word_histogram.sample()
        tweet += ' ' + next_word
    return tweet


if __name__ == '__main__':
    markov_chain = dict_of_histograms_generator(word_list)
    tweet = tweet_generator(markov_chain)
    print(tweet)

