#!/usr/bin/python3
"""Write a class Student
   that defines a student by:
"""


class Student():
    """Write a class Student
       that defines a student by (based on 9-student.py):
    """

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Write a class Student
           that defines a student by (based on 9-student.py):
        """

        if attrs is None:
            return(self.__dict__)
        new = {}
        for i in attrs:
            try:
                new[i] = self.__dict__[i]
            except:
                pass
        return(new)
