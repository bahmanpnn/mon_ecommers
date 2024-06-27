from product_module.models import Product


BASKET_SESSION_ID='basket'

class Basket:
    '''
        constructor method creates a session ,basket(if does not exists created empty dic) varibale

        add method get product and quantity of that product from form and request with BasketAddView 

        save method modified session because session does not save some actions auto and need modify 
    '''

    def __init__(self,request):
        self.session=request.session
        basket=self.session.get(BASKET_SESSION_ID)
        
        if not basket: # if basket is None:
            basket=self.session[BASKET_SESSION_ID]={}
        
        self.basket=basket
    
    def __iter__(self):
        # basket is a dict and we want to get all keys of this dict(keys are id of products) 
        # '3':{'quantity':2,'price':260} ==>'3' is key
        product_ids=self.basket.keys() #it returns a list
        products=Product.objects.filter(id__in=product_ids)
        basket=self.basket.copy()

        # now we need to add products data like product name
        for product in products:
            basket[str(product.id)]['product']=product 
            # __str__ is product.name and in basket template show str not complete obj and
            # here save entire product model obj and for that we have access to 
            # product id for removing and basket-remove url in basket table 
            # basket[str(product.id)]['product']=product.name but this make error for removing :))

        for item in basket.values():
            item['total_price']=item['quantity'] * int(item['price'])
            yield item
    

    def add(self,product,quantity):
        '''
            its clear that product and quantity uses for adding a new dic in basket dictionary!! 
            after all we need to call session to save them,for that i created new method that its name is save!!
        '''
        
        product_id=str(product.id)
        if product_id not in self.basket:
            self.basket[product_id]={'quantity':0,'price':str(product.price)}
        self.basket[product_id]['quantity']+=quantity
        self.save()

    def save(self):
        self.session.modified=True

    def remove_product(self,product):
        product_id=str(product.id)
        if product_id in self.basket:
            del(self.basket[product_id])
            self.save()

    #we can write get total price codes in basket view too,but here is better
    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.basket.values())
    
    def __len__(self):
        return len(self.basket.values())
        # return sum(item['quantity'] for item in self.basket.values())


'''
    session={

        'basket':{
            'product_id':{
                'quantity':3,
                'price':'230'
            },
            '8':{
                'quantity':3,
                'price':'230'
            },
            ...
        }
    
    }

        for product in products:
            basket[str(product.id)]['product']=product.name

        session={
            'basket':{
                'product_id':{
                    'quantity':3,
                    'price':'230',
                    'product':'product.name'
                },
                '8':{
                    'quantity':3,
                    'price':'230'
                    'product':'lenovo ideapad s540'
                },
                ...
            }
    
    }

'''
'''
    session={'basket':{'8':{'quantity':3,'price':'230'},{'3':{'quantity':2,'price':'250'}}
    
            }

    for item in basket.values():
        item['total_price']=item['quantity'] * int(item['price'])
        yield item

    session={
        'basket':
                {'8':{'quantity':3,'price':'230','product':'lenovo ideapad s540','total_price':690},
                {'3':{'quantity':2,'price':'250','product':'lenovo legion2','total_price':500}
            },

        }

'''