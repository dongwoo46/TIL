from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Music
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MusicSerializer

# Create your views here.
def music_html(request):
    musics = Music.objects.all()
    context = {
        "musics": musics,
    }
    return render(request, "music/music.html", context)

# json형태로 id,title,content를 다 입력해서 musics_json을 만들기
def music_json_1(request):
    musics = Music.objects.all()
    musics_json = []

    for music in musics:
        musics_json.append(
            {
                "id": music.pk,
                "title": music.title,
                "content": music.content,
            }
        )
    return JsonResponse(musics_json, safe=False)

# 데이터를 직렬화 하여 저장하고 딕셔너리형태로 json으로 들어가고 어떤 값이 들어갈지 저장
def music_json_2(request):
    musics = Music.objects.all()
    data = serializers.serialize(
        "json",
        musics,
        fields=(
            "title",
            "content",
        ),
    )
    return HttpResponse(data, content_type="application/json")

# serializer를 이용하여 MusicSerializer를 만들어서 더미 데이터를 만들어줌 rest_framework를 사용!
@api_view(['GET'])
def music_json_3(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)
    
