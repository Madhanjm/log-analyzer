from faker import Faker
import random
fake=Faker()

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

with open("log.txt","w") as f:
    for _ in range(10):
        level=random.choice(levels)
        log=(
            f"{fake.date_time()} | "
            f"{level} | "
            f"{random.choice(description)} | "
            f"{fake.bothify(text="???###")} | "
            f"{fake.ipv4()} | "
            f"{status[level]} | "
            f"{fake.http_status_code()}"
        )
        f.write(log+"\n")