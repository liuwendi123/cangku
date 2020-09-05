import pytest

from test_framework.demo_page import DemoPage
from test_framework.utils import Utils


class TestLogin:
	data = Utils.from_file('test_search.yaml')

	def setup_class(self):
		self.demo = DemoPage()
		self.demo.start()

	def setup(self):
		pass

	def teardown(self):
		self.demo.back()


	def teardown_class(self):
		self.demo.stop()

	#todo:有测试数据的的驱动
	@pytest.mark.parametrize('username,password',
	                         (["user1", 'password1'],
	                          ["user2", 'password2']))
	def test_login(self, username, password):
		# todo:测试步骤的数据驱动
		self.demo.login(username, password)
		assert 1 == 1

	# @pytest.mark.parametrize('keyword',[
	# 	'alibaba',
	# 	#'jd',
	# 	#'baidu'
	# ])
	@pytest.mark.parametrize(data['keys'], data['values'])
	def test_search(self, keyword):
		self.demo.search(keyword)