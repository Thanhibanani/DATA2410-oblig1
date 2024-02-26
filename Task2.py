
#Python program to read the throughput values 
#from a file and thn calculate JFI
#CalcJFI copied from task 1 but num_flows,sum_flows and sum_square is renamed 

def calcJFI(throughputs):
    if len(throughputs)==0:
        return 0.0

    numerator =sum(throughputs)**2
    denominator = len (throughputs) * sum(x ** 2 for x in throughputs)
    jfi =numerator/denominator
    return jfi

#Converts units 
def conevert_units(unit):
    units=unit[-4]
    throughput=float(unit[:-5])
    
    if units.lower() =='kbps':
        return throughput *1000
    
    elif units.lower() =='mbps':
        return throughput * 1000000
    else:
        return throughput
    
#Read files that contains throughputs
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            throughputs=[conevert_units(line.strip()) for line in file]
        return throughputs
        
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as  e:
        print("An error occurred", e)
        return []

#Finds the file
filename ='Task2.txt'

#reads the file
throughputs=read_file(filename)

#calls the function and calculates
jfi=calcJFI(throughputs)

#prints JFI
print('jfi:', jfi)    

        
