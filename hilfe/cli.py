# hilfe/cli.py

import typer
import json
import subprocess
from termcolor import colored, cprint
import os

app = typer.Typer()

def load_explanations(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def get_explanation(topic: str):
    explanations = load_explanations("/root/nvim/stuff/hilfe/hilfe/data.json")
    if topic in explanations:
        return explanations[topic]
    elif topic not in explanations:
        try:
            subprocess.run(["man", topic], check=True, text=False, capture_output=False)
        except Exception:
            print("Here is a list of commands:\n")
            for char, i in enumerate(explanations):
                print(char, i)
            print()
            print(colored("and every command found in the manual page.", "red"))

@app.command()
def hilfe(topic: str):
    explanation = get_explanation(topic)
    typer.echo(explanation)

if __name__ == "__main__":
    app()
