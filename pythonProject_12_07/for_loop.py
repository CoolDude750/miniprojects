n = 6
for i in range(6):
    if i <= 3:
        n = i
    else:
        n = 6 - i
    print(("ineuron "*n).center(50,' '))