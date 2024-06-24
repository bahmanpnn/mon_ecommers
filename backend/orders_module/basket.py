BASKET_SESSION_ID='basket'

class Basket:
    def __init__(self,request):
        self.session=request.session
        basket=self.session.get(BASKET_SESSION_ID)
        
        # if basket is None:
        if not basket:
            basket=self.session[BASKET_SESSION_ID]={}
        
        self.basket=basket