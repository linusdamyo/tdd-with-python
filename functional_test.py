from selenium import webdriver
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
        self.fail('Finish the test!')

        # 작업 추가

        # 공작깃털 사기 텍스트 상자에 입력

        # 엔터키를 치면 페이지가 갱신되고 작업목록에
        # 1: 공작깃털 사기 아이템이 추가된다.

        # 추가 아이템을 입력할 여분의 텍스트 상자가 보인다.
        # 다시 공작깃털 이용해서 그물 만들기 입력

        # 페이지가 다시 갱신되고, 두개 아이템이 목록에 보인다.
        # 사이트는 특정 url 을 생성한다.
        # 이때 url에 대한 설명도 함께 제공된다.

        # 해당 url 에 접속하면, 작업 목록이 그대로 나온다.

if __name__ == '__main__':
    unittest.main()
