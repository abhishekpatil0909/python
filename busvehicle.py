#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Bike1:
    name = ""
    gear = 0
    def __init__(self , name , gear):
        self.name = name
        self.gear = gear

bike1 =(Bike1("abc" , 2))
print(bike1.name , bike1.gear) 


# In[24]:


class vehicle:
    name = ""
    max_speed = 0
    mileage =  0
    
    def __init__(self, name , max_speed , mileage):
        self.name = name
        self. max_speed = max_speed
        self.mileage = mileage
    
    def display(self):
        print(self.name , self.max_speed, self.mileage)
    
class bus(vehicle):
    def print():
        print("bus is called")
        
bus_det = bus("maruti" , 100 , 50)
bus_det.display()
bus_det.print()
    


# In[23]:


class Vehicle:
    name = ""
    max_speed  = 0
    mileage = 0
    
    def __init__(self, name , max_speed , mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity (self, capacity):
        return f"the seating capacity of a {self.name } is {capacity} passengers"
    
    
class bus(Vehicle):
        def seating_capacity(self , capacity = 50):
            return f"The seating capacity oa a {self.name } is {capacity} passengers"
        
bus("school bus", 120 , 2990).seating_capacity()


# In[30]:


class Vehicle:
    def __init__(self, name , mileage , capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    
    def fare(self):
        return self.capacity * 100
    
class Bus(Vehicle):
    
    def fare(self):
        fare_car = self.capacity * 100
        total_fare = fare_car + (0.1 *fare_car)
        return total_fare
    
School_bus = Bus("Schoool Volvo", 12, 50)
print("Total Bus fare is:",School_bus.fare())
    


# In[ ]:




