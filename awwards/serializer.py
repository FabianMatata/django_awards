from rest_framework import serializers
from .models import Profile,project,Rating

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('bio','email','profile_pic','user')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=project
        fields=('webimage','name','description','link','profile','no_of_ratings')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        models=Rating
        fields = ('id','design','content','usability','user','project')
