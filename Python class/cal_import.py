
# module

# syntax -- from module-(filename) import function_name
from calculator import add 

# syntax -- from package.module import function_name
# package -- folder name & module-(filename)

x=add(20,80)
print("add:",x)

from calculator import sub 

y = sub(100,20)
print("sub:",y)

from calculator import mult 

y = mult(100,20)
print("mult:",y)

from calculator import div 

y = div(100,20)
print("div:",y)

from calculator import power 

y = power(20,2)
print("power:",y)

from calculator import sell,output

x = sell(10)
output("sell",x)





