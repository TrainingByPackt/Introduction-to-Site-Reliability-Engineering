#!/usr/bin/env python3
from random import seed, choice
from flask import Flask
import logging

logger = logging.getLogger(__name__)
seed()
application = Flask(__name__)

excuseslist = ['my car broke down', 'I was at a funeral', 'I had a dentist appointment', 'I had to take the kids to school', 'My wife\'s water broke', 'there is terrible traffic today', 'i was dealing with a production outage from home', 'the train was slow' ]

@application.route('/excuse')
def deliver_exuse():
    return "Sorry, I'm running a bit late today because {}. I will be in shortly!".format(choice(excuseslist))


@application.route('/ping')
def health():
    return "OK"

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80, debug=True)
