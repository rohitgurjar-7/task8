#!/usr/bin/python3
import cgi
import os
import subprocess as sp
print("content-type: text/html")
print()
f=cgi.FieldStorage()
cmd = f.getvalue("x")

if cmd == "MH02EC 4747":
	print('''<pre>
	Car Number: MH02EC 4747
	Car Model: Maserati Quattroporto
	Registration Name: Sushant Singh Rajput
	Fuel Type: Petrol 
	Location: Haryana , India
	Vehicle Class: Super Sedan
	</pre>''')

elif cmd == "TTL D4FTY":
	print('''<pre>
	Car Number: TTL D4FTY
	Car Model: BMW	
	Registration Name: Suresh
	Registration Date: 17/1/2015
	Fuel Type: CNG
	Location: TamilNadu, India
	Vehicle Class: SUV
	Insurance Upto: 19/12/2025
	</pre>''')


