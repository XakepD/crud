from rest_framework import serializers
from .models import *

class NameSerializer(serializers.ModelSerializer):
      class Meta:
            model = Person
            fields = ["name"]