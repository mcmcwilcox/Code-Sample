print("Simply enter the number of legs and segments you have observed on your creature!")
legs = 1400
segments = 3
if legs < 6:
  print("This doesn't have enough legs to be an arthropod...")
if legs == 6 and segments == 3:
  print("You probably have an insect!")
if legs > 6 and legs <8:
  print("You may have an injured spider..")
if legs == 8 and segments == 2:
  print("You are probably looking at a spider! Don't panic, very few spiders can even bite a human!")
if legs == 8 and segments == 1:
  print("This can only be a mite!")
if legs > 8 and legs < 30:
  print("Hmm, I'm not sure what has that many legs.. try counting them again!")
if legs >= 30 and legs <=354:
  print("This could be a centipede OR a milipede!")
if legs > 354 and legs <= 1306:
  print("Only a milipede can have that many legs!")
if legs > 1306:
  print("Back slowly away, and report your location to wildlife services so they can investigate...")
