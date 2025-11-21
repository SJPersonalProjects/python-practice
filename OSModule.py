"""
30DaysPythonChallenge: OSModule
"""

import os
# Creating a directory.
os.mkdir('sample_directory')
# Changing the current directory.
# os.chdir('path')
# Getting the current working directory.
print(os.getcwd())
# Removing the directory.
os.rmdir('sample_directory')