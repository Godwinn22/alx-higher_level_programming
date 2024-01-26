#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        new = fct(*args)
        return new
    except ZeroDivisionError as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
    except IndexError as i:
        sys.stderr.write("Exception: {}\n".format(i))
        return None
    except ValueError as ve:
        sys.stderr.write("Exception: {}\n".format(ve))
        return None
