import unittest

import PythonAutomation
from PythonAutomation.SeleniumAuto.login_20_ui import TestLoginOrion
from PythonAutomation.SeleniumAuto.NBAI_Pro_upload_ui import OrionProUploadUI
from PythonAutomation.SeleniumAuto.HTML import HTMLStyle


class MyTestSuite(unittest.TestCase):

    def test_cases(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(
                PythonAutomation.SeleniumAuto.NBAI_Pro_upload_ui.OrionProUploadUI),
            unittest.defaultTestLoader.loadTestsFromTestCase(PythonAutomation.SeleniumAuto.login_20_ui.TestLoginOrion),
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
