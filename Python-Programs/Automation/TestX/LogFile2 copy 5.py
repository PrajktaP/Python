import sys
import time

def main():
    timestamp = time.ctime()

    file_name = "MarvellousLog%s.log" %(timestamp)
    file_name = file_name.replace(" ", "_")
    file_name = file_name.replace(":", "_")

    fobj = open(file_name, "w")
    
    border = "-"*80

    fobj.write(border + "\n")
    fobj.write("This is a log file of Marvellous Automation script \n")
    fobj.write("\n" + border)

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    fobj.write(border + "\n")
    
    fobj.write("File created at: " + timestamp)
    
    fobj.write(border + "\n")

if __name__ == "__main__":
    main()