# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup and Running

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python routes.py commands.example.json
```

The app runs at `http://localhost:5000` in Flask debug mode.

## Architecture

This is a minimal Flask app that serves as a Linux system monitoring dashboard. There are no tests and no build steps.

**Data flow:**
1. `routes.py` serves `index.html` at `/` and exposes `/ajax/get-columnN` endpoints (currently 7 columns)
2. Each column endpoint runs a shell command via `subprocess.Popen(shell=True)` and returns an HTML `<fieldset>` snippet via `format_ajax()`
3. `templates/index.html` polls all column endpoints every 5 seconds using jQuery `$.get()` and injects the returned HTML into `<div id="columnN">` elements
4. Bootstrap 5 grid (`div.col`) arranges the columns horizontally

**Adding or changing a command panel** requires only editing the JSON config file — no Python or HTML changes needed. Each entry has three fields:
```json
{"title": "display name", "command": "shell command", "interval": 10}
```
`interval` is in seconds. `commands.example.json` has the default set of 7 panels.
