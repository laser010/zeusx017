#!/usr/bin/python3
# Coded By https://www.instagram.com/laser01/
from os import system
import subprocess

class command():
    """
    Commander class , used to exute cmd (command line)
    cmd= 'the command'
    sudo=False (by defult)
    live=True (by defult) , use to print command directly 
    """
    def __init__(self, cmd=None, sudo=False, live=True):
        self.cmd  = cmd
        self.sudo = sudo
        self.live = live

    def run(self):
        if self.sudo:
            command = ('sudo', self.cmd)
        elif self.sudo == False:
            command = str(self.cmd)
        if self.live == False:
            output = subprocess.run(command,
                                    shell=True,
                                    stdout=subprocess.PIPE,
                                    universal_newlines=True)
            return output.stdout
        elif self.live:
            print(command)
            system(command)