#!/usr/bin/python
import lldb

def superview(debugger, command, result, internal_dict):
    """Prints the superview for a variable name or memeory address."""
    
    ci = debugger.GetCommandInterpreter()
    ro = lldb.SBCommandReturnObject()
    
    command = command.strip()
    
    if len(command) < 1:
        print >>result, "Empty argument. Try 'sv <variable>' or 'sv <memory_address_to_a_UIView>'"
        return
        
    ci.HandleCommand("po [(UIView *){} superview]".format(command), ro)
    output = ro.GetOutput().strip()
    print >>result, output

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand("command script add -f superview.superview sv")
    print 'The "sv" python command has been installed and is ready for use.'