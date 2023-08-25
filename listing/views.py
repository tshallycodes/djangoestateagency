from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Properties
from accounts.models import Users


def categories(request):
    properties = Properties.objects.order_by('-list_date')

    context = {
        'properties': properties
    }

    return render(request, 'listing/categories.html', context)

def agents(request):
    agents = Users.objects.order_by('-reg_date').filter(is_superuser=False)

    context = {
        'agents': agents
    }

    return render(request, 'listing/agents.html', context)


@login_required(login_url='login')
def createPost(request):
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
    agentid = request.user

    try:
        items = Properties(agent_id=agentid, name=name, location=location, ptype=type, status=status, area=area, bed=bed, bath=bath, garage=garage, description=desc, photo=photo, price=price)
        items.save()

        messages.success(request, 'Post uploaded successfully')
        return redirect('dashboard')
    except Exception as e:
        print(e)
        messages.error(request, 'Error saving details')
        return redirect('dashboard')
    

def single(request, agent_id):
    agent = get_object_or_404(Users, pk=agent_id)

    properties = Properties.objects.order_by('-list_date').filter(agent_id=agent.id)

    context = {
        'agent': agent,
        'pcount': len(properties),
        'properties': properties
    }

    return render(request, 'listing/agentsingle.html', context)


def findSingle(request, listing_id):
    property = get_object_or_404(Properties, pk=listing_id)

    context = {
        'property': property
    }

    return render(request, 'listing/property.html', context)