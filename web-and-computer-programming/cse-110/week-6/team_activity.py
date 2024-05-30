# Team Activity

#CORE REQUIREMENTS
# Reading a file and putting it into a variable called hr_doc. 
# (In my case, I needed to change the usual syntax and use the slash in the address instead of the backslash - default in Windows addresses)
#with open("c:/Users/rapha/my-codes/byu-codes/web-and-computer-programming/cse-110/week-6/hr_system.txt") as hr_doc:
#    # getting information from each line in the file
#    for line in hr_doc:
#        # Braking the line after each space. In this case, we have four columns [0][1][2][3].
#        parts = line.split(" ")
#    
#        name = parts[0]
#        job_title = parts[2]
#        print(f"Name: {name}, Title: {job_title}")

#STRETCH CHALLENGE
with open("c:/Users/rapha/my-codes/byu-codes/web-and-computer-programming/cse-110/week-6/hr_system.txt") as hr_doc:
    # Getting information from each line in the file
    for line in hr_doc:        
        # Braking the line after each space. In this case, we have four columns [0][1][2][3].
        parts = line.strip().split(" ") # Strip off any leading and trailing whitespace from each line.

        name = parts[0]
        job_title = parts[2]
        id_number = parts[1]
        salary = float(parts[3])

        biweekly_payment = salary / 24 # They receive payment twice a month.

        if job_title == "Engineer": # bonuses for anyone who is an engineer. 
            biweekly_payment += 1000

        print(f"{name} (ID: {id_number}), {job_title} - ${biweekly_payment:.2f}")
