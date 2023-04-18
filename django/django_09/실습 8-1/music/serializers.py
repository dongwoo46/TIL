from rest_framework import serializers
from .models import Music

# MusicSerializer하기위해 serialzers파일과 클래스 만들기
class MusicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Music
        fields = '__all__'