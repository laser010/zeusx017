#!/usr/bin/env python3
from libs.printer  import *
from libs.settings import *
from libs.commander import command
from libs.metasploit import metasploit
import socket
import csv
import os
##########
DATA = {}
##########

def main():
    global info
    global errer
    conf = getConf()
    banner = conf['banner']
    print(banner)
    target = input('Enter the IP target : ')
    if  target == '':
        errorMsg = ('You must enter the target!')
        error(errorMsg)
        exit(1)
    elif '/' in target or  '\\' in target:
        errorMsg = ('You must enter the target without "/" or "\\" to work without errors.')
        error(errorMsg)
        exit(1)
    elif target  != '':
        if target.count('.') == 3:
            pass
        elif target.count('.') != 3:
            print('[{host}] This is not IPv4!'.format(host=target))
            exit(1)
            result = command(cmd='ping -c 1 {host}'.format(host=target), live=False)
            if 'Destination Host Unreachable' in result:
                exit('[{host}] host is down'.format(host=target))
            elif 'Destination Host Unreachable' not in result:
                print('[{host}] host is up'.format(host=target))
        command('service postgresql start').run()
        try:
            os.mkdir('output/{target}'.format(target=target))
        except FileExistsError:
             pass
    # Start port scan with nmap (Network Mapper), First scan.
        output = ('output/{target}'.format(target=target))
        info('Start port scan with nmap (Network Mapper)')
        metasploit(ip=target, output=output).nmap()
        nmOUT = (output+"/nmap.csv")
        with open(nmOUT, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            ports = {}
            for row in reader:
                port = row['port']
                proto = row['proto']
                name = row['name']
                state = row['state']
                info = row['info']
                p = {
                'port':port,
                'proto':proto,
                'name':name,
                'state':state,
                'info':info,
                'exploits':[]
                }
                ports[port] = p

        print('[+] Start searching exploits')
        command('service postgresql start').run()
        ports = metasploit(output=output).searchSploit(ports=ports)
        DATA[target] = ports
        ports = DATA[target]
        #The last
        for key, valu in ports.items():
            result = '\n\n\033[1;32;40m#'+30*'-'+'#'
            result += ('\nip         : {target}'.format(target=target))
            result += '\n#'+30*'-'+'#'
            port = ports[key]['port']
            proto = ports[key]['proto']
            name = ports[key]['name']
            state = ports[key]['state']
            info = ports[key]['info']
            exploits = ports[key]['exploits']
            result += ('\nPORT    : {port}/{proto}'.format(port=port, proto=proto))
            result += ('\nSERVICE : {name}'.format(name=name))
            result += ('\nVERSION : {info}'.format(info=info))
            result += '\n#'+30*'-'+'#'
            num = len(exploits)
            result += '\n#'+10*'-'+'\033[31;1;40m EXPLOITS : {num}'.format(num=num)
            if num == 0:
                result += ('\nEploits is not exist!')
            for exploit in exploits:
                result += '\n#'+30*'-'+'#'
                EXname = exploit['name']
                cve = exploit['cve']
                rank = exploit['rank']
                description = exploit['description']
                result += ('\n\tNAME        : {name}'.format(name=EXname))
                result += ('\n\tCVE         : {cve}'.format(cve=cve))
                result += ('\n\tDESCRIPTION : {description}'.format(description=description))
            print(result)
            print('\033[0m')
