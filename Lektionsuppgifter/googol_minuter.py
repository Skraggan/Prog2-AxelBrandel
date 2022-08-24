import time

t_now = time.time()
t_now = int(t_now)

t = t_now + (10**100)*60
current = t % (60*60*24)
hours = current // (60*60)
minutes = (current - hours*3600)//60

print(f"The time in googol minutes is: {hours}:{minutes}")