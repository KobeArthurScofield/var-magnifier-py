# VaLueMagNifier
# This library is used for monitoring values in your Python script when you need to observe it.

print("You have lodaded VLMN VaLueMagNifier inside your Python scripts. If you don't want to see this notice, please remove the import and any codes that use VLMN from your script.")

print("It is strongly recommended to remove VLMN from scripts for release.")

print("Initializing VLMN functions...")


from .varmagnifier import *

__all__ = [
    "ConLogVar",
    "ConLogMsg",
    "FilLogVar",
    "FilLogMsg",
]

ConLogMsg("VLMN functions has been loaded.")
