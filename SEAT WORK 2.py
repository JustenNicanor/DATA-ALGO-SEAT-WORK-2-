#Display a menu of options
dictionary = { } 


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

        dictionary[surname] = givename, middlename, sex, age, birthmonth, dayofbirth, birthyear, placeofbirth, langguage, occupation, contactnu, citizenship, province, city, baranggay, religion, status
    elif userans == 2:
        askuser = input("Enter your Surname to search: ")
        if askuser in dictionary:
            print(f"{askuser}'s Informations: {dictionary[askuser]}")
        else:
            print("Your Information is not added already or Check the spelling.")
    elif userans == 3:
        yesno = input("Are you sure? (y or n): ")
        if yesno == "y":
            break
    










