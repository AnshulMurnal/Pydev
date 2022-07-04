import time
import random


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
    def times(self,):
        op3 = input().lower()
        set2 = ["what is the time", "tell me the time"]
        if op3 in set2:
            print(time.ctime())
        else:
            print("cannot understand")

    temp = random.randint(0, 50)
    def temperature(self,):
        if self.temp > 40:
            print("I am overheated!")
        else:
            self.temp = random.randint(0, 50)
    battery = random.randint(0, 100)
    def power(self,):
        if self.battery < 20:
            print("Low battery power!Please charge")
        else:
            self.battery = random.randint(0, 100)
    speed = random.randint(0, 40)
    def acceleration(self,):
        if self.speed > 20:
            print("My speed has increased : "+str(self.speed))
        else:
            self.speed = random.randint(0, 40)
bot = Robot("dora", "black")
bot.acceleration()
bot.temperature()
bot.clean()
bot.power()
bot.news()
bot.times()