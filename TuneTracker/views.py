from django.shortcuts import render

# Create your views here.
# TuneTracker/views.py
#from django.shortcuts import render
from .models import Song

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})

def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'song_detail.html', {'song': song})

# TuneTracker/views.py
#from django.shortcuts import render

def playlist_view(request):
    # Add logic to retrieve and pass playlist data to the template
    playlist_data = [...]  # Replace with actual playlist data
    return render(request, 'playlist.html', {'playlist_data': playlist_data})
