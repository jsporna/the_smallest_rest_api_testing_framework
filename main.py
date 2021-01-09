import unittest, xmlrunner, json, requests, glob

def abstract_test(self, data, response):
    self.assertEqual(response.status_code, data['assert']['statusCode'])
    self.assertSetEqual(set(response.json().keys()), set(data['assert']['responseKeys']))
    self.assertLessEqual(response.elapsed.total_seconds(), data['assert']['responseTime'])

test = lambda data: lambda self: abstract_test(self, data, requests.request(**data['request']))
globals().update({file_name: type(file_name, (unittest.TestCase, ), {name: test(data) for name, data in json.load(open(file_name, 'r')).items() }) for file_name in glob.iglob("test_*.json")})
unittest.main(testRunner=xmlrunner.XMLTestRunner())