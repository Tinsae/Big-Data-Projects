#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Read FairDealCustomerData.csv
import csv,sys,re,random
with open('datasets/FairDealCustomerData.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    cdata = []
    for row in reader:
        lname = row[0].strip()
        namelist = re.split(r'(\s)', row[1].strip())
        blacklisted = int(row[2])
        # remove space
        namelist = [s for s in namelist if s != ' ']
        title = namelist[0]
        fname = namelist[1]
        cdata.append((title, fname, lname, blacklisted))    


# In[2]:


# 4. Create Custom Exception – CustomerNotAllowedException
class Error(Exception):
   """Base class for other exceptions"""
   pass
class CustomerNotAllowedException(Error):
   """Raised when customer is blacklisted"""
# 3. Store the data in Customer Class
class Customer:

    def __init__(self, title, fname, lname, blacklisted):
        # private
        self.__title = title
        self.__fname = fname
        self.__lname = lname
        self.__blacklisted = blacklisted

    def __str__(self):
        return "{:10s} {:18s} {:18s} {:5d}".format(self.__title, self.__fname, self.__lname, self.__blacklisted)

    def setIsblacklisted(self, blacklisted):
        self.__blacklisted = blacklisted

    def isblacklisted(self):
        return self.__blacklisted

    def setTitle(self,title):
        self.__title = title

    def getTitle(self):
        return self.__title

    def setFname(self,fname):
        self.__fname = fname

    def getFname(self):
        return self.__fname

    def setLname(self,lname):
        self.__lname = lname

    def getLname(self):
        return self.__lname
    # Change function createOrder to take productname and product code as input
    def createOrder(self, pname, pcode):
        try:
            if (self.isblacklisted()):
                raise CustomerNotAllowedException
            # Return object of type Order in case customer is eligible
            else:
                print("product ordered")
                return Order(pname, pcode)
        except CustomerNotAllowedException:
            print("Customer is blacklisted and cannot order")

class Order:
    def __init__(self, name, code):
        self.__name = name
        self.__code = code
    
    def getName():
        return __name
    def setName(name):
        self.__name = name
    def getCode():
        return __code
    def setCode(code):
        self.__code = code
       
customers = []
for title, fname, lname, blacklisted in cdata:
    customers.append(Customer(title, fname, lname, blacklisted))
print(len(customers), " customer objects")    


# In[3]:


indices = random.choices(range(532), k=10)
print(indices)
# check how many of them are blacklisted
print("10 randomly selected customers- blacklisted ?")
for i in indices:
    print(customers[i].isblacklisted(), end=",")
print()


# In[4]:


# call create order on each customer
# suppose all 10 customers ordered the same product
print("10 customers trying to order the same product")
for i in indices:
    customers[i].createOrder("p-9777", "ergonomic_chair")

