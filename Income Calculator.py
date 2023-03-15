Thomas Hunt
Created 16/03/2023



name = input("What is your name? ")
print(f"Hello, {name}")
age = int(input("What is your age?: "))
if age <= 15:
    print(f"{age} is pretty young.")
else :
    print(f"{age} getting older")

wage = float(input("What is your hourly wage: $"))
hours = int(input("How many hours a day do you work: "))
days = int(input("How many days a week: "))
expens = float(input("What are your weekly expenses: $"))
hrwk = hours * days
gross = hrwk * wage
if ((gross >= 0) and ( gross <= 14000)):
    tax = 10.5 
elif ((gross > 14000) and ( gross <= 48000)):
    tax = 17.5
elif ((gross > 48000) and ( gross <= 70000)):
    tax = 30
else :
    tax = 33
finaltax = tax * gross / 100
aft = gross - tax - expens
year = hrwk * 52
total = year * wage
t2 = aft * 52
print(f"You work {hrwk} hours every week!")
print(f"This means you make gross ${gross} a week!")
print(f"So {name} at the age of {age} you work {hrwk} every week and make gross ${gross}, Thats really good")
print(f"You lose ${finaltax:0.2f} to tax each week")
print(f"You make {aft:0.2f} after your weekly expenses of ${expens}")
print(f"Your yearly income is ${total}")
print(f"If your income doesn't change and neither does your exspenses you will have ${t2:.2f} in the bank every year")
