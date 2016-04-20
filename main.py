import os

from flask import Flask, render_template

app = Flask(__name__)
all_words_dict = {}

import poem

# Views
@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    global all_words_dict
    all_words_dict = {}
    return render_template('index.html')

def getInput():
	return text = poem.text('')
	
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)