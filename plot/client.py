from inspect import Signature, Parameter, signature

def test(a,b):
    pass 

a = signature(test)
p = Parameter()
print(a)