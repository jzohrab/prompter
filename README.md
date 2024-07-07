# Prompter

An _extremely basic_ program for improv practice.  Given a data file of prompts to say at specified intervals, it speaks each prompt and then waits to say the next prompt.

Useful for practicing jamming over a backing track when you want to be reminded of licks and ideas to try out.

**This currently only works on Mac, as it uses the terminal `say` command.**

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Config

Copy config.yaml.example to config.yaml, edit with your licks.

## Usage

```
python main.py

# Enter the mins you want it to run.
```