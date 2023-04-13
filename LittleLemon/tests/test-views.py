from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers  import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        item1 = Menu.objects.create(title="Cake", price=90, inventory=90)
        item2 = Menu.objects.create(title="Yoghurt", price=70, inventory=110)

    def test_getall(self):
        response = self.client.get()
        menus = Menu.objects.all()
        serializer = MenuSerializer
        self.assertEqual(response.data, serializer.data) 