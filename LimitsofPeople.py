class People:
    def __init__(self, name, age='0', height = ''):
        self.name = name
        self.age = int(age)
        self.height = height
        
    def calc_feetinch(self, height):
        i = height.split("'")
        self.feet = int(i[0])
        self.inches = int(i[1][0:-1])

        if self.inches > 12:
            self.feet +=  self.inches // 12
            self.inches = self.inches % 12
        
        self.height = (f"{self.feet}\'{self.inches}\"")
        

    def profileheightstack(personx, persony):                                             #always enter taller person second as persony
    
        xFeet = personx.feet
        yFeet = persony.feet
        
        footdiff = persony.feet - personx.feet
        inchediff = persony.inches - personx.inches
        
        print(f"\n____---------------------------------------------------____\n")
        print(f"Worlds Tallest:\n")
        print(f"{persony.name}(1918 - 1940) was considered the tallest person on earth by the Guinness World Records.\n He was born in Illinois, U.S. and traveled with the circus for sometime. Let compare the data.\n   ")

        print(f"Height Legend: \t\t\t\t\t\tFeet: | \n\n")

        print(f"{persony.name}: {persony.height:}{"":^10}{personx.name}: {personx.height}\n")
        print(f"{"oo":^20}",end="")
        print(f"{"oo":^40}")
        print(f"{"oooo":^20}",end="")
        print(f"{"oooo":^40}")
        print(f"{"oo":^20}",end="")
        print(f"{"oo":^40}")


        for x in range(yFeet):
            if x == 1:
                print(f"{"-----":^20}",end="")
                print(f"{"-----":^40}")
                continue
        
            if x < xFeet:
                print(f"{"|":^20}",end="")
                print(f"{"|":^40}")
            elif x == xFeet:
                print(f"{"|":^20}",end="")
                print(f"{"/ \\":^40}")
            else:
                print(f"{"|":^20}")

        print(f"{"/ \\":^20}\n\n")
        print(f"{persony.name} wouldve been taller than you by {footdiff} feet and {inchediff} inches. Feeling short now? \n")
        print(f"----___________________________________________________----")


    

    def profileshorteststack(personx, persony):                                                  #always enter taller person second as persony
    
        xFeet = personx.feet
        yFeet = persony.feet
        
        footdiff = persony.feet - personx.feet
        inchediff = persony.inches - personx.inches
        
        print(f"\n____---------------------------------------------------____\n")
        print(f"Worlds Shortest:\n")
        print(f"{personx.name} (1993 - ) is considered the shortest person on earth by the Guinness World Records.\n She was born in India and has been featured in popular TV shows. Lets compare the data.\n")
        print(f"Height Legend: \t\t\t\t\t\tFeet: | \n\n")


        print(f"{persony.name}: {persony.height:}{"":^10}{personx.name}: {personx.height}\n")
        print(f"{"oo":^20}",end="")
        print(f"{"oo":^40}")
        print(f"{"oooo":^20}",end="")
        print(f"{"oooo":^40}")
        print(f"{"oo":^20}",end="")
        print(f"{"oo":^40}")


        for x in range(yFeet):
            if x == 1:
                print(f"{"-----":^20}",end="")
                print(f"{"-----":^40}")
                continue
        
            if x < xFeet:
                print(f"{"|":^20}",end="")
                print(f"{"|":^40}")
            elif x == xFeet:
                print(f"{"|":^20}",end="")
                print(f"{"/ \\":^40}")
            else:
                print(f"{"|":^20}")

        print(f"{"/ \\":^20}\n\n")
        print(f"{personx.name} is shorter than you by {footdiff} feet and {inchediff} inches. You would stand tall beside her.\n")
        print(f"----___________________________________________________----")




    def oldeststack(personx, persony):                                                    #always enter older person first(as personx)
        yeardiff = personx.age - persony.age


        decadesx = personx.age//10
        singlex = personx.age % 10
         
        decadesy = persony.age//10
        singley = persony.age % 10
        



        print(f"\n____---------------------------------------------------____\n")
        print(f"World Oldest Person:\n {personx.name} (1875 - 1997) was considered the oldest recorded living person.\n She was born in France and lived up to the age of {personx.age}. Lets compare the data.\n")
        print(f"Year Legend: \t\t\t\t\t Dacade: -  Single Year: .\n\n")

        print(f"{personx.name} ({personx.age} y/o): ",end=(""))
        for x in range(decadesx):
            print("-",end=(""))
        for x in range(singlex):
            print(".",end=(""))
        print("\n")


        print(f"{persony.name} ({persony.age} y/o): ",end=(""))
        for x in range(decadesy):
            print("-",end=(""))
        for x in range(singley):
            print(".",end=(""))
        print("\n\n")
        print(f"{personx.name} was {yeardiff} years older than you. You have a long way to go till you even come close to beating her.")
        print(f"----___________________________________________________----")













   
    


tallest = People("Robert Wadlow", 22, "8'11\"")                                                      #<----- default profiles
smallest = People("Jyoti Amge", 30, "2'1\"")
oldest = People("Jeanne Calment", 122, "5'0\"")    
tallest.calc_feetinch(tallest.height)
smallest.calc_feetinch(smallest.height)
oldest.calc_feetinch(oldest.height)

#-------------------------------------------------------------------------------------------------------------------#

x= input("Start test. Repeat after me : ")       #<--- This is a check
print(x)



print(f"{"******": ^60}")                                                                              #<----- Header title
print(f"{"*************": ^60}")
print(f"{"********************": ^60}")
print(f"{"********* Welcome to ***********": ^60}")
print(f"{"********* the Limits of your Body! ***********": ^60}")
print(f"{"********************************": ^60}")
print(f"{"********************": ^60}")
print("\n\n\n")


switch = int(0);


#Info entry

while(switch == 0):
    try:
        user_Name = input("Please enter your name: ")                                                #<------ Questions for input
        user_Age = int(input("Please enter your age: "))
        user_Height = input("Please enter your height (Feet \', Inches \"): ")
        switch = 1
    except:
        print('Your information did not match the request. Please revise ur answers.')
        switch = 0



person1 = People(user_Name, user_Age, user_Height)  
person1.calc_feetinch(person1.height)



#print(f"\n - - - You are {person1.name} of {person1.age} years and you are {person1.feet}\'{person1.inches}\" tall. - - - ") 
#print(f"\t - - -   {person1.feet} feet and {person1.inches} inches to be exact!    - - -\n")

userResponse = "x"
while not (userResponse == "Q" or userResponse == "q"):
    print(f"\nHow would you like to test your limit?\n   H) Height\n   A) Age \n   Q) Quit")
    userResponse = input("Your response: ")

    if(userResponse == "H" or userResponse == "h"):                     #Questions for Height Entry
        userResponseH = "x"
        while not (userResponseH == "R" or userResponseH == "r"):
            print(f"\nAre you more short or tall?\n   S) Short\n   T) Tall\n   R) Return to previous")
            userResponseH = input("Your response: ")


        
            if(userResponseH == "T" or userResponseH == "t"):
                People.profileheightstack(person1, tallest)
        
            elif(userResponseH == "S" or userResponseH == "s"):
                People.profileshorteststack(smallest, person1)
        
            elif(userResponseH == "R" or userResponseH == "r"):
                continue

            else:
                print(f"\n\tInvalid Response.Please try again.")

    elif(userResponse == "A" or userResponse == "a"):
        People.oldeststack(oldest, person1)

    elif(userResponse == "q" or userResponse == "Q"):
        print("\nGoodbye!\n")

    else:
        print("\nPlease Enter a Valid Response.\n")





print(f"{"****************************************************************": ^60}")
print(f"{"********* Thank You for using our program. ***********": ^60}")
print(f"{"*********  We hope you enjoyed your time!  ***********": ^60}")
print(f"{"****************************************************": ^60}")



