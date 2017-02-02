from django.test import TestCase
from django.contrib.auth.models import User

from .models import Advert


class CreateSuperUserTest(TestCase):

    def test_can_create_super_user(self):
        data = {
            'username': 'user',
            'email': 'user@gmail.com',
            'is_staff': True,
            'is_active': True,
            'is_superuser': True,
        }
        password = 'user1234'
        user = User(**data)
        user.set_password(password)
        user.save()

        self.assertEqual(User.objects.count(), 1)


class HomePageTest(TestCase):

    def test_home_page_render_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'adverts/home.jade')

    def test_passes_correct_adverts_to_template(self):
        Advert.objects.create(title='1', text='объявление 1')
        Advert.objects.create(title='2', text='объявление 1')

        response = self.client.get('/')

        self.assertEqual(list(response.context['adverts']),
                         list(Advert.objects.all()))


class DetailViewTest(TestCase):

    def test_detail_page_render_detail_template(self):
        Advert.objects.create(title='веник', text='просто веник')
        response = self.client.get('/1/')
        self.assertTemplateUsed(response, 'adverts/detail.jade')

    def test_passes_correct_data_to_template(self):
        Advert.objects.create(title='веник', text='просто веник')
        response = self.client.get('/1/')
        self.assertEqual(response.context['data'], Advert.objects.get(id=1))

    def test_query_string_processing(self):
        advert = Advert.objects.create(title='веник', text='просто веник')

        self.client.get('/1/?v=0')
        advert = Advert.objects.get(id=1)
        self.assertEqual(advert.counter, 1)

        self.client.get('/1/?v=0')
        advert = Advert.objects.get(id=1)
        self.assertEqual(advert.counter, 2)

        self.client.get('/1/?v=1')
        advert = Advert.objects.get(id=1)
        self.assertEqual(advert.counter, 2)


class AdvertModelTest(TestCase):
    def test_counter_default_value(self):
        item = Advert.objects.create(title='веник', text='просто веник')
        self.assertEqual(item.counter, 0)


class BadMath(TestCase):

    def test_bad_add(self):
        self.assertEqual(2 + 2, 4)

#     def test_bad_mul(self):
#         self.assertEqual(2*2, 3)

#     def test_bad_mul2(self):
#         self.assertEqual(2*2, 3)

#
#
#
#
#
#
