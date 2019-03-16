# Import the library
"""
Exemple de KML

<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Placemark>
    <name>Simple placemark</name>
    <description>Attached to the ground. Intelligently places itself 
       at the height of the underlying terrain.</description>
    <Point>
      <coordinates>-122.0822035425683,37.42228990140251,0</coordinates>
    </Point>
  </Placemark>
</kml>
"""
import xml.etree.ElementTree as ET
# import lxml.etree.ElementTree.

import os, sys

def createPlacemark(StrFromCSV):
  print("createPlacemark")

def go():
  print("CreateKML")

if __name__=="__main__":
  # kml=ET.Element("kml",{"xmlns":"http://www.opengis.net/kml/2.2"})
  # T=ET.ElementTree()
  # E=T.getroot()
  Top='<?xml version="1.0" encoding="UTF-8"?>'
  # E.insert(0,Top)

  kml=ET.Element('kml',{"xmlns":"http://www.opengis.net/kml/2.2"})
  ET.Element
  Placemark=ET.SubElement(kml,'Placemark')
  name=ET.SubElement(Placemark,"name",{})
  name.text="Lille"
  desc=ET.SubElement(Placemark,"description",{})
  desc.text="Attached to the ground. Intelligently places itself at the height of the underlying terrain."
  p= ET.SubElement(Placemark,"Point",{})
  coor=ET.SubElement(p,"coordinates",{})
  coor.text ="-50.6305089,3.0706414,0"


  # Placemark=ET.SubElement(kml,'Placemark')
  # name=ET.SubElement(Placemark,"name",{})
  # name.text="Simple Placemark"
  # desc=ET.SubElement(Placemark,"description",{})
  # desc.text="Attached to the ground. Intelligently places itself at the height of the underlying terrain."
  # p= ET.SubElement(Placemark,"Point",{})
  # coor=ET.SubElement(p,"coordinates",{})
  # coor.text ="-123.0822035425643,37.42228990140251,0"

  # Placemark=ET.SubElement(kml,'Placemark')
  # name=ET.SubElement(Placemark,"name",{})
  # name.text="Simple Placemark"
  # desc=ET.SubElement(Placemark,"description",{})
  # desc.text="Attached to the ground. Intelligently places itself at the height of the underlying terrain."
  # p= ET.SubElement(Placemark,"Point",{})
  # coor=ET.SubElement(p,"coordinates",{})
  # coor.text ="-124.0822035425643,37.42228990140251,0"



  # ET.dump(Top)
  # ET.tostring

  myfile = open("k.kml", "wb")  
  # mydata = ET.tostring(Top)  
  # myfile.write(Top)  
  # mydata2 = ET.tostring(kml)  
  # myfile.write(mydata2)  
  T=ET.ElementTree(kml)

  T.write("k.kml",encoding="UTF-8",xml_declaration=True)#encoding 'UTF-8')

