from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pickle
from django.http import JsonResponse

CLIENT_ID = "70a9fb89662f4dac8d07321b259eaad7"
CLIENT_SECRET = "4d6710460d764fbbb8d8753dc094d131"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

music = pickle.load(open('./static/df.pkl','rb'))
similarity = pickle.load(open('./static/similarity.pkl','rb'))

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommended_music_names.append(music.iloc[i[0]].song)

    return recommended_music_names,recommended_music_posters

def recommend_view(request):
    song = request.GET.get('song')
    if song:
        recommended_music_names, recommended_music_posters = recommend(song)
        recommendations = [
            {'name': name, 'poster': poster}
            for name, poster in zip(recommended_music_names, recommended_music_posters)
        ]
        return JsonResponse({'recommendations': recommendations})
    else:
        return JsonResponse({'error': 'No song provided'}, status=400)

# Create your views here.
def home(request):
    return render(request, 'index.html')

def explore(request):
    music_list = music['song'].values
    context = {'songs': music_list}
    return render(request, 'explore.html', context)

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def faqs(request):
    return render(request, 'faqs.html')

