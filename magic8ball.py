from random import choice
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

I = (255, 255, 255) # White
X = (0, 0, 0) # Black
O = (128, 0, 128) # Purple

ball_pixels = [
    O, O, O, O, O, O, O, O,
    O, O, X, X, X, X, O, O,
    O, X, X, I, I, X, X, O,
    O, X, I, I, I, I, X, O,
    O, X, I, I, I, I, X, O,
    O, X, X, I, I, X, X, O,
    O, O, X, X, X, X, O, O,
    O, O, O, O, O, O, O, O
]

sense.set_pixels(ball_pixels)
sleep(3)

sense.show_message("Ask a Question", text_colour=(255, 255, 255), back_colour=(128, 0, 128), scroll_speed=0.06)
sleep(1)

replies = ['Signs point to yes',
           'without a doubt',
           'You may rely on it',
           'Do not count on it',
           'Looking good',
           'Cannot Predict now',
           'It is decidedly so',
           'Outlook not so good',
           'Your trashcan has a better chance',
           'Maybe...',
           'Probably.',
           'Yep',
           'Nope',
           'I dont know',
           'I suppose',
           'I guess',
           'Whatever you say'
           ]

while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 2 or y > 2 or z > 2 :
        sense.show_message(choice(replies), text_colour=(255, 255, 255), back_colour=(128, 0, 128), scroll_speed=0.06)
    else:
        sense.clear()

sense.show_message(choice(replies), text_colour=(255, 255, 255), back_colour=(128, 0, 128), scroll_speed=0.06)

