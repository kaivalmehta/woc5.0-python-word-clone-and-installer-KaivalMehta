 
import csv

class Item :

    all=[]
    def __init__(self,name,price,quantity) :

        assert price>=0
        assert quantity>=0
        self.name=name
        self.price=price
        self.quantity=quantity

        Item.all.append(self)
    def total(self):
        return self.price*self.quantity
    @classmethod
    def instantiate_form_csv(cls) :
        with open('data.csv','r') as f :
            reader=csv.DictReader(f)
            items=list(reader)

        for item in items :
            print(item)



    def __repr__(self) :
        return f"{self.__class__.__name__}({self.name},{self.price},{self.quantity})"
class Phone(Item) :
    def __init__(self,name,price,quantity=0,brokenphones=0) :

        super().__init__(
        name,price,quantity
        )
        assert brokenphones>=0
        self.brokenphones=brokenphones
    


    

phone1=Phone("Phone1",500,5)
print(Item.all)
print(Phone.all)
Item.instantiate_form_csv()