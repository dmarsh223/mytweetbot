from urllib.request import urlopen
import xml.etree.ElementTree as ET


alert = urlopen("https://alerts.weather.gov/cap/wwaatmget.php?x=NJZ026&y=0")
alert_string = alert.read()

root = ET.fromstring(alert_string)
tree = ET.ElementTree(alert_string)

for child in root:
    print(child.tag, child.attrib)

tree.getroot()

for elem in tree.iter():
    print (elem.tag, elem.attrib)

# for child_of_root in root:
#     print (child_of_root.tag, child_of_root.attrib)


print (alert_string)