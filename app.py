from flask import Flask, redirect, render_template, request
import re
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

app = Flask(__name__)


@app.route("/")
def index():
    return redirect('/frequency')


@app.route('/frequency')
def frequency():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    wordlist = []
    URL = request.form['link']
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    # If this line causes an error, run 'pip install html5lib' or install html5lib
    a_text = soup.find_all('p')
    a_text=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
    for i in a_text:
        wordlist.append(i.split())
    
    wordlist = [[ele for ele in item if str(ele) != "" or str(ele) != "{" or str(ele) != "}"] for item in wordlist]             
    # print(wordlist)
    # wordlist = clean_wordlist(wordlist)
    # print()
    # print(wordlist)
    # print()
    wordlist = create_dictionary(wordlist)
    # print(wordlist)
    # print()
    # wordlist.append(a_text)
    return render_template('result.html', result=wordlist)
    # result = clean_wordlist(wordlist)
    # return render_template('result.html', result=result)

def clean_wordlist(wordlist): 
      
    clean_list =[] 
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|;:"<>?/., '
          
        for i in range (0, len(symbols)):
            for string in word:
                string = str(string).replace(symbols[i], '') 

              
        if len(word) > 0: 
            clean_list.append(word) 
    top = create_dictionary(clean_list)
    return top

# Creates a dictionary conatining each word's  
# count and top_20 ocuuring words 
def create_dictionary(clean_list): 
    word_count = {} 
    for item in clean_list:
        for word in item:
            if word in word_count: 
                word_count[word] += 1
            else: 
                word_count[word] = 1
    c = Counter(word_count) 
      
    # returns the most occurring elements 
    top = c.most_common(10) 
    return top

if __name__ == "__main__":
    app.run()
