class Sample:
    global a
    a=10
    
    def __init__(self):
        print('constructor of Sample is called')

    def hello(self):
      print('hello')
    
    def Name(self,name):
        print('name='+name)

    def values(self):
        print("value="+str(a))    

x=Sample()
x.hello()
x.Name('anandhu')
x.Name('anandh')
x.values()