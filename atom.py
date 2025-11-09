class Atom:
    def __init__(self):
        self.id= None
        self.x= None
        self.y= None
        self.z= None
        self.name= None
        self.serial= None
        self.resname=None
        self.resid=None
        self.bfactor=None
        self.occup=None
        self.chain=None
    def __repr__(self):
        #return f'name={self.name},serial={self.serial},resname={self.resname},resid={self.resid},
        return f'x={self.x},y={self.y},z={self.z}'
    def set_data(self,pdb_line):
        self.x=float(pdb_line[30:38])
        self.y=float(pdb_line[38:46])
        self.z=float(pdb_line[46:54])
        self.occup=float(pdb_line[54:60])
        self.bfactor=float(pdb_line[60:66])
        self.name=pdb_line[12:16].lstrip().rstrip()
        self.serial=pdb_line[6:11].lstrip().rstrip()
        self.resname=pdb_line[17:20].lstrip().rstrip()
        self.resid=pdb_line[22:26].lstrip().rstrip()
        self.chain=pdb_line[21]
    def distance(self,atom):
        d2=(self.x-atom.x)**2+(self.y-atom.y)**2+(self.z-atom.z)**2
        return d2**0.5