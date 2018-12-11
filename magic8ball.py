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

sense.show_message(choice(replies))
