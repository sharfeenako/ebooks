from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Comment,Book


# Create your views here.

def index(request):
    context={
     'is_index':True

    }
    return render(request,"web/index.html",context)

def shop(request):

    comments = Comment.objects.filter(approved=True)

    return render(request, 'web/shop-list.html', {'comments': comments})

def book(request):
    

    year = request.GET.get('year')
    language = request.GET.get('language')


    if year:
        book = book.filter(year=year)
    if language:
        book = book.filter(language=language)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price and max_price:
    # Assuming the 'price' field is present in the 'Book' model
        book = book.filter(price__gte=min_price, price__lte=max_price)

  
    context={
   
    'book':Book.objects.all(),

    }
    return render(request, 'web/shop-grid.html',context)




def register_1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if(pass1!=pass2):
            print('password not equal'*20)
            return redirect('web:signup')
        else:
            if User.objects.filter(username=username).exists():
                print('user already exist')
                return redirect('web:signup')
            else:
                customer = User.objects.create_user(username=username,password=pass1)
                return redirect('web:login')
           

    return render(request,"web/register.html")
          
def login_1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('web:index')
        else:  
            print('hi')
            return redirect('web:signup')
    return render(request,"web/login.html")

@login_required
def comment_submit(request):
    if request.method == 'POST':
        content = request.POST['content']
        author = request.user
        comment = Comment(content=content, author=author)
        comment.save()
        return redirect('web:shop')

    return render(request, 'web/comment_submit.html')





def logout_1(request):
    logout(request)
    return redirect('web:index')
def shop_detail(request,id):
       
    book =Book.objects.get(id=id)
    context={

        'book':book,

    }
    
    return render(request,'web/single-product.html',context)