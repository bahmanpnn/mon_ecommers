from .basket import Basket


def basket_product_counts(request):
    return {'counts':Basket(request)}