import unittest, xmlrunner, json, requests

with open('tests.json', 'r') as jfile:
    class Tests(unittest.TestCase): pass
    for test_name, test_data in json.load(jfile).items(): setattr(Tests, test_name, (lambda data: lambda self: self.assertEqual(requests.request(**data['request']).status_code, data['assert']['statusCode']))(test_data))

unittest.main(testRunner=xmlrunner.XMLTestRunner())