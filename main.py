from flask import Flask, request, jsonify, render_template, redirect, flash, url_for
from flask_restful import Api
import random
import time
import json
import sys

app = Flask(__name__)
api = Api(app)

# time_start = 0
# wpm = 0
# word = ''
w=750
h=500
reset=True
active = False
input_text=''
word = ''
time_start = 0
total_time = 0
accuracy = '0%'
results = 'Time:0 Accuracy:0 % Wpm:0 '
wpm = 0
end = False
HEAD_C = (255,213,102)
TEXT_C = (240,240,240)
RESULT_C = (255,70,70)
global start_time
global final_result
start_time = time.time()
# @app.route('/', methods = ['POST','GET'])
# def typing():
#     return render_template('index.html')

@app.route('/show_data/', methods = ['POST','GET'])
def get_sentence():

    f = open('sentences.txt').read()
    sentences = f.split('\n')
    sentence = random.choice(sentences)
    print("Sentence: ",sentence)
    return sentence

@app.route("/",methods = ['POST', 'GET'])
def add_data(end = False):

    if request.method == "POST":
        result = request.form["input_text"]

        print("name:",result)
        global results

        #Calculate time

        time_start = start_time
        print(time)

        total_time = time.time() - time_start
        print("time:",total_time)
        print("time_start:", time_start)


        word = get_sentence()
        print("words:",word)
        print("result:", result)
        #Calculate accuracy
        count = 0
        for i,c in enumerate(word):
            try:
                if result[i] == c:
                    count += 1
            except:
                pass
        print("count:",count)
        accuracy = count/len(word)*100
        print("accuracy:",accuracy)
            
        #Calculate words per minute
        wpm = len(result)*60/(5*total_time)
        print("wpm:",wpm)

        print(total_time)
            
        global results

        results = 'Time:'+str(round(total_time)) +" secs   Accuracy:"+ str(round(accuracy)) + "%" + '   Wpm: ' + str(round(wpm))

        print(results)

        # return redirect(url_for('final_result',final_result = results))
        return results
        # return (results)
    # else:
    #     # return redirect(url_for('hello_guest', guest=name))
    #     return redirect(url_for('final_result', final_result = results))

    return render_template("index.html", final_result = results)


@app.route('/result')
def final_result():
    a = add_data()
    print("(&**^*:",a)
    return jsonify(a)



    
    
    


    
if __name__ == '__main__':
    app.run(port='5555', debug=True)