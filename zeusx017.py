#!/usr/bin/env python3
import sys

url = ("https://www.python.org/downloads/")
version = sys.version_info[0:3]
if version[0] <= 2:
    errMsg = ("""[Incompatible] Your Python version {version}.
To run zeusx017 without problems you have to use Python version 3.6.x .
For install visit {url}""".format(version=version, url=url))
    print(errMsg)
    exit(1)
elif version[0] >= 3:
    from zeusx017.main import main
    if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            print('\nUser aborted!')
            exit(0)
#        except Exception as e:
#            print(e)
#            exit(0)
