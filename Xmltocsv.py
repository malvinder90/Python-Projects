#Q3. Write a program to convert xml data to csv file.
"""
<Employees>
<Employee>
	<name>Rajesh</name>
	<address>Chennai</address>
	<dept>IT</dept>
</Employee>
<Employee>
	<name>Suresh</name>
	<address>Bangalore</address>
	<dept>Non-IT</dept>
</Employee>
<Employee>
	<name>Mahesh</name>
	<address>Pune</address>
	<dept>Bank</dept>
</Employee>
</Employees>
"""

import xml.etree.ElementTree as ET
import csv
f = ET.parse("xml1.xml")
root = f.getroot()
f1 = open("Employee.csv","w")
cwo = csv.writer(f1)
list_head = []                           #list that contain header
count = 0
for element in root.findall("Employee"): #Loop for each node
    list_nodes = []
    if count==0:
        name = element.find("name").tag
        list_head.append(name)

        address = element.find("address").tag
        list_head.append(address)

        dept = element.find("dept").tag
        list_head.append(dept)

        cwo.writerow(list_head)
        count+=1

    name = element.find("name").text       #get child node# list_nodes.append(name)
    list_nodes.append(name)

    address = element.find("address").text
    list_nodes.append(address)

    dept = element.find("dept").text
    list_nodes.append(dept)
    cwo.writerow(list_nodes)

f1.close()



