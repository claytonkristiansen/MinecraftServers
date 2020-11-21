
VERSION_NUMBER = (0, 0, 0)
VERSION_INT = 0
VERSION_STAGE = "DEV"
VERSION_STRING = f"{'.'.join((str(n) for n in VERSION_NUMBER))}-{VERSION_STAGE}"

if __debug__:
    VERSION_STRING += "-source"
