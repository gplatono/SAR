import xml.etree.ElementTree as ET

class Schema(object):
    def __init__(self, id):
        self.id = id

class Agent(object):
    def __init__(self, schemas):
        self.schemas = schemas
    
schemas = {}
schemas_db = ET.parse("schemas.xml")
root = schemas_db.getroot()
root.append(ET.Element("TEST"))
schemas_db.write("schemas.xml")
#for elem in schemas_db:
    
