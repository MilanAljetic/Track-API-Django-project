from pydub import AudioSegment
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from track_app.models import Track

from .serializers import TrackSerializer


class TrackView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
            file_serializer = TrackSerializer(data=request.data)
            if file_serializer.is_valid():
                    file_serializer.save()
                    return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            else:
                    return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CalculateTimeView(APIView):

    def post(self, request, id):
        file = Track.objects.values('id', 'file')
        for data in file:
            if int(id) == data['id']:
                song_file = data['file']
        song_format = song_file[-3:]
        song = AudioSegment.from_file(f"media/{song_file}", format=song_format)
        silent_blocks = 0
        interval = 1
        threshold = -80
        chunks = [song[i:i+interval] for i in range(0, len(song), interval)]
        for c in chunks:
            if c.dBFS == float('-inf') or c.dBFS < threshold:
                silent_blocks += 1
            else:
                break
        rounds = round(silent_blocks * (interval/1000), 3)
        return Response(rounds)
