from distutils.core import setup, Extension
from sys import platform, version

if platform == "win32":
	threader = Extension('threader',
		sources = ['threaderPy3windows.c'])
elif version[0] == '2':
	threader = Extension('threader',
		sources = ['threader.c'])
elif version[0] == '3':
	threader = Extension('threader',
		sources = ['threaderPy3.c'])

setup (name = 'Threader',
	version = '1.0',
	description = 'External thread killing',
	ext_modules = [threader])