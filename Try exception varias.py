# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:18:01 2023

@author: Usuario
"""

#17-04-2023

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")
print("THE END.")

"""
Exception

StopIteration
ArithmeticError
FloatingPointError
OverflowError
ZeroDivisionError
AssertionError
AttributeError
BufferError
EOFError
ImportError
LookupError
IndexError
KeyError
MemoryError
NameError
UnboundLocalError
OSError
BlockingIOError
ChildProcessError
ConnectionError
BrokenPipeError
ConnectionAbortedError
ConnectionRefusedError
ConnectionResetError
FileNotFoundError
InterruptedError
IsADirectoryError
NotADirectoryError
PermissionError
ProcessLookupError
TimeoutError
ReferenceError
RuntimeError
NotImplementedError
SyntaxError
IndentationError
TabError
SystemError
TypeError
ValueError
UnicodeError
UnicodeDecodeError
UnicodeEncodeError
UnicodeTranslateError
Warning
DeprecationWarning
PendingDeprecationWarning
RuntimeWarning
SyntaxWarning
UserWarning
FutureWarning
ImportWarning
UnicodeWarning
BytesWarning
ResourceWarning
EnvironmentError
IOError
VMSError
WindowsError
ZeroDivisionError
SystemExit
KeyboardInterrupt
"""


