from sys import exit
from random import randint

def death():
  quips = ["You died. You kinda suck at this.",
           "Your mom would be proud. If she were smarter.",
           "Such a luser.",
           "I have a small puppy that's better at this."]
  print quips[randint(0, len(quips)-1)]
  exit(1)

def princess_lives_here():
  print "You see a beautiful Princess with a shiny crown."
  print "She offers you some cake."