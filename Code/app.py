"""Main script, uses other modules to generate sentences."""
from flask import Flask, redirect, render_template, request, redirect
from tokens import tokenize
from markov_chain_second_order import markov_chain_generator, walk
import twitter
from histogram import read_file
file = './data/socrates-apology.txt'

app = Flask(__name__)
word_list = read_file(file)
tokens = tokenize(word_list)
markov_chain = markov_chain_generator(tokens)


from sample import sampler
from dictogram import Dictogram
from listogram import Listogram
from markov_chain import dict_of_histograms_generator, tweet_generator
word_list = read_file(file).replace(',', '').replace('.', '').replace('?', '').replace('"', '').replace('”', '').replace('’', '').replace('`', '').replace('!', '').replace('/', '').replace(';', '').replace(':', '').lower().split()

@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    corpus_list = read_file(file).replace(',', '').replace('.', '').replace('?', '').replace('"', '').replace('”', '').replace('’', '').replace('`', '').replace('!', '').replace('/', '').replace(';', '').replace(':', '').lower().split()
    # histogram = Dictogram(corpus_list)
    histogram = Listogram(word_list)
    return histogram


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = walk(markov_chain)
    return render_template('index.html', sentence=sentence)

@app.route("/tweet", methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')
    
if __name__ == "__main__":
    """To run the Flask server, execute `python3 app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)

