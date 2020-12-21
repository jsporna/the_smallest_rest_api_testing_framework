import unittest, xmlrunner, json, requests, copy

class Tests(unittest.TestCase): pass

with open('tests.json', 'r') as jfile:
    for test_name, test_data in json.load(jfile).items():
        func = lambda data: lambda self: self.assertEqual(requests.request(**data['request']).status_code, data['assert']['statusCode'])
        setattr(Tests, test_name, func(test_data))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner())