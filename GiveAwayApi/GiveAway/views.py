from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from GiveAway.models import User, Item
from GiveAway.serializers import UserSerializer, ItemSerializer
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def ItemsApi(request, id=0):
    if request.method =='GET':
        items = Item.objects.all()
        items_serializer = ItemSerializer(items,many=True)
        return JsonResponse(items_serializer.data,safe=False)
    elif request.method =='POST':
        item_data = JSONParser().parse(request)
        item_serializer = ItemSerializer(data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        item_data_id = JSONParser().parse(request)
        item_data = Item.objects.get(ItemId=item_data_id['ItemId'])
        item_serializer = ItemSerializer(item_data,data=item_data_id)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Item Not Updated", safe=False)
    elif request.method =='DELETE':
        item_data = Item.objects.get(ItemId=id)
        item_data.delete()
        return JsonResponse("Deleted Successfully", safe=False) 

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)

@csrf_exempt
def Home(request):
    return render(request, 'index.html')


@csrf_exempt
def BrowseFreebie(request):
    if request.method =='GET':
        items = Item.objects.all()
        context = {'items':items}
        #items_serializer = ItemSerializer(items,many=True)
    #return JsonResponse(items_serializer.data,safe=False)
    return render(request, 'browsefreebie.html', context=context)


@csrf_exempt
def PostFreebie(request):
    if request.method == 'GET':
        return render(request, 'postfreebie.html')
    if request.method =='POST':
        files = request.FILES  # multivalued dict
        image = files.get("itemimage")
        #SaveFile(request)
        item_data = Item(
            ItemName=request.POST.get('itemname'),
            ItemImage= image,
            ItemCity= request.POST.get('itemcity'),
            ItemState= request.POST.get('itemstate'),
            ItemLandmark= request.POST.get('itemlandmark'),
            ItemCountry= request.POST.get('itemcountry'),
            ItemDescription=  request.POST.get('itemdescription'),
            ItemRequested= True,
            ItemPincode= request.POST.get('itempincode'),
            UserId= ' '
        )
        user_data = User(
            UserName=request.POST.get('username'),
            UserEmail=request.POST.get('useremail'),
            UserPhoneNo=request.POST.get('userphone'))
        
        item_data.save()
        user_data.save()
    return render(request, 'postfreebie.html')