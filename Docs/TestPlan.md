# **SSN Validator – Test Plan**
- **Prepared by**: Deivy Jr. Peña Rodríguez.
- **Date**: 5/17/2022.
## **Introduction**
Test Plan document is for tracking information requited to define, in an effective way, the approach to be used in the testing of this project. 

Specifically in this case, test plan in thought for organize the concepts of the functionality testing and how they are going to be implemented. This document is created during the planning phase of the project.
## **Objectives and tracks**:
### **Objectives**
* Remark and detail every single possible case to test in this project.
* Understand every single unit of the code implemented and test it in an effective and foolproof way.
* Divide the program by the main functionalities to test every single main functionality exhaustively and carefully to reduce possible errors or bugs in the future.
* Know and understand the importance of testing in the context of software engineering.
* Avoid human errors or selfish attitudes during the testing process.
### **Tasks**
* Make a list the test cases.
* Do testing in a cycle way, something like PDD we’ve seen before.
* Report every single step during the testing process. Those are: what was the function we were testing, what was the expected result and its differences (if exist) to the real results. And a conclusion to understand better what was the reason of the error.
## **Testing strategy**:
The strategy we are supposed to implement to this SSN validator is based on unit testing, specifically, with the program functions test in different scenarios. 

As you can imagine, the test structure defined by the author of this document (and every single document you find in this repository) is:
* **Scenario** title: Is the test case we are doing in fact.
Function that is testing: Function of the code that is testing.
Expectations from the test: What does the tester think is going to happen.
* **Expected result**: What is expected by the tester.
* **Real result**: How really result the test.
* **Conclusion**: What was the changes (if there were) and how did he fix the possible problem.
## **Methodology of unit testing**.
For the SSN validator, automated unit test is used to develop the functional tests. Consequently, the framework selected is pytest, obviously, programming language used for this program is python. 

The following flow is used for every single unit test in this program: 
1. Test case is selected.
2. Inputs and expected results are parametrized. 
3. Tests execute, and the result is what’s going to be documented in another Docs (see the end of this document to go).

## **List of testing that are going to be implemented**
1. Check if the program validates the range of the first part in the SSN.
2. Validate if the program validates the range of the second part in SSN.
3. Verify if the program validates the range of the third part in SSN.
4. Check if the program validates the format in SSN (divided by hyphen).
5. Confirm if the program support incorrect inputs (random strings, special characters, etc.).

> To see the results of these tests, click [here](/Docs/TestsResults.md)
