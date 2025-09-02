import time
# ASi Codes:
RESET = "\x1b[0m"
GREEN = "\033[32m"
BLUE_WHITE = "\x1b[44;97m"

print(BLUE_WHITE,"Countdown Program!",RESET)
print("="*40)

for cdwon in  range(30,0,-1): # loops through the sequence of 30-0
  print(f"{GREEN}Counting down: {cdwon}{RESET}") # outputs countdown 
  time.sleep(0.8) # pausing for 0.8 mms for every number till 1
