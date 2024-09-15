import time

hour=int(time.strftime('%H'))
minute=int(time.strftime('%M'))
second=int(time.strftime('%S'))

if hour>=12:
  print("good after noon")

elif hour<=12:
    print("good morning")

else:
     print("nothing")