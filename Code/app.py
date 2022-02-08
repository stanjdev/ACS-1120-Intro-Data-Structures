"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from histogram import histogram_dict, read_file
from sample import sampler
from dictogram import Dictogram
from listogram import Listogram
file = './data/socrates-apology.txt'

app = Flask(__name__)
word_list = read_file(file).replace(',', '').replace('.', '').replace('?', '').replace('"', '').replace('”', '').replace('’', '').replace('`', '').replace('!', '').replace('/', '').replace(';', '').replace(':', '').lower().split()

@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    corpus_list = read_file(file).replace(',', '').replace('.', '').replace('?', '').replace('"', '').replace('”', '').replace('’', '').replace('`', '').replace('!', '').replace('/', '').replace(';', '').replace(':', '').lower().split()
    # histogram = histogram_dict(corpus_list)
    # histogram = Dictogram(corpus_list)
    histogram = Listogram(word_list)
    return histogram


@app.route("/")
def home():
    histogram = before_first_request()
    chosen_word = histogram.sample()
    # chosen_word = sampler(histogram)
    """Route that returns a web page containing the generated text."""
    return render_template('index.html', chosen_word=chosen_word, histogram=histogram)


if __name__ == "__main__":
    """To run the Flask server, execute `python3 app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)

