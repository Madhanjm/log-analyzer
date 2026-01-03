from faker import Faker
import random
fake=Faker()

def genarate_log(filename="log.txt",n=30):

    levels=["DEBUG","INFO","WARNING","ERROR","CRITICAL"]
    description=[
        "User logged in",
        "File not found",
        "Connection established",
        "Data saved successfully",
        "Error processing request",]
    status={
        "DEBUG":"OK",
        "INFO":"OK",
        "WARNING":"FAIL",
        "ERROR":"FAIL",
        "CRITICAL":"CRASH"
    }
    
    status_code=[200,201,400,401,500,503]

    with open("log.txt","w") as f:
        for _ in range(n):
            level=random.choice(levels)
            log=(
                f"{fake.date_time()} | "
                f"{level} | "
                f"{random.choice(description)} | "
                f"{fake.ipv4()} | "
                f"{status[level]} | "
                f"{random.choice(status_code)}"
            )
            f.write(log+"\n")
            
genarate_log()