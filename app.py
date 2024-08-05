from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'links.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS links
                 (id INTEGER PRIMARY KEY, link TEXT, description TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM links')
    links = c.fetchall()
    conn.close()
    return render_template('index.html', links=links)

@app.route('/add', methods=['POST'])
def add_link():
    password = request.form['password']
    if password == '12345':
        link = request.form['link']
        description = request.form['description']
        if link and description:
            conn = sqlite3.connect(DATABASE)
            c = conn.cursor()
            c.execute("INSERT INTO links (link, description) VALUES (?, ?)", (link, description))
            conn.commit()
            conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
