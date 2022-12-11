from rest_framework import serializers
from GiveAway.models import User, Item

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('UserId','UserName','UserEmail', 'UserPhoneNo', 'UserAddress')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields=('ItemId','ItemName', 'ItemImage','ItemCity','ItemState','ItemLandmark','ItemCountry','ItemPincode','ItemDescription','ItemRequested','UserId')