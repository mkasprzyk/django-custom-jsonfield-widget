from django.test import TestCase
from custom_widget.models import ReactorModel

class ReactorModelTest(TestCase):
    def setUp(self):
        self.model = ReactorModel.objects.create(
            name="Testing"
        )

    def test_(self):
        print(self.model)