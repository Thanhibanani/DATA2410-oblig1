# Calculate JFI

def calc_jfi(throughputs):
    num_flows = len(throughputs)
    sum_throughputs = sum(throughputs)
    sum_square = sum(x**2 for x in throughputs)
    
    if num_flows==0:
        return 0
    else:
        jfi=(sum_throughputs**2)/ (num_flows *sum_square)
        return jfi
    
if __name__ == "__main__":
    throughputs =[float(throughputs) for throughputs in input("Enter throughputs").split()]
    jfi =calc_jfi(throughputs)
    print("jfi:" ,jfi)
    
    
