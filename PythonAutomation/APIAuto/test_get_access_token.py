import unittest, json
from PythonAutomation.APIAuto import data_transaction


class TestGetToken(unittest.TestCase):
    def setUp(self):
        # ========== Customize your userName and Password ==========
        self.userName = ["rex99miller@hotmail.ca", "", "rex999.miller@hotmail.ca", "rex.miller.ca"]
        self.password = ["a123456", "--", "", "a123456"]

        # ========== Connect Server URL ==========
        self.orion_server_path = "127.0.0.1:8000"
        self.url_get_token = self.orion_server_path + "get_access_token"

        # ========== Get Token ==========
        # payload for Token was in data_transaction.py
        # self.token = data_transaction.get_token(self.userName[0], self.password[0], self.url_get_token)
        # UserName is empty: HTTP 400 Bad Request
        # UserName and Password is not match: HTTP 401 Unauthorized
        # UserName is non-email format: HTTP 401 Unauthorized

    def test_00_get_token_valid(self):

        self.token = data_transaction.get_token(self.userName[0], self.password[0], self.url_get_token)

        self.token_dict = json.loads(self.token)
        try:
            self.assertTrue(self.token_dict['access_token'])
            print("Got Token ID: " + self.token_dict['access_token'])
        except AssertionError as e:
            error_note = [(self.userName[0], self.password[0]), str(e)]
            print(error_note)

    def test_01_get_token_empty(self):

        self.token = data_transaction.get_token(self.userName[1], self.password[1], self.url_get_token)
        self.token_dict = json.loads(self.token)
        try:
            self.assertEqual(self.token_dict['error'], "HTTP 400 Bad Request")
        except AssertionError as e:
            error_note = [(self.userName[1], self.password[1]), str(e)]
            print(error_note)

    def test_02_get_token_notMatch(self):

        self.token = data_transaction.get_token(self.userName[2], self.password[2], self.url_get_token)

        self.token_dict = json.loads(self.token)
        try:
            self.assertEqual(self.token_dict['error'], "HTTP 401 Unauthorized")
        except AssertionError as e:
            error_note = [(self.userName[2], self.password[2]), str(e)]
            print(error_note)

    def test_03_get_token_nonEmail_format(self):

        self.token = data_transaction.get_token(self.userName[3], self.password[3], self.url_get_token)

        self.token_dict = json.loads(self.token)
        try:
            self.assertEqual(self.token_dict['error'], "HTTP 401 Unauthorized")
        except AssertionError as e:
            error_note = [(self.userName[3], self.password[3]), str(e)]
            print(error_note)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)



# os.system('py.test ComboAPITest/test_get_access_token.py --html=./TestReport/My_test_report.html')
    # py.test ComboAPITest/test_get_access_token.py --html=./TestReport/My_test_report.html
    # py.test sum.py - -html = name_of_html_file.html

