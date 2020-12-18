import unittest, xmlrunner, json, requests

class Tests(unittest.TestCase): pass

with open('tests.json', 'r') as jfile:
    for test_name, test_data in json.load(jfile).items():
        setattr(Tests, test_name, lambda self: self.assertEqual(requests.request(**test_data['request']).status_code, test_data['assert']['statusCode']))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner())