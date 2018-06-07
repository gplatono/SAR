import xml.etree.ElementTree as ET

class Unit(object):
    def __init__(self, id, name=None, unit_type="default", content=None):
        self.id = id
        self.name = name
        self.unit_type = unit_type
        self.content = content
        self.activation_level = 0

    def toXMLNode(self):
        node = ET.Element(self.id)
        for key, value in self.__dict__.items():
            node.set(key, value)
        return node

    def fire(self, value=1.0):
        self.activation_level = value

    def attenuate(self, value=0.9):
        self.activation_level *= value
            
class Agent(object):
    def __init__(self, units):
        self.units = units
        self.perception_units = {}
        self.active_units = []
        self.firing_history = []

    def start(self, inputs):
        for input in inputs:
            process_input(input)
            self.firing_history += [self.active_units]
    
    def process_input(self, input):
        for percept in input:            
            if percept not in self.perception_units:
                self.perception_units[percept] = Unit("perc" + len(self.perception_units), unit_type = "SENSORY", content=percept)
            sensory = self.perception_units[percept]
            if sensory not in self.active_units:
                active_units += [sensory]
            sensory.fire()

    def load(self):
        return 1
        

    def persist(self):
        header = "<?xml version=\"1.0\"?><roor><\root>"
        xmltree = ET.fromstring(header)
        root = schemas.getroot()
        for u in self.units:
            root.append(u.toXMLNode())
        xmltree.write("schemas.xml")
        
    


    
    
schemas = {}
schemas_db = ET.parse("schemas.xml")
root = schemas_db.getroot()
root.append(ET.Element("TEST"))
schemas_db.write("schemas.xml")
u = Unit(100, "name1", content = "CONTENT")
print (u.toXMLNode())
#print (u.__dict__)
#for elem in schemas_db:
    
