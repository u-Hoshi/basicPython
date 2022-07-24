from rest_framework.serializers import ModelSerializer
from .models import CustomerUser


class UserSerializer(ModelSerializer):
  class Meta:
    model = CustomerUser
    fields =[
      "userId",
      "username",
      "email",
      "password"
    ]

  def create(self,validated_data):
    user = CustomerUser.objects.create_user(
      validated_data["username"],
      validated_data["email"],
      validated_data["password"]
    )
    
    return user