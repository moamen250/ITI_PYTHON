is_quit = False
while is_quit == False:
        print("what do you want to do")
        print(" Enter 1 to replace()  \n Enter 2 for split() \n Enter 3 for upper() \n Enter 4 for title()")

        selected = int(input("Enter the number corresponding to the activity you want to do: "))

        if selected == 1:
            print("******************************************************************************************")
            print("Returns a string where a specified value is replaced with a specified value")
            print("Example for replace() \ntxt = I like bananas \n x = txt.replace(bananas, apples) \n print(x)")
            print("******************************************************************************************")
        elif selected == 2:
             print("******************************************************************************************")
             print("Splits the string at the specified separator, and returns a list")
             print("Example for split() \n txt = welcome to the jungle \n x = txt.split() \n print(x)")
             print("******************************************************************************************")
        elif selected == 3 :
            print("******************************************************************************************")
            print("Converts a string into upper case")
            print("Example for upper() \n txt = \"Hello my friends\" \n x = txt.upper() \n print(x)")
            print("******************************************************************************************")
        elif selected == 4:
             print("******************************************************************************************")
             print("Converts the first character of each word to upper case")
             print("Example for title() \n txt = \"Welcome to my world\" \n x = txt.title() \n print(x)")
             print("******************************************************************************************")
        elif selected == 0:
             is_quit = True
        else:
            print("Please enter a correct value shown")
else:
    print("Entered wrong pin")