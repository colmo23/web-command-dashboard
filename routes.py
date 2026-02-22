#!/usr/bin/env python3

import html
import subprocess


from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

# two decorators, same function


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Web commmand dashboard')


def format_ajax(title, content, err=None):
    if err:
        return '<fieldset><legend style="color:red;font-weight:bold;">%s</legend><pre>%s</pre></fieldset>' % (
            title, html.escape(err))
    return '<fieldset><legend style="color:blue;font-weight:bold;">%s</legend><pre>%s</pre></fieldset>' % (
        title, html.escape(content))


def run_command(command):
    p = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    stdout = stdout.decode("utf-8", errors="ignore")
    stderr = stderr.decode("utf-8", errors="ignore")
    return stdout, stderr


@app.route('/ajax/get-column1')
def ajax_column1():
    dir_list, stderr = run_command("ls -l")
    return format_ajax("directory list", dir_list, stderr)


@app.route('/ajax/get-column2')
def ajax_column2():
    top, err = run_command("top -b -n 1")
    return format_ajax("top", top, err)


@app.route('/ajax/get-column3')
def ajax_column3():
    df, err = run_command("df -h")
    return format_ajax("df -h", df, err)


@app.route('/ajax/get-column4')
def ajax_column4():
    uptime, err = run_command("uptime")
    return format_ajax("uptime", uptime, err)


@app.route('/ajax/get-column5')
def ajax_column5():
    ns, err = run_command("netstat -nap")
    return format_ajax("netstat -nap", ns, err)

@app.route('/ajax/get-column6')
def ajax_column6():
    top, err = run_command("top -b -n1 -c -w 500")
    return format_ajax("top - full process name", top, err)

@app.route('/ajax/get-column7')
def ajax_column7():
    top, err = run_command(" top -b -n 1 -o RES -c -w 500")
    return format_ajax("top - sorted by memory usage", top, err)



if __name__ == '__main__':
    app.run(debug=False)
