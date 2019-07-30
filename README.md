# AutomationTesting
Python&Java

# CICD 
Gitlab
Jenkins
Azure

# Python code
Tools:
Unittest
Selenium
Pytest
Html for report
xger

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


![alt text](https://github.com/leoli2019/AutomationTesting/blob/master/PythonAutomation/SeleniumAuto/testReport.JPG)

# Java code
Tools:
Jmeter
TestNG
JUnit
