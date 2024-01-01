from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

def generate_password(username):
    randomized_username = ''.join(random.choice([c.upper(), c.lower()]) for c in username)
    symbols = '!@#$%&*_-+=<>?'
    numbers = '0123456789'
    position = random.choice(['prefix', 'suffix', 'center'])

    if position == 'prefix':
        password = randomized_username + random.choice(symbols) + random.choice(numbers) + random.choice(symbols) + random.choice(numbers)
    elif position == 'suffix':
        password = random.choice(symbols) + random.choice(numbers) + random.choice(symbols) + random.choice(numbers) + randomized_username
    elif position == 'center':
        prefix_length = random.randint(1, 6)
        suffix_length = 16 - prefix_length - len(randomized_username)
        password = (
            random.choice(symbols) * prefix_length +
            randomized_username +
            random.choice(symbols) * suffix_length
        )
    else:
        raise ValueError("Invalid position")

    while len(password) < 16:
        password += random.choice(symbols + numbers + randomized_username)

    return password[:16]

@app.route('/')
def generate_password_page():
    return render_template('generate_password.html')

@app.route('/generate_password', methods=['POST'])
def generate_password_route():
    username = request.form['username']
    generated_password = generate_password(username)
    return render_template('password_result.html', username=username, password=generated_password)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
