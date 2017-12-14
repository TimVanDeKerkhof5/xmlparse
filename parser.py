from lxml import etree as ET

xmllist = []
xml = ""

with open('Allocation_codes2.xml', 'r') as file:
	for line in file.readlines():
		line.strip("\n")
		xmllist.append(line.replace('&lt;','<'))

for item in xmllist:
	xml += item

parser = ET.XMLParser(recover=True)
root = ET.fromstring(xml, parser=parser)

tree = ET.ElementTree(root)
tree.write('codes.xml',pretty_print=True,xml_declaration=True,encoding='utf-8')
