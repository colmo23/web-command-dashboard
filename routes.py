#!/usr/bin/env python3

import os

from flask import Flask, render_template
app = Flask(__name__,  static_url_path='/static')

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Hex Edit')

def format_ajax(title, content):
    return '<fieldset><legend style="color:blue;font-weight:bold;">%s</legend><pre>%s</pre></fieldset>' % (title, content)

@app.route('/ajax/get-column1')
def ajax_column1():
    dir_list = os.popen("ls -l").read()
    return format_ajax("directory list", dir_list)

#   <legend style="color:blue;font-weight:bold;">General Information</legend>
@app.route('/ajax/get-column2')
def ajax_column2():
    top = os.popen("top -b -n 1").read()
    return format_ajax("top", top)

@app.route('/ajax/get-column3')
def ajax_column3():
    df = os.popen("df -h").read()
    return format_ajax("df -h", df)
@app.route('/ajax/get-column4')
def ajax_column4():
    uptime = os.popen("uptime").read()
    return format_ajax("uptime", uptime)
@app.route('/ajax/get-column5')
def ajax_column5():
    ns = os.popen("netstat -nap").read()
    return format_ajax("netstat -nap", ns)

if __name__ == '__main__':
    app.run(debug=True)
