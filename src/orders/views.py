from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
# from django.core.mail import send_mail
# from .tasks import order_created
from django.urls import reverse

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

            # # set the order in the session
            # request.session['order_id'] = order.id
            # # redirect for payment
            # return redirect(reverse('payment:process'))

            # send email
            subject = 'Order nr. {}'.format(order.id)
            message = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}.'.format(order.first_name, order.id)
            send_mail( subject,
                       message,
                       'mihainegrisan.cv@gmail.com',
                       [order.email])
            
            #  Celery
            # order_created.delay(order.id)
            # We call the delay() method of the task to execute it asynchronously. The task will be added to the queue and will be executed by a worker as soon as possible.


            # context = {'order': order}
            # return render(request, 'orders/order/created.html', context)
    else:
        form = OrderCreateForm()
    context = {'cart': cart,
               'form': form}
    return render(request, 'orders/order/create.html', context)
