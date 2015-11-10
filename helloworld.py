#!/usr/bin/python
import lldb

def helloWorld(debugger, command, result, internal_dict):
	"""Prints 'Hello, World!'"""
	print >>result, "Hello, World!"
	
def __lldb_init_module(debugger, internal_dict):
	debugger.HandleCommand("command script add -f hello.helloWorld hello")
	print 'The "hello" python command has been installed and is ready for use.'