# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

import smtplib
import random

class Assistant():
    
    def __init__(self, name):
        
        self.name = name
        self.initialize()
                
    def run(self):
        
        while True:
            
            menu_option = "1. Change My Name\n2. Create Schedule\n3. View Schedule\n4. Send Email\n5. Random Jokes\n0. Exit"
                
            print("\n*********************************************")
            print("Hello Python Folks, my name is " + self.name + ", how can I help you?")
            print(menu_option)
            print("*********************************************")
            
            menu = input("Which one do you want? ")

            if menu == "1":
                name = input("Input new name: ")
                self.change_name(name)
            elif menu == "2":
                self.create_schedule()
            elif menu == "3":
                self.view_schedule()
            elif menu == "4":
                self.send_email()
            elif menu == "5":
                self.random_jokes()
            elif menu == "0":
                print("Good bye!")
                break
            else:
                print("Invalid menu, please try again!")
    
    def initialize(self):        
        print("New Virtual Assistant has been created successfully.")
        input("- Press ENTER -")

    def change_name(self, name):
        self.name = name
        print("\nMy name has been changed.")
        input("- Press ENTER -")
        
    def create_schedule(self):
        file = open("./schedule.txt", "a")
        schedule = input("\nPlease input your agenda: (format: dd/mm/yyyy - agenda_name)\n")
        file.write(schedule + "\n")
        file.close()
        print("New schedule has been created.")
        input("- Press ENTER -")
    
    def view_schedule(self):
        print("\nHere is list of your schedule:")
        file = open("schedule.txt", "r")
        print(file.read())
        file.close()

        input("- Press ENTER -")

    def random_jokes(self):
        jokes = [
        "Debugging is like being the detective in a crime movie where you're also the murderer at the same time.", 
        "Algorithm: A word used by programmers when they don't want to explain how their code works.", 
        "To whoever stole my copy of Microsoft Office, I will find you. You have my Word!",
        "I visited my friend at his new house. He told me to make myself at home. So I threw him out. I hate having visitors.",
        "A perfectionist walked into a bar... apparently, the bar was not set high enough."]
        
        while True:
            
            print(random.choice(jokes))
            is_again = input("Again [Yes/No]? ")

            if is_again.lower() == "no" or is_again.lower() == "tidak" or is_again.lower() == "0": break

    def send_email(self):
        
        sender = '' # isi email pengirim
        password = '' # isi password dari email pengirim
        receiver = []

        file = open("./receiver_list.txt", "r")
        for x in file:
            receiver.append(x)

        subject = 'Greetings'
        body = 'Hello, I hope you have a great day!'

        message = "Subject: %s\n\n%s\n\nSent from %s." % (subject, body, self.name)

        try:
            #Create your SMTP session 
            smtp = smtplib.SMTP('smtp.gmail.com', 587) 

            #Use TLS to add security 
            smtp.starttls() 

            #User Authentication 
            smtp.login(sender, password)

            #Sending the Email
            smtp.sendmail(sender, receiver, message) 

            #Terminating the session 
            smtp.quit() 
            print ("Email sent successfully!") 
        
        except Exception as e:
            print("Oops! I found", e.__class__, "occurred.")
            print("Error message:", str(e))

            input("- Press ENTER -")
