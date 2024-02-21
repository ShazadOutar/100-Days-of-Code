from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def home_page():
    return ('<h1 style="text-align: center">'
            'Guess a Number Between 0 and 9'
            '</h1>'
            '<center><img src='
            'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTZyZGF3N2s5a2w2emJheHNwOXNxbThseDN3aHR2ZG0xMDdyYjI5OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/V4EWHxijk2HGaNJTX9/giphy.gif>'
            '</center>'
            )


# generate a random number from 0 to 9
random_number = random.randint(0, 9)


# the route to handle the guessed number
@app.route("/<int:guess>")
def check_guess(guess):
    print(f"Random Number is {random_number}")
    if guess < random_number:
        return (f'<h1>'
                f'Your guess of {guess} was too low'
                f'</h1>'
                f'<img src='
                f'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2xqbHByd2Q3YXE0bTN3cWtuNTRnYWN5c2xrdXJvYTNpMTlhN3JwdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RiWcEgPzygCrFC5gMF/giphy.gif>'
                )
    elif guess > random_number:
        return (f'<h1>'
                f'Your guess of {guess} was too high'
                f'</h1>'
                f'<img src='
                f'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjRzbTV2aDNyeW13Y3BhNmc3cWFrZzQ3bjQ3N3l4em91dGM4Zmw0dCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/fRJxL9D36l6q7hOgjI/giphy.webp>')
    else:
        return (f'<h1>'
                f'YOU GOT IT! The number was {guess}'
                f'</h1>'
                f'<img src='
                f'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3J0ZWlsZGlsd2xxeXhnd2cwa283NzdoNWdmanB4Zzcyem1uc2hzdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zlVf2eSgXIFFuTnEhz/giphy.gif>')
    # return (f'Your guess was {guess}')


if __name__ == "__main__":
    # generate a random number from 0 to 9
    # random_number = random.randint(0, 9)
    # print(random_number)
    app.run(debug=True)
