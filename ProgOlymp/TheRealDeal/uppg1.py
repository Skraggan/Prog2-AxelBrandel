tor_time = int(input("Tors tid ? "))
mor_time = int(input("Mors tid ? "))
carrots = 40
tor_carrots = 0
mor_carrots = 0

t = 0
while carrots > 0:
    t += 1
    if carrots == 1 and t % tor_time == 0 and t % mor_time == 0:
        break
    if t % tor_time == 0:
        carrots -= 1
        if carrots <= 0: break
        tor_carrots += 1
    if t % mor_time == 0:
        carrots -= 1
        mor_carrots += 1

print()
print(f"Svar: Tor {tor_carrots}, Mor {mor_carrots}")