# https://tech-at-du.github.io/Tweet-Generator/#/P10-Markov-Chains-Revisited/README
from histogram import histogram_dict, read_file
from dictogram import Dictogram
from tokens import tokenize
# file = './data/fish.txt'
# file = './data/dogs_cats.txt'
file = './data/socrates-apology.txt'
word_list = tokenize(read_file(file))
print(word_list)

ORDER = 2

def markov_chain_generator(corpus):
    markov_dict = {}
    for i in range(len(corpus)):
        word = corpus[i]
        next_word = corpus[(i + 1) % len(corpus)]
        tup = tuple([word, next_word])
        token = corpus[(i + ORDER) % len(corpus)]
        """ 
        [
            ((I, like), dogs), 
            ((like, dogs), and), -- the tuple 'window'
        ] 
         """

        if tup not in markov_dict:
            histogram = Dictogram()
            histogram.add_count(token)
            markov_dict[tup] = histogram
        else:
            markov_dict[tup].add_count(token)
    return markov_dict

def walk(markov_chain_dict, char_limit = 140):
    tweet = ''
    start = next(iter(markov_chain_dict))[0]
    second_word = next(iter(markov_chain_dict))[1]
    tweet += start + " " + second_word

    while len(tweet) < char_limit:
        tweet_list = tweet.split()
        # print(tweet_list)
        last_word = tweet_list[-1]
        last_last_word = tweet_list[-2]
        # print(last_word, last_last_word)
        tup = tuple([last_last_word, last_word])
        # print(tup)
        last_word_histogram = markov_chain_dict[tup]
        # print(last_word_histogram)
        next_word = last_word_histogram.sample()
        # print(next_word)
        tweet += ' ' + next_word
        # print(tweet)
    return tweet


if __name__ == '__main__':
    markov_chain = markov_chain_generator(word_list)
    # print(markov_chain)
    tweet = walk(markov_chain)
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



pseudocode

def create_markov(word_list):
    take in a word list
    iterate every two words (if they exist)
    [i]
    [i + 1]
    put both words in a tuple
    Check if this tuple was in a dictionary, 
        if it was, increment the count for the next word (+1)
        else: make a new entry with the value being the next word initialized to 1
    return markov chain

markov_chain = create_markov(word_list)

example = {
    (cats, I) : {
        like: 1
    },
    (I, like): {
        dogs: 1,
        cats: 1
    },
    (like, dogs): {
        and: 1,
    },
}

seed the first word to be the first word of the word list ("I")
sentence = wordlist[0]
"I like dogs"

loop for until we hit our sentence length limit:
    check if sentence[-1] is in any of the tuples[1] keys in our markov_chain,
    and then use sample() function to choose the next word from that histogram,
    append that word to the sentence
return sentence











 """
