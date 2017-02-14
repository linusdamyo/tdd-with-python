from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 웹사이트 접근
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀 헤더 To-Do 
        #assert 'To-Do' in browser.title, "Browser title was " + browser.title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 작업 추가
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
        )

        # 공작깃털 사기 텍스트 상자에 입력
        inputbox.send_keys('공작깃털 사기')

        # 엔터키를 치면 페이지가 갱신되고 작업목록에
        # 1: 공작깃털 사기 아이템이 추가된다.
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: 공작깃털 사기' for row in rows),
            "신규 작업이 테이블에 표시되지 않는다"
        )

        # 추가 아이템을 입력할 여분의 텍스트 상자가 보인다.
        # 다시 공작깃털 이용해서 그물 만들기 입력
        self.fail('Finish the test!')

        # 페이지가 다시 갱신되고, 두개 아이템이 목록에 보인다.
        # 사이트는 특정 url 을 생성한다.
        # 이때 url에 대한 설명도 함께 제공된다.

        # 해당 url 에 접속하면, 작업 목록이 그대로 나온다.

if __name__ == '__main__':
    unittest.main()
