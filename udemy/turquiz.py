import turtle

turtle.bgcolor=('white')

print("Willkomen bei der Artikel Quiz")
print("Fur alle Worter die du siehst, gib den richtigen Artikel\n")
questions = {
"Flasche":"die",
    "Wasser":"das",
    "Koffer":"der",
    "Auto":"das",
    "Heft":"das"
}
count = 0
for a in questions:
    print(a)
    ans = input("Rate mal - ")
    if ans == questions[a]:
        print("Good Job")
        count=count+1
    else:
        print("Oopss")
print("Du hast ",count,"Punkte")