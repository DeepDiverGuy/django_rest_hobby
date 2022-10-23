from django.contrib import auth
from rest_framework import serializers
from person.models import Person




User = auth.get_user_model()



class PersonSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Person
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):

    person_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Person.objects.all()) # Notice: if you don't use '_set' at the end, then it's gonna through an error. The documentation is misleading on this one.

    class Meta:
        model = User
        fields = '__all__'
