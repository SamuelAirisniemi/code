age = input("Ange din ålder: ")
weight = input("Ange din vikt i kg: ")

if int(age) >= 3 and int(age) <= 7 and int(weight) >= 15 and int(weight) <= 25:
    print("Du ska ta 1/2 tablett.")

elif int(age) > 7 and int(weight) < 26:
        print("Du ska ta 1/2 tablett.")

elif int(age) >= 7 and int(age) <= 12 and int(weight) > 25 and int(weight) <= 40:
    print("Du ska ta 1/2-1 tablett.")

elif int(age) <= 12 and int(weight) > 40:
        print("Du ska ta 1-2 tabletter.")
        
elif int(age) > 12 and int(weight) > 40:
    print("Du ska ta 1-2 tabletter.")