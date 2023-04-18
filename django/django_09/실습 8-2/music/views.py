from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Music
from .serializers import MusicSerializer, MusicListSerializer

# Create your views here.
@api_view(['GET','POST'])
def music_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        musics = get_list_or_404(Music)
        serializer = MusicListSerializer(musics, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicListSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE','PUT'])
def music_detail(request, music_pk):
    # article = Article.objects.get(pk=article_pk)
    music = get_object_or_404(Music, pk= music_pk)
    if request.method =='GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        music.delete()
        data = {
            'delete':f'음악 {music_pk}가 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    elif request.method =='PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
