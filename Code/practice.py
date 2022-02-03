
from unicodedata import name


class MyClass(dict):
    def __init__(self, word_list = None):
        super(MyClass, self).__init__()

        if word_list is not None:
            for word in word_list:
                print(self)



test = MyClass(['var', 'rsa', 'esf', 'fgsdfg', 'agaga', ])

if __name__ == '__main__':
    print(test)




