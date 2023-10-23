#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        sys.stderr.write('Exception: '+ e.args[0] + '\n')
        return None
