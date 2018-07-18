#!/usr/bin/python3
# Coded By https://www.instagram.com/laser01/

from libs.commander import command
import csv
import os

class SaveOutput():
    """Save output in file"""
    def __init__(self, file, output):
        self.file   = file
        self.output = output
    def save(self):
        output = open(self.file, 'w')
        output.write(self.output)
        output.close()

class metasploit():
    """docstring for metasploit"""
    def __init__(self, ip=None, output=None):
        self.ip = ip
        self.output = output

    def nmap(self):
        c = ("db_nmap -v -T4 -sV -PA --version-all --osscan-guess -sC -sS {ip}".format(
            ip=self.ip
            )
        )
        c += ("\nservices --rhosts {ip} -o {output}/nmap.csv".format(
            ip=self.ip, output=self.output
            )
        )
        c += ("\nexit")
        cfile = ('{output}/nmap.c'.format(output=self.output))
        SaveOutput(file=cfile, output=c).save()
        command('msfconsole -r {cfile}'.format(cfile=cfile)).run()

    def searchSploit(self, ports=None):
        c = ''
        for port in ports:
            prt = ports[port]['port']
            name = ports[port]['name']
            info = ports[port]['info']
            c += ('\nsearch type:exploit name:{name} {info} -o {output}/{port}.csv'.format(
                name=name, info=info, output=self.output, port=prt
                )
            )
        c += ('\nexit')
        cfile = ('{output}/ports.c'.format(output=self.output))
        SaveOutput(file=cfile, output=c).save()
        command('msfconsole -r {cfile}'.format(cfile=cfile)).run()
        lst = os.listdir('{output}'.format(output=self.output))
        for file in lst:
            for port in ports:
                prt = ports[port]['port']
                if file.startswith(prt):
                    file = self.output+'/{file}'.format(file=file)
                    with open(file, newline='') as csvfile:
                        reader = csv.DictReader(csvfile)
                        exploits = []
                        for row in reader:
                            name = row['Name']
                            cve  = row['Disclosure Date']
                            rank = row['Rank']
                            description = row['Description']
                            exploit = {
                            'name':name,
                            'cve':cve,
                            'rank':rank,
                            'description':description
                            }
                            exploits.append(exploit)
                        ports[port]['exploits'] = exploits
        return ports
