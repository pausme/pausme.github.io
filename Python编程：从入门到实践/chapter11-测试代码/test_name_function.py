import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    # 所有以test_打头的方法都将自动运行
    def test_first_last_name(self):
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")


# 如果此文件作为主程序执行时，变量__name__将被设置为'__main__'
if __name__ == '__main__':
    unittest.main()
