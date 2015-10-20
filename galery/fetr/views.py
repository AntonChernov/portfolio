from django.shortcuts import render_to_response

from fetr.models import Album, Image

def all_alb(request):
    return (render_to_response('index.html', {'albums':Album.objects.all()}))

def det_imag(request, id):
    return (render_to_response('detail.html', {'images':Image.objects.filter(album_id=id)}))

# Create your views here.
