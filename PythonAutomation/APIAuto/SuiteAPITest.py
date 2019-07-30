import unittest

import PythonAutomation
from PythonAutomation.APIAuto.test_get_access_token import TestGetToken
from PythonAutomation.SeleniumAuto.HTML import HTMLStyle


class MyTestSuite(unittest.TestCase):

    def test_cases(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(
                PythonAutomation.APIAuto.test_get_access_token.TestGetToken),
        ])

        outfile = open("TestReport_UI/SeleniumReportUI.html", "w")

        runner1 = HTMLStyle(
            stream=outfile,
            title='UI Test Report',
            description='Selenium Tests'
        )

        runner1.run(smoke_test)


if __name__ == '__main__':
    unittest.main()
