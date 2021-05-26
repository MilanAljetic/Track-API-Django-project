from django.test import TestCase

from track_app.models import Track


class TestTrackModel(TestCase):

    def setUp(self):
        self.data1 = Track.objects.create(file='musics/moonwalk.mp3', artist='Michael Jackson', title='Moonwalk')

    def test_track_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Track))

    def test_track_model_name(self):
        data = self.data1
        self.assertEqual(str(data), 'Moonwalk')
