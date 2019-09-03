from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
# from .tasks import order_created

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the Cart
            cart.clear()


            #  Celery
            # order_created.delay(order.id)
            # We call the delay() method of the task to execute it asynchronously. The task will be added to the queue and will be executed by a worker as soon as possible.

            context = {'order': order}
            return render(request, 'orders/order/created.html', context)
    else:
        form = OrderCreateForm()
    context = {'cart': cart,
               'form': form}
    return render(request, 'orders/order/create.html', context)
