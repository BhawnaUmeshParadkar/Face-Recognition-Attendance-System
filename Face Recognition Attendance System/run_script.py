import os
import subprocess

# Change the working directory
os.chdir("C:/Users/ADMIN/Desktop/Face Recognition Attendance System")

# Run the login.py script in a separate process
subprocess.Popen(["python", "-u", "newmain.py"], creationflags=subprocess.DETACHED_PROCESS)