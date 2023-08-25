
from collections import namedtuple

"""
Test the Task data type
"""


Task = namedtuple("Task", ["summary", "owner", "done", "id"])
Task.__new__.__defaults__ = (None, None, False, None)

print(Task._fields)
