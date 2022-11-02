import unittest
import io
import sys
from unittest.mock import patch
from gradebook import *

g = {11111: {'name': 'Student 1', 'homework': [60, 80], 'laboratory': [80, 100]}, 22222: {'name': 'Student 2', 'homework': [65, 85], 'laboratory': [65, 85]}, 33333: {'name': 'Student 3', 'homework': [95, 75], 'laboratory': [100, 70]}}

class Test01_student_homework_average(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 **** GIVEN: g = {11111: {'name': 'Student 1', 'homework': [60, 80], 'laboratory': [80, 100]}, 22222: {'name': 'Student 2', 'homework': [65, 85], 'laboratory': [65, 85]}, 33333: {'name': 'Student 3', 'homework': [95, 75], 'laboratory': [100, 70]}} *** FUNCTION CALL: student.homework_average(grades=g,student_id=22222) *** EXPECT: 75.0 ***
        """
        self.assertEqual(75.0, student.homework_average(grades=g,student_id=22222))
        print()

class Test02_student_homework_average(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 **** GIVEN: g = {11111: {'name': 'Student 1', 'homework': [60, 80], 'laboratory': [80, 100]}, 22222: {'name': 'Student 2', 'homework': [65, 85], 'laboratory': [65, 85]}, 33333: {'name': 'Student 3', 'homework': [95, 75], 'laboratory': [100, 70]}} *** FUNCTION CALL: student.homework_average(grades=g,student_id=00000) *** EXPECT: 0 ***
        """
        self.assertEqual(0, student.homework_average(grades=g,student_id=00000))
        print()

class Test03_student_laboratory_average(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 **** GIVEN: g = {11111: {'name': 'Student 1', 'homework': [60, 80], 'laboratory': [80, 100]}, 22222: {'name': 'Student 2', 'homework': [65, 85], 'laboratory': [65, 85]}, 33333: {'name': 'Student 3', 'homework': [95, 75], 'laboratory': [100, 70]}} *** FUNCTION CALL: student.laboratory_average(grades=g,student_id=33333) *** EXPECT: 85.0 ***
        """
        self.assertEqual(85.0, student.laboratory_average(grades=g,student_id=33333))
        print()

class Test04_student_laboratory_average(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 **** GIVEN: g = {11111: {'name': 'Student 1', 'homework': [60, 80], 'laboratory': [80, 100]}, 22222: {'name': 'Student 2', 'homework': [65, 85], 'laboratory': [65, 85]}, 33333: {'name': 'Student 3', 'homework': [95, 75], 'laboratory': [100, 70]}} *** FUNCTION CALL: student.laboratory_average(grades=g,student_id=00000) *** EXPECT: 0 ***
        """
        self.assertEqual(0, student.laboratory_average(grades=g,student_id=00000))
        print()

class Test05_student_total_weighted_average(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test05 **** GIVEN: g = {11111: {'name': 'Student 1', 'homework': [60, 80], 'laboratory': [80, 100]}, 22222: {'name': 'Student 2', 'homework': [65, 85], 'laboratory': [65, 85]}, 33333: {'name': 'Student 3', 'homework': [95, 75], 'laboratory': [100, 70]}} *** FUNCTION CALL: student.total_weighted_average(grades=g,student_id=11111) *** EXPECT: 85.0 ***
        """
        self.assertEqual(85.0, student.total_weighted_average(grades=g,student_id=11111))
        print()

class Test06_student_total_weighted_average(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test06 **** GIVEN: g = {11111: {'name': 'Student 1', 'homework': [60, 80], 'laboratory': [80, 100]}, 22222: {'name': 'Student 2', 'homework': [65, 85], 'laboratory': [65, 85]}, 33333: {'name': 'Student 3', 'homework': [95, 75], 'laboratory': [100, 70]}} *** FUNCTION CALL: student.total_weighted_average(grades=g,student_id=00000) *** EXPECT: 0 ***
        """
        self.assertEqual(0, student.total_weighted_average(grades=g,student_id=00000))
        print()

class Test07__classroom_homework_average(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test07 **** GIVEN: g = {11111: {'name': 'Student 1', 'homework': [60, 80], 'laboratory': [80, 100]}, 22222: {'name': 'Student 2', 'homework': [65, 85], 'laboratory': [65, 85]}, 33333: {'name': 'Student 3', 'homework': [95, 75], 'laboratory': [100, 70]}} *** FUNCTION CALL: classroom.homework_average(grades=g,assignment_no=0) *** EXPECT: 73.3 ***
        """
        self.assertEqual(73.3, round(classroom.homework_average(grades=g,assignment_no=0),1))
        print()

class Test08__classroom_homework_average(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test08 **** GIVEN: g = {11111: {'name': 'Student 1', 'homework': [60, 80], 'laboratory': [80, 100]}, 22222: {'name': 'Student 2', 'homework': [65, 85], 'laboratory': [65, 85]}, 33333: {'name': 'Student 3', 'homework': [95, 75], 'laboratory': [100, 70]}} *** FUNCTION CALL: classroom.homework_average(grades=g,assignment_no=5) *** EXPECT: 0 ***
        """
        self.assertEqual(0, round(classroom.homework_average(grades=g,assignment_no=5),1))
        print()

class Test09__classroom_homework_average_average(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test09 **** GIVEN: g = {11111: {'name': 'Student 1', 'homework': [60, 80], 'laboratory': [80, 100]}, 22222: {'name': 'Student 2', 'homework': [65, 85], 'laboratory': [65, 85]}, 33333: {'name': 'Student 3', 'homework': [95, 75], 'laboratory': [100, 70]}} *** FUNCTION CALL: classroom.homework_average_average(grades=g) *** EXPECT: 76.7 ***
        """
        self.assertEqual(76.7, round(classroom.homework_average_average(grades=g),1))
        print()

class Test10__classroom_laboratory_average(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test10 **** GIVEN: g = {11111: {'name': 'Student 1', 'homework': [60, 80], 'laboratory': [80, 100]}, 22222: {'name': 'Student 2', 'homework': [65, 85], 'laboratory': [65, 85]}, 33333: {'name': 'Student 3', 'homework': [95, 75], 'laboratory': [100, 70]}} *** FUNCTION CALL: classroom.laboratory_average(grades=g,assignment_no=1) *** EXPECT: 85.0 ***
        """
        self.assertEqual(85.0, round(classroom.laboratory_average(grades=g,assignment_no=1),1))
        print()

class Test11__classroom_laboratory_average(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test11 **** GIVEN: g = {11111: {'name': 'Student 1', 'homework': [60, 80], 'laboratory': [80, 100]}, 22222: {'name': 'Student 2', 'homework': [65, 85], 'laboratory': [65, 85]}, 33333: {'name': 'Student 3', 'homework': [95, 75], 'laboratory': [100, 70]}} *** FUNCTION CALL: classroom.laboratory_average(grades=g,assignment_no=5) *** EXPECT: 0 ***
        """
        self.assertEqual(0, round(classroom.laboratory_average(grades=g,assignment_no=5),1))
        print()

class Test12__classroom_laboratory_average_average(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test12 **** GIVEN: g = {11111: {'name': 'Student 1', 'homework': [60, 80], 'laboratory': [80, 100]}, 22222: {'name': 'Student 2', 'homework': [65, 85], 'laboratory': [65, 85]}, 33333: {'name': 'Student 3', 'homework': [95, 75], 'laboratory': [100, 70]}} *** FUNCTION CALL: classroom.laboratory_average_average(grades=g) *** EXPECT: 83.3 ***
        """
        self.assertEqual(83.3, round(classroom.laboratory_average_average(grades=g),1))
        print()

class Test13__classroom_total_weighted_average_average(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test13 **** GIVEN: g = {11111: {'name': 'Student 1', 'homework': [60, 80], 'laboratory': [80, 100]}, 22222: {'name': 'Student 2', 'homework': [65, 85], 'laboratory': [65, 85]}, 33333: {'name': 'Student 3', 'homework': [95, 75], 'laboratory': [100, 70]}} *** FUNCTION CALL: classroom.total_weighted_average_average(grades=g) *** EXPECT: 81.7 ***
        """
        self.assertEqual(81.7, round(classroom.total_weighted_average_average(grades=g),1))
        print()


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
