import random
import time
class Robot:


    def __init__(self, name, colour):
        self.colour = colour
        self.name = name
    
    def start(self,):
        print("Hello!Please wait the boot is loading it may take few seconds.....")
    def shutdown(self,):
        print("I am off now so good bye and have great day...")
    def clean(self,):
        option = input("do you want me to clean the place?: ")
        if option == "yes":
            print("I am cleaning ")
        else:
            print("Thats fine")

    def news(self,):
        op2 = str(input()).lower()
        set = ["tell me the news", "what is the news"]
        if op2 in set:
            print("Today's news is  xyz...")
        else:
            print("cannot understand")
    def time(self,):
        op3 = input().lower()
        set2 = ["what is the time", "tell me the time"]
        if op3 in set2:
            print("The time is: "+time.ctime(time.time()))
        else:
            print("cannot understand")

    temp = random.randint(0, 50)
    def temperature(self,):
        if self.temp > 40:
            print("High temperature the person is like to have drank too much alcohol")
        else:
            print("The temperature seems to be normal")
    alcohol = random.randint(0, 20)
    def alcoholity(self,):
        if self.alcohol > 10:
            print("High rate")
        else:
            print("Normal rate")
    speed = random.randint(0, 40)
    def acceleration(self,):
        if self.speed > 30:
            print("He is fast")
        else:
            print("He is slow")
    person = temp + speed + alcohol
    def Person(self,):
        if self.person > 70:
            print("Ladies and gentlemen we have found the GIGICHAD!")
        else:
            print("A normal guy")
bot = Robot("dora", "black")
bot.acceleration()
bot.temperature()
bot.alcoholity()
bot.Person()
bot.clean()
bot.news()
bot.time()