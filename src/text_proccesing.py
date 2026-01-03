def text_analysis(input="log.txt",output="summary_log.txt"):
    ip=[]
    warning_log=0
    error_log=0
    total_log=0
    
    with open(input,"r") as f:
        for line in f:
            total_log+=1
            
            split_log=line.strip().split(" | ")
            
            date_time=split_log[0]
            level=split_log[1]
            description=split_log[2]
            ip_address=split_log[3]
            status=split_log[4]
            http_code=split_log[5]
            
            ip.append(ip_address)
            
            if level=="ERROR" or level=="CRITICAL":
                error_log+=1
            elif level=="WARNING":
                warning_log+=1
                
    with open(output,"w") as f:
        f.write("---------------Log Summary------------------------\n")
        f.write(f"Total Logs : {total_log}\n")
        f.write(f"Error Logs : {error_log}\n")
        f.write(f"Warning Logs : {warning_log}\n")
        f.write("Collected Ips : \n")
        for i in ip:
            f.write(i + "\n")
            
            
text_analysis()
        
            