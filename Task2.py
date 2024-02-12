
#Python program to read the throughput values 
#from a file and thn calculate JFI
def calcJFI(throughputs):
    if len(throughputs)==0:
        return 0.0

    numerator =sum(throughputs)**2
    denumerator = len (throughputs) * sum(x ** 2 for x in throughputs)
    jfi =numerator/denumerator
    return jfi

#Converts units 
def units(unit):
    units=unit[-1]
    throughput=float(unit[:-1])
    
    if units.lower() =='k':
        return throughput *1000
    
    elif unit.lower() =='m':
        return throughput * 1000000
    else:
        return throughput
    
#Read files that contains throughputs
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            throughputs=[units(line.strip()) for line in file]
        return throughputs
        
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as  e:
        print("An error occurred", e)
        return []

        
