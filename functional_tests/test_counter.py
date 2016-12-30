from adverts.models import Advert

from .base import FunctionalTest


class CounterTest(FunctionalTest):

    def create_test_data(self):
        ## HACK - 1 id использован при запуске предыдушего теста, 
        ## что-бы не учитывать порядок выполнения тестов принудительно назначаем id
        broom = {'title': 'электровеник', 'text': 'прекрасный электровеник', 'id': 1} # веник
        mop = {'title': 'электрошвабра', 'text': 'прекрасная электрошвабра'} # швабра

        create_row = lambda data: Advert.objects.create(**data)
        list(map(create_row, [broom, mop]))


    def test_counter_works_correctly(self):
        ## создаем тестовые данные что-бы было с чем работать
        self.create_test_data()

        # user 1 - Вася
        # Васе посоветовали новый сайт с объявлениями
        # он не долго думая отправился туда
        # Васа понял что папал туда куда надо - в заголовке страницы - 'Доска объявлений'
        self.browser.get('{site_url}'.format(site_url=self.live_server_url))
        self.assertIn('Доска объявлений', self.browser.title)

        # на странице имелось несколько объявлений
        # 1 - 'электровеник', 2 - 'электрошвабра'
        # Васа решил посмотреть объявление с электровениками
        # он кликрул на первую ссылку
        advert_link = self.browser.find_elements_by_link_text('электровеник')[0]
        advert_link.click()

        # когда страница перезагрузилась - Вася увидел текст объявления - 'прекрасный электровеник'
        self.assertIn('прекрасный электровеник', self.get_body_text())
        # Васа нажал кнопку 'назад' и вернулся к списку объявлений
        self.browser.back()

        current_url = self.browser.current_url
        self.assertRegex(current_url, '/')

        # затем Василий перешел по ссылке 'электрошвабра'
        # и лицезрел описание этого объявления
        advert_link = self.browser.find_elements_by_link_text('электрошвабра')[0]
        advert_link.click()

        self.assertIn('прекрасная электрошвабра', self.get_body_text())

        # и снова вернулся на главную страницу
        self.browser.back()
        current_url = self.browser.current_url
        self.assertRegex(current_url, '/')

        # поверхностно посмотрев все объявления Вася вернулся к первому
        advert_link = self.browser.find_elements_by_link_text('электровеник')[0]
        advert_link.click()

        # и снова вернулся на главную страницу
        self.browser.back()

        ## проверяем состояние localStorage
        script = """return get_data();"""
        result = self.browser.execute_script(script)
        self.assertEqual(result, [1, 2])

        ## проверяем что несмотря на то что Вася дважды просмотрел первое объявление
        ## и только один раз второе в поле count каждой записи стоит единица
        self.assertEqual(Advert.objects.get(title='электровеник').counter, 1)
        self.assertEqual(Advert.objects.get(title='электрошвабра').counter, 1)
