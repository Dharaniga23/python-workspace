#for counter in reversed(range(1,10)):
 #   if counter == 3:
  #      continue
   # else:
    #    print(counter)

#print("HAPPY NEW YEAR")
 
import time

seconds = int(input("Enter the time in seconds:"))

for x in range(seconds,0,-1):
    seconds = x % 60
    minutes = int(x/60)%60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!!")
 
