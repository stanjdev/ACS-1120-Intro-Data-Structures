import random
from histogram import read_file, histogram_dict

""" 
PSEUDOCODE:
take in file
get dict histogram from it,
loop through each value (number) of the histogram,

fill out another dict with keys as numbers auto-incrementing, and their values are the words
OR
randomly pick a number, then count up to that number in the accumulating histogram numbers
end boundary can be all histogram numbers summed
pick a random number within that bound
iterate the histogram word by word summing their values and 
keep checking if the random number is less than or equal to the current sum. That's your word!

 """


# words_list = read_file(file).split()
# histogram = histogram_dict(words_list)
# length = len(words_list)


# ACCUMULATION METHOD
def sampler(words_list):
  histogram = histogram_dict(words_list)
  length = len(words_list)
  random_number = random.randint(1, length) # dart
  # print(random_number)

  sum = 0 # target
  for key in histogram:
    sum += histogram[key]
    if sum >= random_number:
      return key


def test_sampler(histogram):
  histogram_samples = {}
  for i in range(10000):
    selected_word = sampler(histogram)
    if selected_word in histogram_samples:
      histogram_samples[selected_word] += 1
    else:
      histogram_samples[selected_word] = 1
  return histogram_samples


if __name__ == '__main__':
  # print(sampler())
  print(test_sampler())



# # DUPLICATION METHOD
# def throw_dart(list_of_words):
#   hist = histogram_dict(list_of_words)
#   word_line = []
#   for key in hist:
#     for i in range(hist[key]):
#       word_line.append(key)
#   rand_index = random.randint(0, len(word_line) - 1)
#   return word_line[rand_index]

# def sampler():
#   words_list = read_file(file).split()
#   histogram_samples = {}
#   for i in range(10000):
#     selected_word = throw_dart(words_list)
#     if selected_word in histogram_samples:
#       histogram_samples[selected_word] += 1
#     else:
#       histogram_samples[selected_word] = 1
#   return histogram_samples



  

""" 
Stochastic Sampling, 
Accumulate word count through list
where a uniform random number splits it

Distillation (values of)
fenceposts, denoting where the certain words occur

If I roll a 3, ask "what is number greater than and what's the next fencepost?"


1 2 3 4 5 6 7 8
|       | | | |
one     fish, etc..

choose a random number, then iterate the list and check if the random number is less than current fence post. 

3 less than 0? no

3 less than 5? yes. stop

7 less than


Generate a dart to throw on the number line, and return a word.
randint(1, 8) hits only the fence posts.

random.random could do floating point. like 1.3, 7.8

random.uniform(0, 8)
- returns floating point values, that don't hit the outer fence posts.


loop through object, make a list writing out how many times each word appears, then throw a dart.

 """





