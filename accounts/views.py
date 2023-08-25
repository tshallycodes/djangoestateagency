from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Users
from listing.models import Properties
from message.models import MyMessages


def loginPage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if email == '' or password == '':
            messages.error(request, 'All fields are required')
            return redirect('login')

        if Users.objects.filter(email=email).exists():
            try:
                user = authenticate(request, username=email, password=password) 
            except ValueError as e:
                print(e)
                messages.error(request, 'Error authenticating user')
                return redirect('login')

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Error signing in user')
                return redirect('login')
        else:
            messages.error(request, 'Invalid email address')
            return redirect('login')
                              
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        fullname = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        twitter = request.POST['twi']
        instagram = request.POST['inst']
        facebook = request.POST['fac']
        description = request.POST['desc']
        photo = request.FILES.get('file')

        if fullname == '' or email == '' or phone == '' or password == '' or twitter == '' or instagram == '' or facebook == '' or description == '':
            messages.error(request, 'All fields are required')
            return redirect('register')
        
        if not photo:
            messages.error(request, 'Image is required')
            return redirect('register')
        
        # check email
        if Users.objects.filter(email=email).exists():
            messages.error(request, 'Email address already taken')
            return redirect('register')
        
        try:
            newuser = Users.objects.create_user(fullname=fullname, phone=phone, email=email, password=password, facebook=facebook, twitter=twitter, instagram=instagram, description=description, photo=photo)

            messages.success(request, 'Now login with your details')
            return redirect('login')
        except Exception as e:
            messages.error(request, 'Error creating account')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


@login_required(login_url='login')
def msg(request):
    
    mymessage = MyMessages.objects.order_by('-msg_date').filter(agent_id=request.user.id)

    context = {
        'msgs': mymessage
    }

    return render(request, 'accounts/messages.html', context)


@login_required(login_url='login')
def profile(request):
    agent = get_object_or_404(Users, pk=request.user.id)

    properties = Properties.objects.order_by('-list_date').filter(agent_id=request.user.id)

    context = {
        'agent': agent,
        'pcount': len(properties),
        'properties': properties
    }

    return render(request, 'accounts/profile.html', context)


@login_required(login_url='login')
def settings(request):
    if request.method == 'POST':
        fullname = request.POST['name']
        phone = request.POST['phone']
        twitter = request.POST['twi']
        instagram = request.POST['inst']
        facebook = request.POST['fac']
        description = request.POST['desc']
        photo = request.FILES.get('file')

        if fullname == '' or phone == '' or twitter == '' or instagram == '' or facebook == '' or description == '':
            messages.error(request, 'All fields are required')
            return redirect('settings')
        
        member = Users.objects.get(id=request.user.id)
        if not photo:
            member.fullname = fullname
            member.phone = phone
            member.twitter = twitter
            member.instagram = instagram
            member.description = description
            member.save()
            messages.success(request, 'Account Updated')
            return redirect('settings')
        else:
            member.fullname = fullname
            member.phone = phone
            member.twitter = twitter
            member.instagram = instagram
            member.description = description
            member.photo = photo
            member.save()
            messages.success(request, 'Account Updated')
            return redirect('settings')
    else:
        return render(request, 'accounts/settings.html')


@login_required(login_url='login')
def edit(request, listing_id):
    if method == 'POST':
        name = request.POST['name']   
        location = request.POST['location']   
        type = request.POST['type']   
        status = request.POST['status']   
        area = request.POST['area']   
        bed = request.POST['bed']   
        bath = request.POST['bath']   
        garage = request.POST['garage']   
        desc = request.POST['desc']   
        price = request.POST['price']   
        photo = request.FILES.get('file')

        item = Properties.objects.get(id=listing_id)

        if not photo:
            item.name = name
            item.location = location
            item.ptype = type
            item.status = status
            item.area = area
            item.bed = bed
            item.bath = bath
            item.garage = garage
            item.description = desc
            item.price = price
            item.save()
            messages.success(request, 'Property Updated')
            return redirect('/user/edit/' + str(listing_id))
        
        else:
            property = get_object_or_404(Properties, pk=listing_id)
            item.name = name
            item.location = location
            item.ptype = type
            item.status = status
            item.bed = bed
            item.bath = bath
            item.garage = garage
            item.area = area
            item.description = desc
            item.photo = photo 
            item.price = price
            item.save()
            messages.success(request, 'Property Updated')
            return redirect('/user/edit/' + str(listing_id))
        
    else:
        property = get_object_or_404(Properties, pk=listing_id)

        context = {
            'property' : property
        }
        return render(request, 'accounts/edit.html', context)


@login_required(login_url='login')
def my_logout(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('login')