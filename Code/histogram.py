def read_file(filename):
  f = open(filename, 'r', encoding='utf-8-sig')
  words = f.read()
  f.close()
  return words

def histogram_dict(source_text):
  """return a histogram in dictionary/hash table form
  source_text: string
  """
  dict = {}
  for word in source_text:
    if word in dict.keys():
      dict[word] += 1
    else:
      dict[word] = 1
  return dict


def histogram_list(source_text):
  lst = []
  
  # # THIS WORKS, but I can't explain why...
  for word in source_text:
    for pair in lst:
      if word == pair[0]:
        pair[1] = pair[1] + 1
        break
    else: 
      lst.append([word, 1])

  # # python implementation: https://stackoverflow.com/questions/48774616/return-the-value-of-a-matching-item-in-a-python-list
  # for word in source_text:
  #   found_pair = next((pair for pair in lst if word in pair), None)
  #   if found_pair is not None:
  #     found_pair[1] += 1
  #   else: lst.append([word, 1])
  return lst


# NEEDS IMPROVEMENT - immutable data structure.
def histogram_tuple(source_text):
  tuple_list = []
  for word in source_text:
    found_pair = next((pair for pair in tuple_list if word in pair), None)
    if found_pair is not None:
      tuple_list.remove(found_pair)
      amount = found_pair[1]
      temp_list = list(found_pair)
      temp_list[1] = amount + 1
      found_pair = tuple(temp_list)
      tuple_list.append(found_pair)
    else: tuple_list.append((word, 1))
  return tuple_list


def unique_words(dict):
  # returns the total count of unique words in the histogram. For example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475.
  return f'{len(dict)} unique words'

def frequency(word, histogram):
  # returns the number of times that word appears in a text. For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.
  # for lists
  for pair in histogram:
    if pair[0] == word:
      return pair[1]

  # for dicts
  if word in histogram.keys():
    return histogram[word]


if __name__ == '__main__':
  file = ""
  corpus_list = read_file(file).replace(',', '').replace('.', '').replace('?', '').replace('"', '').replace('”', '').replace('’', '').replace('!', '').replace('/', '').replace(';', '').lower().split()

  histogram_dictionary = histogram_dict(corpus_list)
  print(histogram_dictionary)
  print(unique_words(histogram_dictionary))
  print(frequency('sherlock', histogram_dictionary))

  hist_list = histogram_list(corpus_list)
  print(hist_list)
  print(unique_words(hist_list))
  print(frequency('sherlock', hist_list))

  hist_tuple = histogram_tuple(corpus_list)
  print(hist_tuple)
  print(unique_words(hist_tuple))

