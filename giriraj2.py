from  easygui import *
import sys

while 1:
	msgbox("welcome to ebazzar")
	msg="what you  would like to buy?"
	title="ebazzar"
	choices=["electronics","groceries","fashion","appliances","home"]
	choice=choicebox(msg,title,choices)
	msgbox("you choose:"+str(choice),"survey result")
	if choice=="electronics":
		choices1=["TV","mobile","fridge"]
		choice1=choicebox(msg,title,choices1) 
                msgbox("you choose"+str(choice1),"result")
		if choice1=="TV":
			choices2=["sony","lg","samsung"]
			choice2=choicebox(msg,title,choices2)
			msgbox("you choose"+str(choice2),"result")
		elif choice1=="mobile":
			choices3=["apple","samsung","nokia"]
			choice3=choicebox(msg,title,choices3)
			msgbox("You choose"+str(choice3),"result")
		elif choice1=="fridge":
			choices3=["samsung","lg"]
			choice3=choicebox(msg,title,choices3)
			msgbox("you choose"+str(choice3),"result")

