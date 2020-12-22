import unittest, xmlrunner, json, requests
class Tests(unittest.TestCase): pass
with open('tests.json', 'r') as jfile:
    for test_name, test_data in json.load(jfile).items():
        setattr(Tests, test_name, (lambda data: lambda self: self.assertEqual(requests.request(**data['request']).status_code, data['assert']['statusCode']))(test_data))
unittest.main(testRunner=xmlrunner.XMLTestRunner())