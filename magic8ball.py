from random import choice
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

sense.show_message("Ask a Question")
sleep(5)

replies = ['Signs point to yes',
           'without a doubt',
           'You may rely on it',
           'Do not count on it',
           'Looking good',
           'Cannot Predict now',
           'It is decidedly so',
           'Outlook not so good'
           ]

while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 2 or y > 2 or z > 2 :
        sense.show_message(choice(replies))
    else:
        sense.clear()

sense.show_message(choice(replies))
