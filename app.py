from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

class Note:
    def __init__(self, note, timestamp):
        self.note = note
        self.timestamp = timestamp

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note_text = request.form.get("note")
        if note_text:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            notes.append(Note(note_text, timestamp))
            return redirect(url_for('index'))  # Redirect to GET request after POST
    enumerated_notes = enumerate(notes)  # Enumerate notes here
    return render_template("home.html", enumerated_notes=enumerated_notes)

@app.route('/edit/<int:index>', methods=["GET", "POST"])
def edit(index):
    if request.method == "POST":
        new_note = request.form.get("note")
        if new_note:
            notes[index].note = new_note
            notes[index].timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return redirect(url_for('index'))
    return render_template("edit.html", note=notes[index])

@app.route('/update/<int:index>', methods=["POST"])
def update(index):
    updated_note = request.form.get("updated_note")
    if updated_note:
        notes[index].note = updated_note
        notes[index].timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=["POST"])
def delete(index):
    del notes[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
