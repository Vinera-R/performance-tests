import xml.etree.ElementTree as ET
xml_data = """

<person>
    <name>Jhon Doe</name>
    <age>30</age>
    <city>New York</city>
</person>


"""

root = ET.fromstring(xml_data)
print('person name:', root.find('name').text)
print('person age:', root.find('age').text)
