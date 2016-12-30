from django.contrib.auth.models import User

from .base import FunctionalTest


class AdvertsCreationTest(FunctionalTest):

    def _createsuperuser(self):
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

    def _login(self):
        username = 'user'
        password = 'user1234'
        inputbox_login = self.browser.find_element_by_id('id_username')
        inputbox_password = self.browser.find_element_by_id('id_password')
        submit_button = self.browser.find_elements_by_css_selector('input[type="submit"]')[0]

        inputbox_login.send_keys(username)
        inputbox_password.send_keys(password)
        submit_button.click()

    def test_can_create_advert(self):
        ## создание суперпользователя
        self._createsuperuser()

        # переходим на страницу администрирования
        self.browser.get('{site_url}/admin/'.format(site_url=self.live_server_url))
        self._login()
        body_text = self.get_body_text()

        self.assertIn('Администрирование сайта', body_text)

        # находим ссылку 'Объявления' и переходим
        advert_link = self.browser.find_elements_by_link_text('Объявления')[0]
        advert_link.click()

        # список объявлений пост - создаем его
        # ищем кнопку(ссылку) на страницу создания объявления и переходим на нее
        add_advert_link = self.browser.find_element_by_class_name('addlink')
        add_advert_link.click()


        # мы на нужной странице - так как на ней присутствуе текст 'Добавить Объявление'
        # создаем новое объявление и сохраняем его
        self.assertIn('Добавить Объявление', self.get_body_text())

        inputbox_title = self.browser.find_element_by_id('id_title')
        inputbox_text = self.browser.find_element_by_id('id_text')
        save_button = self.browser.find_element_by_name('_save')

        inputbox_title.send_keys('электровеник')
        inputbox_text.send_keys('продаю прекрасный электровеник')
        save_button.click()

        # страница перезагрузилась и в списке объявлений появилась строка 'электровеник'
        self.assertIn('электровеник', self.get_body_text())
