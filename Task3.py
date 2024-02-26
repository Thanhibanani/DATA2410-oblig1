
#Imports
import argparse
import sys

#Checks ports using try and except
#Gives out ArgumentTypeError
def check_ports(val):
    #Checks input value.
    try:
        value=int(val)
    except ValueError:
        raise argparse.ArgumentTypeError('Integer please')
    #Checks for valid port
    if(value<=0):
        raise argparse.ArgumentTypeError('Invalid port')
        sys.exit()
    return value

#Validate IP-adress using try and except
#Gives out ArgumentTypeError
def valid_ip(ip):
#Splits ip using '.'
    parts =ip.split('.')
#Must contain 4 integers
    if len(parts) !=4:
        raise argparse.ArgumentTypeError('IP must be four numbers')
    try:
#Checks for if the IP is in range of 0-255
        parts=[int(part) for part in parts]
        for part in parts:
            if part <0 or part> 255:
                raise argparse.ArgumentTypeError('Must be in range of 0-255')
    except ValueError:
        raise argparse.ArgumentTypeError('Must be number')
    return ip


#Arguments corrisponding to the given table.
parser=argparse.ArgumentParser()
parser.add_argument('-s', '--server', action='store_true', help='Enable server mode')
parser.add_argument('-c', '--client', action='store_true', help='Enable client mode')
parser.add_argument('-p', '--port', type=check_ports, default=8088, help='Port number for server')
parser.add_argument('-i','--ip', type=valid_ip, default ='127.0.0.1', help='IP of server for client to connect')

args=parser.parse_args()

#Gives put error messages if user writes wrong arguments/ flags or uses multiple flags.
#Gives out success messages and which port and ip the user  have chosen.
if args.server and args.client:
    print("Cannot enable both server and client")
elif args.server:
    print(f"Server mode enabled. {args.ip}:{args.port}")
elif args.client:
    print(f"Client mode enabled. {args.ip}:{args.port}")
else:
    print('No server and no client enabled.')   
    
