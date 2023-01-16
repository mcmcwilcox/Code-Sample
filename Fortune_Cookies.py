import random
name = "MC"
birth_month = "June"
fortune = ""
random_number = random.randint(1,10)
print(random_number)
if random_number == 1:
  fortune = " Looking too much into the past will not prepare you for the future."
elif random_number == 2:
  fortune = " Today will be exceedingly lucky for you."
elif random_number == 3:
  fortune = " Watch out for the number 4 this week..."
elif random_number == 4:
  fortune = " Hope for the best, but be prepared for the worst."
elif random_number == 5:
  fortune = " Acquaintance softens prejudice."
elif random_number == 6:
    fortune = " Advice prompted by selfishness should not be heeded."
elif random_number == 7:
    fortune = " Fine feathers do not a fine bird make."
elif random_number == 8:
    fortune = " One may judge a man by the company he keeps."
elif random_number == 9:
    fortune = " If you keep your wits about you, a prosperous year lies ahead."
elif random_number == 10:
  fortune = " Do not bite the hand that feeds."
else:
  fortune = "You must look deeply inside yourself." 
if name == "" or birth_month == "":
    print("I must know where the stars were at the time of your birth to proceed...")
else:
  print(name + " wishes for a glimse at the future: " + fortune)
