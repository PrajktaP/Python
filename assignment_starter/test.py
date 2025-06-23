import re

data = """
1.Design automation script which display information of running processes as its name, PID,
Username.
Usage : ProcInfo.py
2.Design automation script which accept process name and display information of that process if
it is running.
Usage : ProcInfo.py Notepad
3. Design automation script which accept directory name from user and create log file in that
directory which contains information of running processes as its name, PID, Username.
Usage : ProcInfoLog.py Demo
Demo is name of Directory.
4. Design automation script which accept directory name and mail id from user and create log
file in that directory which contains information of running processes as its name, PID,
Username. After creating log file send that log file to the specified mail.
Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com
Demo is name of Directory.
marvellousinfosystem@gmail.com is the mail id.
"""

# Use regex to split the text into 4 parts at each digit followed by a dot
sections = re.split(r'(?=\b\d\.)', data.strip())

# Clean up the whitespace
sections = [s.strip() for s in sections if s.strip()]

# Now `sections` contains 4 separate instruction blocks
for i, section in enumerate(sections, 1):
    print(f"{section}\n")
