from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)

# We can get the Product instance just through the ID since it's a unique attribute. However, we include the slug in the URL to build SEO-friendly URLs for products.
def product_detail(request, id, product_slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=product_slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    context = {'product': product,
               'cart_product_form': cart_product_form}
    return render(request, 'shop/product/detail.html', context)
