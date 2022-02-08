import xml.etree.ElementTree as ET
#from lxml import etree as ET

stream = open('sample.xml','r')

xml = ET.parse(stream)
root = xml.getroot()



for e in root:
    #print(ET.tostring(e))
    #print("", end="")
    #print(e.get("Id"))
    print((ET.SubElement(e,"FirstName"))