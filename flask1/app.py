from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = 'supersecretkey'
users = {}
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists! Try a different one.', 'error')
            return redirect(url_for('register'))
        users[username] = password
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            flash(f'Welcome, {username}!', 'success')
            return f"Hello, {username}! You are now logged in."
        else:
            flash('Invalid username or password. Please try again.', 'error')
            return redirect(url_for('login'))
        return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)
