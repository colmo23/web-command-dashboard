#!/usr/bin/env python3

import argparse
import json
import subprocess

from flask import Flask, jsonify, render_template
app = Flask(__name__, static_url_path='/static')

commands = []


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Web command dashboard', commands=commands)


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


@app.route('/ajax/get-column/<int:col_id>')
def ajax_column(col_id):
    if col_id < 0 or col_id >= len(commands):
        return 'Not found', 404
    cmd = commands[col_id]
    output, err = run_command(cmd['command'])
    if err:
        return jsonify({'text': err, 'is_error': True})
    return jsonify({'text': output, 'is_error': False})


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Web command dashboard')
    parser.add_argument('config', help='Path to JSON commands config file')
    args = parser.parse_args()

    with open(args.config) as f:
        commands = json.load(f)

    app.run(debug=False)
