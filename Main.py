from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find-carbon-date', methods=['POST'])
def result():
    
    c_url  = request.form.get('url')
    
    # You can validate the car brands. If someone is telling the wrong brand name, reply them with the wrong answer
    
    c_date = get_carbon_date(c_url)
    
    user = {
        'c_url' : c_url,
        'created_date': c_date,         
    }
    
    #return content
    return render_template('result.html', user=user)

def get_carbon_date(url):
    return 'Jan 29, 2019'


if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host= host, port = port, use_reloader = False)
    
    
'''
Sources:
    http://cd.cs.odu.edu/cd/https://www.laurencegellert.com/2012/08/what-is-a-full-stack-developer/
'''