import platform
import os 

cwd = os.getcwd()
my_system = platform.uname()
 
print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Current Working Directory: {cwd}")