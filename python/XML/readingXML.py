from xml.dom import minidom
import sys, os
sys.path.append(os.path.abspath("python/XML/files"))

mydoc = minidom.parse('GVL.xml')
