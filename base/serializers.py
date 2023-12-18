from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *

class UserSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    sleeper_id = serializers.SerializerMethodField(read_only=True)
    sleeper_team_name = serializers.SerializerMethodField(read_only=True)
    sleeper_display_name = serializers.SerializerMethodField(read_only=True)
    sleeper_avatar = serializers.SerializerMethodField(read_only=True)
    sleeper_league_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        # fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff
    def get_sleeper_id(self, obj):
        if hasattr(obj, 'userprofile'):
            return obj.userprofile.sleeper_id
    def get_sleeper_display_name(self, obj):
        if hasattr(obj, 'userprofile'):
            return obj.userprofile.sleeper_display_name
        return None
    def get_sleeper_team_name(self, obj):
        if hasattr(obj, 'userprofile'):
            return obj.userprofile.sleeper_team_name
        return None
    def get_sleeper_avatar(self, obj):
        if hasattr(obj, 'userprofile'):
            return obj.userprofile.sleeper_avatar
        return None
    def get_sleeper_league_id(self, obj):
        if hasattr(obj, 'userprofile'):
            return obj.userprofile.sleeper_league_id
        return None


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        # fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)



class NFLPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFLPlayers
        fields = [
            'first_name', 'last_name', 'search_first_name', 'search_last_name',
            'team', 'fantasy_positions', 'stats_id', 'yahoo_id', 'player_id',
            'espn_id', 'oddsjam_id', 'gsis_id', 'sportradar_id', 'rotowire_id',
            'rotoworld_id', 'pandascore_id', 'fantasy_data_id'
        ]

    # If you need to handle the JSON fields specifically
    fantasy_positions = serializers.JSONField()




# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'


# class ProductSerializer(serializers.ModelSerializer):
#     reviews = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = Product
#         fields = '__all__'

#     def get_reviews(self, obj):
#         reviews = obj.review_set.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return serializer.data


# class ShippingAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShippingAddress
#         fields = '__all__'


# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = '__all__'


# class OrderSerializer(serializers.ModelSerializer):
#     orderItems = serializers.SerializerMethodField(read_only=True)
#     shippingAddress = serializers.SerializerMethodField(read_only=True)
#     user = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = Order
#         fields = '__all__'

#     def get_orderItems(self, obj):
#         items = obj.orderitem_set.all()
#         serializer = OrderItemSerializer(items, many=True)
#         return serializer.data

#     def get_shippingAddress(self, obj):
#         try:
#             address = ShippingAddressSerializer(
#                 obj.shippingaddress, many=False).data
#         except:
#             address = False
#         return address

#     def get_user(self, obj):
#         user = obj.user
#         serializer = UserSerializer(user, many=False)
#         return serializer.data
