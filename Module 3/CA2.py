#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Read file bank-data.csv
import csv,sys
with open('datasets/bank-data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    # Skip first line
    next(reader)
    # Build a set of unique jobs
    profs = set()
    # Store age in dictionary
    age_dict = {"min_age":1e20, "max_age":-1}
    # Compute max and min age
    min_age = 1e20
    max_age = -1
    for row in reader:
        age = int(row[0])
        if age < age_dict["min_age"]:
            age_dict["min_age"] = age
        if age > age_dict["max_age"]:
            age_dict["max_age"] = age
        prof = row[1]
        profs.add(prof.lower().strip())
# End only if user types "END" for profession
prof = "scientist"
while(True):
    # Read the input from command line –profession
    prof = input("Enter profession: ")
    if(prof.lower() == "end"):
        break
    # Check if profession is in list
    # Print whether client is eligible
    # Make the profession check case insensitive
    if(prof.lower() in profs):
        if(age >= age_dict["min_age"] and age <= age_dict["max_age"]):
            print("You are eligible")
        else:
            print("Not eligible due to your age")
    else:
        print("Not eligible due to your job")

