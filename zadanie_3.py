
x, y = 50, 50

if x > 100 or x < 0 or y > 100 or y < 0:
    print("Jesteś poza planszą")
elif x > 90 and y > 90:
    print("Jesteś w GPR")
elif x > 90 and y < 10:
    print("Jesteś w DPR")
elif x < 10 and y > 90:
    print("Jesteś w LGR")
elif x < 10 and y < 10:
    print("Jesteś w LDR")
elif x > 90:
    print("Jeteś na PK")
elif x < 10:
    print("Jeteś na LK")
elif y > 90:
    print("Jeteś na GK")
elif y < 10:
    print("Jeteś na DK")
else:
    print("Jesteś w Centrum")