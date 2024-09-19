class item:
  discount=0.6
  all=[]
  def __init__(self, name:str,price):
    self.name=name
    self.price=price
    assert price >=0
    item.all.append(self) 
  def calculate(self):
    print (f"the Price of {self.name} is {self.price}")
    return self.name,self.price
  def apply_discount(self):
    self.price=self.price*self.discount

  def __repr___(self):
    return f"item('{self.name}',{self.price})"


item1=item("Bottle Water",250)
item2=item("phone",3000)
item3=item("laptop",70000)
print(item.all)
