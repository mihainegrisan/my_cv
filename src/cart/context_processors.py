# A context processor to set the current cart into the
# request context. We will be able to access the cart in any template
from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}

# A context processor is a function that receives the request object as a
# parameter and returns a dictionary of objects that will be available
# to all the templates rendered using RequestContext.

# 'cart.context_processors.cart',

# The cart context processor will be executed every time a template is
# rendered using Django's RequestContext. The cart variable will be set in
# the context of your templates.
# Context processors are executed in all the requests that use RequestContext.
# You might want to create a custom template tag instead of a context processor if your functionality is not needed in all templates, especially if it involves database queries.
