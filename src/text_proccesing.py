import re
def text_analysis(input="log.txt",output="summary_log.txt"):
    unique_ip=set()
    code_freq={}
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
            
            unique_ip.add(ip_address)
            
            if level=="ERROR" or level=="CRITICAL":
                error_log+=1
            elif level=="WARNING":
                warning_log+=1
                
            if re.match(r"[245]\d{2}",http_code):
                if http_code in code_freq:
                    code_freq[http_code]+=1
                else:
                    code_freq[http_code]=1
                        
    with open(output,"w") as f:
        f.write("---------------Log Summary------------------------\n")
        f.write(f"Total Logs : {total_log}\n")
        f.write(f"Error Logs : {error_log}\n")
        f.write(f"Warning Logs : {warning_log}\n")
        f.write("Unique Ips : \n")
        for i in unique_ip:
            f.write(i + "\n")
            
        f.write("HTTP CODE FREQUENCY:\n")
        for code,count in code_freq.items():
            f.write(f"{code}:{count}\n")
            
            
            
def match_ip_errcode():
    with open("log.txt","r") as f,open("ip_errcode_match_regex.txt","w") as match:
        for line in f:
            ip=re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line)
            err_code=re.search(r"[45]\d{2}",line)
            
            if ip:
                match.write(f"IP : {ip.group()}\n")
            if err_code:
                match.write(f"HTTP ERROR CODE : {err_code.group()}\n")
                
text_analysis()
                