# https://tech-at-du.github.io/Tweet-Generator/#/P10-Markov-Chains-Revisited/README
from histogram import histogram_dict, read_file
from dictogram import Dictogram
# file = './data/fish.txt'
file = './data/dogs_cats.txt'
# file = './data/socrates-apology.txt'
word_list = read_file(file).replace(',', '').replace('.', '').replace('?', '').replace('"', '').replace('”', '').replace('’', '').replace('`', '').replace('!', '').replace('/', '').replace(';', '').replace(':', '').lower().split()


def dict_of_histograms_generator(word_list):
    start = word_list[0]
    dict_of_histograms = {}
    for i in range(len(word_list) - 2):
        word = word_list[i]
        next_word = word_list[i + 1]

        tup = tuple([word, next_word])
        last_word = tup[1]
        next_next_word = word_list[i + 2]

        # I think I want to be able to search every histogram's key only the [1] index position of each tuple? 
        if tup not in dict_of_histograms:
            histogram = Dictogram()
            histogram.add_count(next_next_word)
            dict_of_histograms[tup] = histogram
        else:
            dict_of_histograms[tup].add_count(next_next_word)

        # if word not in dict_of_histograms:
        #     histogram = Dictogram()
        #     histogram.add_count(next_word)
        #     dict_of_histograms[word] = histogram
        # else:
        #     dict_of_histograms[word].add_count(next_word)
    return dict_of_histograms

def tweet_generator(markov_chain_dict):
    tweet = ''
    start = next(iter(markov_chain_dict))[0]
    second_word = next(iter(markov_chain_dict))[1]
    tweet += start + " " + second_word
    char_limit = 140

    while len(tweet) < char_limit:
        tweet_list = tweet.split()
        last_word = tweet_list[-1]
        last_last_word = tweet_list[-2]
        tup = tuple([last_last_word, last_word])
        last_word_histogram = markov_chain_dict[tup]
        next_word = last_word_histogram.sample()
        tweet += ' ' + next_word
    return tweet


if __name__ == '__main__':
    markov_chain = dict_of_histograms_generator(word_list)
    tweet = tweet_generator(markov_chain)
    print(tweet)




class Queue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue):
            return self.queue.pop(0)
        else:
            raise ValueError('Queue is empty. Cannot dequeue.')
        
    





""" 
RESULTING DICT:

“I like dogs and you like dogs. I like cats but you hate cats.”

{
    (I, like): {
        dogs: 1
    },
    (like, dog) {
        
    }
}


{
    (“I”, “like”): {
        “dogs”: 2,
        “cats”: 1
    },
    (“like”, “dogs”): {
        “I”: 1,
        “and”: 1
    },
    (“like”, “cats”): {
        “but”: 1
    },
    (“dogs”, “I”): {
        “like”: 1
    },
    (“dogs”, “and”): {
        “you”: 1
    },
    (“and”, “you”): {
        “like”: 1
    },
    (“you”, “like”): {
        “dogs”: 1
    },
    (“cats”, “but”): {
        “you”: 1
    },
    (“but”, “you”): {
        “hate”: 1
    },
    (“you”, “hate”): {
        “cats”: 1
    },
    (“hate”, “cats”): {
        “I”: 1
    },
    (“cats”, “I”): {
        “like”: 1
    },
}

 """
