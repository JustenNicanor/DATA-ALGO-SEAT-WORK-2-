#Display a menu of options
print("~~~~~MENU~~~~~")
print()
print("(1) Add an Item")
print("(2) Search")
print("(3) Exit (y/n)")
print()
print("~~~~~~~~~~~~~~")


while True:
    #Asking user for action
    userans = int(input("Which action do you desire? "))
    #no.1 personal infos
    if userans == 1:
        surname = input("Enter your Surname: ")
        givename = input("Enter your Given name: ")
        middlename = input("Enter your Middle name: ")
        sex = input("Sex: ")
        age = (input("Age: "))
        birthmonth = input("Birth Month: ")
        dayofbirth = (input("Day of Birth: "))
        birthyear = (input("Birth year: "))
        placeofbirth = input("Place of Birth: ")
        langguage = input("Langguage: ")
        occupation = input("Occupation: ")
        contactnu = (input("Contact Number: "))
        citizenship = input("Citizenship: ")
        province = input("Province: ")
        city = input("City: ")
        baranggay = input("Brgy: ")
        religion = input("Religion: ")
        status = input("Status: ")
        print("SAVED!")
    elif userans == 2:
        askuser = input("Enter your Surname to search: ")
        if askuser == surname:
            print(dictionary)
        elif askuser != surname:
            print("Please add Item First or Check the spelling and the captalization you input.")
    elif userans == 3:
        yesno = input("Are you sure? (y or n): ")
        if yesno == "y":
            break
    dictionary = {
            "Surname": surname,
            "Given name": givename,
            "Middle name": middlename,
            "Sex" : sex,
            "Age" : age,
            "Birth Month" : birthmonth,
            "Day of Birth" :  dayofbirth,
            "Birth year" : birthyear, 
            "Place of Birth" :  placeofbirth,
            "Langguage" : langguage,
            "Occupation" : occupation,
            "Contact Number" : contactnu,
            "Citizenship" :  citizenship,
            "Province" : province,
            "City" : city, 
            "Brgy" : baranggay,
            "Religion" : religion,
            "Status" : status  
        } 










