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