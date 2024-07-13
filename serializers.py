from rest_framework import serializers

class EmployeesSerializer(serializers.Serializer):
     name= serializers.CharField( max_length=50)
     email= serializers.EmailField( max_length=254)
     address= serializers.CharField( )
     phone = serializers.IntegerField()