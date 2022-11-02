# Exam 1

## Rules of Behavior
1. Do not communicate with anyone during the exam (no email, no social media, no texting, no phones, no talking, no passing notes, no internet communicating).  If there is any evidence of communicating with anyone during the exam you will receive a zero.
1. You **must** turn off your cell phone and store it away.
1. Your submission **must** be solely you own work without the assistance of anyone by any means.
1. All programming code **must** be written in Python.
1. All your code **must** be pushed to Github by ** 9:45 AM today**.  Any submissions after that time will not be considered.
1. You may use your book.
1. You may use the Internet as a **reference only**.
1. If you have questions, raise your hand.

     
## Program Instructions
1. Your are given a main.py file which defines a dictionary of grades.  The data structure of the grades is as follows:
     ```
	grades dictionary:
		key: student id as an integer
		value : student dictionary

	student dictionary:
		for key: 'name'
		value : student name as a string

		for key: 'homework'
		value : list of homework grades for each assignment as an integer

		for key: 'laboratory'
		value : list of laboratory grades for each assignment as an integer
     ```
	The exact data used in the main.py file is as follows:
     ```
	{ 70314: { 'name': 'Anna Kendrick', 
		        'homework': [77, 83, 100], 
		        'laboratory': [85, 78] }, 

	  90919: { 'name': 'Rebel Wilson', 
		       'homework': [51, 60, 96], 
		       'laboratory': [92, 87] }, 

	  72457: { 'name': 'Brittany Snow', 
		       'homework': [97, 81, 73], 
		       'laboratory': [67, 100] }, 

	  55331: { 'name': 'Hailee Steinfeld', 	
		       'homework': [63, 67, 62], 
		       'laboratory': [100, 98] }, 

	  52392: { 'name': 'Hana Mae Lee', 
		       'homework': [95, 100, 73], 
		       'laboratory': [97, 74] }, 

	  65087: { 'name': 'Skylar Astin', 
		       'homework': [61, 89, 87], 
		       'laboratory': [100, 97] }, 

	  91523: { 'name': 'Adam DeVine', 
		       'homework': [99, 94, 89], 
		       'laboratory': [69, 91] }
	}
     ```
	While this data is given in the main.py file, your package should accept any data that meets the above dictionary data structure.  The main.py file also prints a report of a classroom grade book. The report not only contains all the grades from the grade book, it also contains several calculations to show averages and weighted averages.  Your package will calculate all the averages needed for the report.  The main.py file has many variables set to zero and named using the reference letters in the below package specification.  You can edit these variable expressions as you build your modules/functions and use the example output to verify your calculations are correct. 
1. Write a Python package with modules and functions using keyword arguments.  Use the following directory outline and module names (your first starting point should be a directory called `gradebook` within your `exam01-username` directory):
     ```
	gradebook/
		__init__.py
		student.py
		classroom.py
     ```
     
1. Create a `gradebook` package.
     1. Initialize the `__all__` variable to the `student` and `classroom` modules.
     1. Create a `student` module.
          1. Create a function named `homework_average` which receives the keyword parameters `grades` and `student_id`.  The function should return a 0 if the student_id is not in the grades dictionary, otherwise it should return the average of all the homework assignments for the given student_id. Reference `<x>` in the below example output.
          1. Create a function named `laboratory_average` which receives the keyword parameters `grades` and `student_id`.  The function should return a 0 if the student_id is not in the grades dictionary, otherwise it should return the average of all the laboratory assignments for the given student_id. Reference `<y>` in the below example output.
          1. Create a function named `total_weighted_average` which receives the keyword parameters `grades` and `student_id`.  The function should return a 0 if the student_id is not in the grades dictionary, otherwise it should return the total weighted average of all the assignments for the given student_id, where homework assignments are worth 25% and laboratory assignments are worth 75%. Reference `<z>` in the below example output.
     1. Create a `classroom` module.
          1. Create a function named `homework_average` which receives the keyword parameters `grades` and `assignment_no`.  The function should return a 0 if the assignment_no is out of range, otherwise it should return the classroom average of all student homework assignments for the given assignment_no. Reference `<a1>`, `<a2>`, and `<a3>` in the below example output.
          1. Create a function named `homework_average_average` which receives the keyword parameter `grades`.  The function should return the classroom average of all student homework assignments. Reference `<b>` in the below example output.
          1. Create a function named `laboratory_average` which receives the keyword parameters `grades` and `assignment_no`.  The function should return a 0 if the assignment_no is out of range, otherwise it should return the classroom average of all student laboratory assignments for the given assignment_no. Reference `<c1>` and `<c2>` in the below example output.
          1. Create a function named `laboratory_average_average` which receives the keyword parameter `grades`.  The function should return the classroom average of all student laboratory assignments. Reference `<d>` in the below example output.
          1. Create a function named `total_weighted_average_average` which receives the keyword parameter `grades`.  The function should return the classroom total weighted average of all student assignments. Reference `<e>` in the below example output.
1. Example output using the references above:

    ```
	                                                                              Total
				 |-------HOMEWORK-------|    |---LABORATORY---|    Weighted
	Name              ID        H1    H2    H3   Havg       L1    L2   Lavg     Average
	================= =====  ===== ===== =====  =====    ===== =====  =====    ========
	Anna Kendrick     70314     77    83   100    <x>       85    78    <y>         <z>
	Rebel Wilson      90919     51    60    96    <x>       92    87    <y>         <z>
	Brittany Snow     72457     97    81    73    <x>       67   100    <y>         <z>
	Hailee Steinfeld  55331     63    67    62    <x>      100    98    <y>         <z>
	Hana Mae Lee      52392     95   100    73    <x>       97    74    <y>         <z>
	Skylar Astin      65087     61    89    87    <x>      100    97    <y>         <z>
	Adam DeVine       91523     99    94    89    <x>       69    91    <y>         <z>
				 ===== ===== =====  =====    ===== =====  =====    ========
	     Classroom Averages:  <a1>  <a2>  <a3>    <b>     <c1>  <c2>    <d>         <e>
    ```
1. Example output using the grades dictionary defined in the main.py file:

    ```
	                                                                              Total
				 |-------HOMEWORK-------|    |---LABORATORY---|    Weighted
	Name              ID        H1    H2    H3   Havg       L1    L2   Lavg     Average
	================= =====  ===== ===== =====  =====    ===== =====  =====    ========
	Anna Kendrick     70314     77    83   100   86.7       85    78   81.5        82.8
	Rebel Wilson      90919     51    60    96   69.0       92    87   89.5        84.4
	Brittany Snow     72457     97    81    73   83.7       67   100   83.5        83.5
	Hailee Steinfeld  55331     63    67    62   64.0      100    98   99.0        90.2
	Hana Mae Lee      52392     95   100    73   89.3       97    74   85.5        86.5
	Skylar Astin      65087     61    89    87   79.0      100    97   98.5        93.6
	Adam DeVine       91523     99    94    89   94.0       69    91   80.0        83.5
				 ===== ===== =====  =====    ===== =====  =====    ========
	     Classroom Averages:  77.6  82.0  82.9   80.8     87.1  89.3   88.2        86.4
    ```

     
5. Edit and run the main.py file to test all the modules and functions using the command below and repeat the steps above until you are satisfied your program output meets the above requirements. I will not grade this file - it is for your use to test the package.

    ```
    python3 -m main
    ```

1. Run the unit testing program to ensure that your program runs as expected.

    ```
    python3 -m test
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run ` python3 -m test` repeatedly until it passes all the test.

## Submission
Periodically throughout the exercise, and when you have completed the exercise, make zip folder of the which contains all file and that should contain "test.txt."

    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|10|gradebook package defined and meets the program requirements|
|10|student module defined and meets the program requirements|
|10|classroom module defined and meets the program requirements|
|10|unit testing test.txt file results submitted|
|10|unit testing passes each test|
