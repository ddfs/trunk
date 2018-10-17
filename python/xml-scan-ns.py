#!/usr/bin/env python
import re
import xml.etree.ElementTree as ET

if __name__ == "__main__":
    xml_namespaces = dict([
         node for _, node in ET.iterparse(
             'data.xml', events=['start-ns']
         )
    ])

    print(xml_namespaces)

    xml_tree = ET.parse('data.xml')
    xml_root = xml_tree.getroot()

    for node in xml_root.findall('ss:Worksheet/ss:Table/ss:Row', xml_namespaces):
        print(node.findall('ss:Cell/ss:Data', xml_namespaces))
