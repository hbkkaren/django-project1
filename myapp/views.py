from django.shortcuts import redirect, render
from .models import User,Product,Wishlist,Cart
import requests
import random
import stripe
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
from django.http import JsonResponse

# Create your views here.

stripe.api_key = settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN = 'http://localhost:8000'

def validate_signup(request):
	email=request.GET.get('email')
	data={
		'is_taken':User.objects.filter(email__iexact=email).exists()
	}
	return JsonResponse(data)




@csrf_exempt
def create_checkout_session(request):
	amount = int(json.load(request)['post_data'])
	final_amount=amount*100
	
	session = stripe.checkout.Session.create(
		payment_method_types=['card'],
		line_items=[{
			'price_data': {
				'currency': 'inr',
				'product_data': {
					'name': 'Checkout Session Data',
					},
				'unit_amount': final_amount,
				},
			'quantity': 1,
			}],
		mode='payment',
		success_url=YOUR_DOMAIN + '/success.html',
		cancel_url=YOUR_DOMAIN + '/cancel.html',)
	return JsonResponse({'id': session.id})

def success(request):
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,payment_status=False)
	for i in carts:
		i.payment_status=True
		i.save()
		
	carts=Cart.objects.filter(user=user,payment_status=False)
	request.session['cart_count']=len(carts)
	return render(request,'success.html')

def cancel(request):
	return render(request,'cancel.html')





def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')
def blog(request):
    return render(request,'blog.html')
def cart(request):
    return render(request,'cart.html')
def category(request):
    products=Product.objects.all()
    return render(request,'category.html',{'products':products})
def confirmation(request):
    return render(request,'confirmation.html')

def contact(request):
    return render(request,'contact.html')

def elements(request):
    return render(request,'elements.html')


def login(request):
    if request.method=='POST':
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password== request.POST['password']:
               if user.usertype=='buyer':
                    request.session['email']= user.email
                    request.session['fname']= user.fname
                    wishlists=Wishlist.objects.filter(user=user)
                    carts=Cart.objects.filter(user=user,payment_status=False)
                    request.session['wishlist_count']=len(wishlists)
                    request.session['cart_count']=len(carts)
                    return render(request,'index.html')
               else:
                    request.session['email']= user.email
                    request.session['fname']= user.fname
                    return render(request,'seller-index.html')
            else:
                msg="incorrect password"
                return render(request,'login.html',{'msg':msg})
        except:
            msg= "email not register"
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    
def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        del request.session['wishlist_count']
        del request.session['cart_count']

        
        return render(request,'login.html')
    except:
        return render(request,'login.html')


def single_blog(request):
    return render(request,'single-blog.html')

def single_product(request):
    return render(request,'single-product.html')

def single_product(request):
    return render(request,'single-product.html')

def tracking(request):
    return render(request,'tracking.html')

def checkout(request):
    return render(request,'checkout.html')

def signup(request):
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            msg= 'email alread registerd'
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                    usertype =request.POST['usertype'],
                     )  
                msg=' User registerd successfully '
                return render(request,'signup.html',{'msg':msg})
            
            else:
                msg='password & confirm password does not mached'
                return render(request,'signup.html')
    else:
        return render(request,'signup.html')
    

def change_password(request):
    if request.method == 'POST':
        user = User.objects.get(email = request.session['email'])
        if user.password == request.POST['old_password']:
            if request.POST['new_password']== request.POST['cnew_password']:
                user.password = request.POST['new_password']
                user.save()
                return redirect('logout')
            else:
                msg="New password &b confirm new password Does not mached "
                return render(request,'change-password.html',{'msg':msg})
        else:
                msg="old password does not mached "
                return render(request,'change-password.html',{'msg':msg})
        
            
    else:


        return render(request,'change-password.html')


def seller_add_product(request):
    seller = User.objects.get(email=request.session['email'])
    if request.method=="POST":
        Product.objects.create(
            seller = seller,
            Product_brand=request.POST['product_brand'],
            product_price=request.POST['product_price'],
            product_size=request.POST['product_size'],
            product_pic=request.FILES['product_pic'],
        )

        msg="product added successfully"
        return render(request,'seller-add-product.html',{'msg':msg})
    else:
        return render(request,'seller-add-product.html')
    

def seller_view_product(request):
   seller =User.objects.get(email=request.session['email'])
   products= Product.objects.filter(seller=seller)
   return render(request,'seller-view-product.html',{ 'products':products })
 
def seller_product_detail(request,pk):
    products=Product.objects.get(pk=pk)
    return render(request,'seller-product-detail.html',{'product':products})

def seller_edit_product(request,pk):
    products=Product.objects.get(pk=pk)
    if request.method=="POST":
        products.Product_brand=request.POST['Product_brand']
        products.product_price = request.POST['product_price']
        products.product_size = request.POST['produect_size']

        try:
            products.product_pic= request.FILES['product_pic']
        except:
            pass
        products.save()
        msg="Product Updated Sucessfully"
    
    else:
        return render(request,'seller-edit-product.html',{'product':products})

def seller_index(request):
    return render(request,'seller-index.html')

def seller_delete_product(request,pk):
    products=Product.objects.get(pk=pk)
    products.delete()
    return redirect('seller-view-product')

def product_detail(request,pk):
    wishlist_flag= False
    cart_flag=False
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    try:
        Wishlist.objects.get(user=user,product=product)
        wishlist_flag = True
        
    except :
        
        pass
    try:
        Cart.objects.get(user=user,product=product)
        cart_flag = True
        
    except :
        
        pass
    return render(request,'product-detail.html',{'product':product,'cart_flag':cart_flag,'cart_flag':cart_flag})

def add_to_wishlist(request,pk):
    product =Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Wishlist.objects.create(user=user,product=product)
    return redirect('wishlist')

def wishlist(request):
    user =User.objects.get(email=request.session['email'])
    wishlists =Wishlist.objects.filter(user= user)
    request.session['wishlist_count']=len(wishlists)

    return render(request, 'wishlist.html',{'wishlists':wishlists })

def remove_from_wishlist(request,pk):
    product =Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    wishlist=Wishlist.objects.get(user=user,product=product)
    wishlist.delete()
    return redirect('wishlist')

def add_to_cart(request,pk):
    product =Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Cart.objects.create(
        user=user,
        product=product,
        product_price=product.product_price,
        product_qty=1,
        total_price= product.product_price)
    return redirect('cart')

def cart(request):
    net_price=0
    user =User.objects.get(email=request.session['email'])
    carts =Cart.objects.filter(user= user,payment_status=False)
    for i in carts:
        net_price = net_price + i.total_price
    request.session['cart_count']=len(carts)

    return render(request, 'cart.html',{'carts':carts ,'net_price':net_price})

def remove_from_cart(request,pk):
    product =Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    cart=Cart.objects.get(user=user,product=product)
    cart.delete()
    return redirect('cart')
def change_qty(request):
    pk=int(request.POST['pk'])
    product_qty=int(request.POST['product_qty'])
    cart=Cart.objects.get(pk=pk)
    cart.total_price= cart.product_price*product_qty
    cart.product_qty=product_qty
    cart.save()
    return redirect('cart')

def forgot_password(request):
    if request.method == "POST":
            try:
                url = "https://www.fast2sms.com/dev/bulkV2"
                mobile= request.POST['mobile']
                otp = random.randint(1000,9999)

                querystring = {"authorization":"mIk9Ya7tBzZTeAU5C3VGyLwJuRH8ogc2xrqnsKMdPSib6W0jNlQCyZJVL4px2luo8hKgraUk9b3GWejM","variables_values":str(otp),"route":"otp","numbers":str(mobile)}

                headers = {
                    'cache-control': "no-cache"
                }

                response = requests.request("GET", url, headers=headers, params=querystring)

                print(response.text)
                return render(request,'otp.html',{'mobile':mobile,'otp':otp})
            except:
                msg="Mobile Number Not Registered"
                return render(request,'forgot-password.html',{'msg':msg})
    else:

        return render(request,'forgot-password.html')
    
def verify_otp(request):
    mobile=request.POST['mobile']    
    otp=request.POST['otp']    
    uotp=request.POST['uotp']    

    if otp == uotp:
        return render(request,'new-password.html',{'mobile':mobile})
    else:
        msg="invalid otp"
        return render(request,'otp.html',{'mobile':mobile,'otp':otp,'msg':msg})
    
def new_password(request):
    mobile=request.POST['mobile']
    np=request.POST['new_password']
    cnp=request.POST['cnew_password']

    if np==cnp:
        user=User.objects.get(mobile=mobile) 
        user.password=np
        user.save()
        msg="password updataed successfully"
        return render(request,'login.html',{'msg':msg})
    else:
        msg="password & confirm password does not matched"
        return render(request,'new-password.html',{'mobile':mobile,'msg':msg})
    
def myorder(request):
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,payment_status=True)
	return render(request,'myorder.html',{'carts':carts})













    

    




        

        


    

