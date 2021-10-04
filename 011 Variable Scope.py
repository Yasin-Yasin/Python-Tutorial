# LEGB - Local, Enclosing, Global, Built-in
 
x = 'global x' # Global Variable as it is declared in main-scope

def test():
    y = 'local y'  # Local Variable as it is decalred insde a function
    print(y) # Can access here in function but not outside 
    # print(x) # python first check for local- not there, enclosing - not there, global - there
    x = 'local x'
    print(x) # Now when it checked for local first, and found it so it will take that instead of global x

test()
# print(y) Can't access as it is a local variable, can only be accessed in that function
# print(x) 
var = 'global var'
def test1 ():
    global var # change global var inside function
    var = 'local var' # It will set global var to 'local var' because global var above  this line
    print(var)

test1()
print(var)

def test2():
    global a
    a = 'local a'
    print(a)

test2()
print(a) # Although a is defined in function it will be accessible outside function because it is set as global by global keyword


def test3(z):
    print(z) # z is local variable

test3('local z')

# Built-in

m = min([5,1,4,2,3])
print(m)

import builtins

# print(dir(builtins)) # Builtin variable

# Be careful to not overwrite builtin

# Enclosing

def outer():
    m = 'Outer m'

    def inner():
        m = 'Inner m' 
        print(m) # inner m as it is first look up for local which is there defined in inner local to inner
    
    inner()
    print(m) # outer m - local to outer

outer()
     
    
# Enclosing

d = 'global d'
def outer1():
    d = 'Outer d'

    def inner1():
        print(d) # It will look for local which isn't there,  Enclosing - it is there d is encloing variable as it define in outer function
    
    inner1()
    print(d)

outer1()

# nonlocal 
e = 'global e'
def outer2():
    e = 'Outer e'

    def inner1():
        nonlocal e # Just Like global but only winthin function without affecting the global scope
        e = 'inner e'
        print(e) 
    
    inner1()
    print(e)

outer2()
print(e) # global

