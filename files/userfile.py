filename = input("create file eith yoyur name")
f = open(f"files\\{filename}.txt",'x')

name = input("enter your name :>")
age = input ("enter tour age :>")
city = input ("enter your city :>")

w = open (f'files\\{filename}.txt','w')
w.write(f"\n name :{name} \n age :{age} \n city : {city}m")