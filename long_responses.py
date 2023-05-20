import random

r_breath = "I can't breathe because I'm a bot duh!"
r_eat= "How can I eat dummy"

def unknown():
    response = ['Could you please rephrase that? ',
                 'I\'m sorry I didn\'t quite get that', 
                  '...',
                  'Wait what?'][random.randrange(4)]
    return response