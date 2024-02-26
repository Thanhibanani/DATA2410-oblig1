# This is a function to calculate JFI
# The functions uses the JFI formula to calculate throughputs.
# An user have to type in throughputs and the function will return a JFI.



def calc_jfi(throughputs):
   
    #calculate the length og the throughputs
    #returns the number og elements
    num_flows = len(throughputs)
    #calculates the sum of througputs
    sum_throughputs = sum(throughputs)
    #calculates the sum of squares of each throughput
    sum_square = sum(x**2 for x in throughputs)
    
    #Checks for 0 flows, if there are 0 flows return 0
    #If there are flows, proceed with calculating.
    if num_flows==0:
        return 0
    else:
        jfi=(sum_throughputs**2)/ (num_flows *sum_square)
        return jfi
    
    
#Run program in "main"
if __name__ == "__main__":
    throughputs =[float(throughputs) for throughputs in input("Enter throughputs").split()]
    jfi =calc_jfi(throughputs)
    print("jfi:" ,jfi)
    
    
