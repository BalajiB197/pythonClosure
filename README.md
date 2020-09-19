# pythonClosure
A closure is a nested function which has access to a free variable from an enclosing function that has finished its execution.

Three characteristics of a Python closure are: 
 1. it is a nested function. 
 2. it has access to a free variable in outer scope
 3. it is returned from the enclosing function

 In this assignment wrote methods to check closure for examples as web page access by different user, and track their views or how many times they accessed website.

# Methods
 1. closure_counts_dict

 for each dict there was the count of methods accessed.

 2. closure_counts  
 Global dict contains track of the number of times the methods were accessed

 3. fib  
 returns the next incremented fib after each call  

 4. counter  
 check the doc string length with the closure methods.

 A free variable is a variable that is not bound in the local scope. In order for closures to work with immutable variables such as numbers and strings, we have to use the nonlocal keyword.

Python closures help avoiding the usage of global values and provide some form of data hiding. They are used in Python decorators.

