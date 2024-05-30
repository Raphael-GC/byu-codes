"""
Author: Brother Burton

Purpose: Practice working with files.
"""

with open("hr_system.txt") as f:
    # The file has now been opened and stored in a variable "f"

    # Read each line, one by one, into a variable: current_line
    for line in f:
        # Strip off leading/trailing whitespace.
        # This is important, otherwise, our last variable will have \n characters with it.
        clean_line = line.strip()

        # Split the current line into its parts based on a space " " as the separator
        parts = clean_line.split(" ")

        # Save each part into a variable
        name = parts[0]
        id_number = parts[1]
        title = parts[2]
        salary = float(parts[3])

        # Output the data as desired
        # Used for Stretch #1
        # print(f"{name} (ID: {id_number}), {title} - ${salary:.2f}")

        # Calculate the paycheck amount
        pay_amount = salary / 24

        # Compute engineering bonus
        if title.lower() == "engineer":
            pay_amount += 1000

        # Output the data as desired
        print(f"{name} (ID: {id_number}), {title} - ${pay_amount:.2f}")


