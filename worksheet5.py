#print (2 ** 3 ** 2)#
#print (2 * 3 ** 3 * 4)#
#print (10 - 4 * 2)#
#print (-18 // 4)#
#print (2%6)#
''''x = 100  
y = 50  
print(x and y)'''''

#print(36 / 4)#
'''''var1 = 1  
var2 = 2  
var3 = "3"  
print (var1 + var2 + var3)
Python does not allow adding an int and a str directly.'''''

'''''p, q, r = 10, 20 ,30  
print(p, q, r)'''''

'''''valueOne = 5 ** 2  
valueTwo = 5 ** 3  
print(valueOne) 
print(valueTwo)'''''

'''''var = "James" * 2 * 3  
print(var)'''''

'''''x = 36 / 4 * (3 + 2) * 4 + 2  
print(x)'''''

#print(type (10))#
'''''Roll_number =33  
marks= 25
print(Roll_number,type(Roll_number))
print(marks,type(marks))'''''

'''''a=int(input("enter a value:"))
b=float(input("enter b value:"))
c=input("enter c value:")
print(a,type(a))
print(b,type(b))
print(c,type(c))'''''



#======== home_work-4 ========#


'''''x=10
y=5
x,y=y,x
print("after_swaping")
print("x:",x)
print("y:",y)'''''

'''''n=35555
m=2.564728
o=2 + 3j
print(n,type(n))
print(m,type(m))
print(o,type(o))'''''

'''''x = 6  
y = 2 
print(x ** y)  
print(x // y)

o/p:
36
3'''''

'''''a = 4  
b = 11  
print(a | b) 
print(a >> 2)
o/p:
15
1'''''

'''''y = 10  
x = y += 2 
print(x)
This will result in a syntax error in Python.'''''

'''''print(2 * 3 ** 3 * 4)
o/p:
216'''''

'''''print(10 - 4 * 2)
o/p:
2'''''

'''''print(-18 // 4)
o/p:
-5'''''

'''''x = 10  
y = 50  
if x ** 2 > 100 and y < 100:  
    print(x,y) 
    o/p:
    nothing'''''


'''''x = 100  
y = 50  
print(x and y)
o/p: 50'''''

'''''print(type(range(5)))
o/p: <class 'range'>'''''

'''''print(type(10))
o/p:<class 'int'>'''''



#====== Home Work III (Day 3.1) =====#

'''''glass_of_water=3  
glass_of_water=glass_of_water + 1  
print(glass_of_water) 
o/p: 4'''''


'''''glass_of_water= 6
print("I drank", glass_of_water, "glasses of water today.")

o/p: I drank 6 glasses of water today.'''''

'''''men_stepped_on_the_moon= 10
print(men_stepped_on_the_moon)
 o/p: 10'''''

'''''my_reason_for_coding=input("enter a name:")
print(my_reason_for_coding)
o/p: enter a name:indra
indra'''''


'''''global_mean_sea_level_2018=21  
global_mean_sea_level_2018=519.00 
print(global_mean_sea_level_2018)
o/p=519.00'''''

'''''staying_alive= "True or false"
print(staying_alive)
o/p: True'''''

#print("Earth", 2025)#
'''''my_text="Hello World!" 
print(my_text)'''''
'''''. In Python, a variable must be declared before it is assigned a value: 
A. True 
B. False
answeer: False'''''

'''''employee_number = 6
Employee_Number = 7
employee_Number = 8
print(employee_number)
print(Employee_Number)    
print(employee_Number)  '''''  


#print( 5*2**10)#


'''''my_list=list(["Rose","Peony","Orchids"])
print(my_list)'''''

'''''list=[1,2,3,4,5,6,7,8]
len=len(list)
print(len)'''''
'''''l1=[1,2,3,4,5,6,7,8]
l1.sort()
l1.sort(reverse=True)
print("Revers list:",l1)'''''

import tkinter as tk

# Function to perform addition
def add_numbers():
    try:
        first_number = int(entry1.get())
        second_number = int(entry2.get())
        result = first_number + second_number
        result_label.config(text="Result: " + str(result), fg="red")
    except ValueError:
        result_label.config(text="Please enter valid numbers", fg="red")

# Create main window
window = tk.Tk()
window.title("GUI Addition")
window.geometry("400x250")  # width x height

# Label and Entry for first number
label1 = tk.Label(window, text="Enter The First Number:")
label1.pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack(pady=5)

# Label and Entry for second number
label2 = tk.Label(window, text="Enter The Second Number:")
label2.pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack(pady=5)

# Label for result
result_label = tk.Label(window, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

# Submit button
submit_button = tk.Button(window, text="Submit", command=add_numbers)
submit_button.pack(pady=5)

# Run the window
window.mainloop()

