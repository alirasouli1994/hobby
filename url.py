#URL to IP Converter
import socket
import os
import tkinter as tk
from tkinter import filedialog
import csv

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV File", "*.csv")])

dir_path = os.path.dirname(file_path)
base_name = os.path.splitext(os.path.basename(file_path))[0]
new_path = os.path.join(dir_path,f"{base_name}_ip.csv")

with open(file_path,"r") as file :
    lines = file.readlines()


with open(new_path, "w",newline= '' ) as file:
    writer = csv.DictWriter(file,fieldnames=["url","ip"])
    writer.writeheader()

    for line in lines:
        
        try:
            url= line.rstrip()
            ip = socket.gethostbyname(url)
            writer.writerow({"url" : url, "ip" : ip})
            print(url, ip)
        except Exception as e:
            print(line.rstrip(),e)
            writer.writerow({"url" : url, "ip" : e})