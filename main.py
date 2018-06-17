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
        self.receptive_field = []
        self.firing_history = []
        self.id_counter = len(units)

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
                receptive_field += [sensory]
            sensory.fire()
            
    def create_association(self, units):
        candidate = Set()
        for u in units:
            
            
        
    def instantiate_unit(self, units):
        if units not in self.units:
            new_unit = Unit(self.id_counter, None, unit_type="default", content=units)
            self.id_counter += 1
            self.units += [new_unit]
        self.units[units].fire()

    def propagate_activations(self):
        for i in range(0, len(self.receptive_field)-1):
            instantiate_unit([self.receptive_field[i], self.receptive_field[i+1]])
            if i < len(self.receptive_field) - 2:
                instantiate_unit([self.receptive_field[i], self.receptive_field[i+1], self.receptive_field[i+2]])
            if i < len(self.receptive_field) - 3:
                instantiate_unit([self.receptive_field[i], self.receptive_field[i+1], self.receptive_field[i+2], self.receptive_field[i+3]])

            
    def cognitive_loop(self, input):
        process_input(input)
        
        
            
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
    
