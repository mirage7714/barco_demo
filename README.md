# barco_demo
 This assignment is for barco interview. In this repo, it contains test cases for the requirement, and also the automation cases.  
 At the same time, there are also some issues found during the test. 

 
## Target:  
 The url: https://www.barco.com/en/clickshare/support/warranty-info  
 The purpose is to test the function of searching SN for warranty info  

 
## Test cases:  
 In the test case sheet, it contains the following test cases:   
 - Query for an invalid sn number  
 - Query for a valid sn number  
 - Query but no search result
 - The search log on server side  
 - The error code handling  
 - Operation under mobile web  
 - Switch between different languages  

 
## Issues:  
 During the testing, there are some defect:
 - In mobile web mode, the long sn will be cut on the border  
 - The Explore button will overlap with the sn title when the language is not en  

 
## Test structure:
 The test is using page-object pattern: it contains tests and pages directory:  
 - tests: contains all the test cases  
 - pages: contains the elements and functions of the pages  
 
 Besides the two directories, there's another folder for the test report: 
 - reports: directory for test reports


## Automation test:  
 Steps for executing the automation test:  
 1. Enter the project folder, and install the required packages: `pip install -r requirement.txt`  
 2. Open IDE (I use PyCharm), and execute the `test_warranty.py` for testing  
 3. Or can use cmd tools and execute `pytest --html=reports/report.html` to run tests and create test report after execution  

