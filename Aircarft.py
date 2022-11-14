class Aircraft:
    def __init__(self,make,code,typ,flight_range):
        self.make=make
        self.code=code
        self.typ=typ
        self.flight_range=flight_range
        
    def __repr__(self) -> str:
        return f'Aircraft make by: {self.make} code:{self.code} typ:{self.typ} rnage:{self.flight_range}'
        
    def get_maker(self):
        return self.make
    