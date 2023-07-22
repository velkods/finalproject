from datetime import date
from django.shortcuts import render
from .models import GoodsList
from django.shortcuts import get_object_or_404

# Create your views here.

def all_goods(request):
  goods_list = GoodsList.objects.all()
  return render(request, "store/all_products.html", {'goods_list' : goods_list}) 

def all_goods_starting_page(request):
  goods_list_home = GoodsList.objects.all()
  return render(request, "store/index.html", {'goods_list' : goods_list_home}) 

def starting_page(request):
  goods_list = GoodsList.objects.all()
  return render(request, "store/index.html", {'goods_list' : goods_list})

def products(request):
  return render(request, "store/all_products.html")

def product_detail(request, slug):
  return render(request, "store/product_detail.html")

all_products = [
  {
    "slug": "jeans-for-sale",
    "title": "Jeans",
    "image": "jeans.png",
    "price": 1000,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": True,
    "date": date(2023, 6, 21),
  },
  {
    "slug": "eyewear",
    "title": "Eyewear",
    "image": "eyewear.jpeg",
    "price": 2000,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": True,
    "date": date(2023, 6, 10),
  },
  {
    "slug": "shirt",
    "title": "Shirt",
    "image": "shirt.png",
    "price": 500,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": True,
    "date": date(2023, 6, 22),
  },
  {
    "slug": "shop_img",
    "title": "Shop",
    "image": "shop_img.jpg",
    "price": 500,
    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.",
    "availability": False,
    "date": date(2023, 6, 2),
  },
]

def get_date(product):
  return product['date']

def starting_page(request):
  sorted_products = sorted(all_products, key=get_date)
  latest_products = sorted_products[-3:]
  return render(request, "store/index.html", {
    "products": latest_products
  })

def products(request):
  return render(request, "store/all_products.html", {
    "all_products": all_products
  })

def product_detail(request, slug):
  identified_product = get_object_or_404(GoodsList, slug=slug)
  return render(request, "store/product_detail.html", {
    "product": identified_product
  }) 