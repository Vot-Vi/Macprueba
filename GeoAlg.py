import numpy as np

class GeomAlg:
  def spade(self):
    if isinstance(self,vector)==True:
      return self
    elif isinstance(self,bivector)==True:
      a=bivector()
      return -self
  def mod(self):
    return np.sqrt(self*spade(self))
  def __truediv__(self,other):
    return self*other/mod(other)



class vector(GeomAlg):
  def __init__(self,e0,e1,e2,e3):
    self.e0=e0
    self.e1=e1
    self.e2=e2
    self.e3=e3
  def __rpr__(self):
    return f{self.e0*e0+self.e1*e1+self.e2*e2+self.e3*e3}
  def __mult__(self,other):
    return self.e0*other.e0-self.e1*other.e1-self.e2*other.e2-self.e3*other.e3
  def __sum__(self,other):
    return vector(self.e0+other.e0,self.e1+other.e1,self.e2+other.e2,self.e3+other.e3)


class bivector(GeomAlg):
  def __init__(self,e01,e02,e03,e23,e13,e12):
    self.e01=e01
    self.e02=e02
    self.e03=e03
    self.e23=e23
    self.e13=e13
    self.e12=e12

class trivector(GeomAlg):
  def __init__(self,e023,e013,e012,e123):
    self.e023=e023
    self.e013=e013
    self.e012=e012
    self.e123=e123

class pseudoescalar(GeomAlg):
  def __init__(self,e0123):
    self.e0123=e0123

class escalar(GeomAlg):
  def __init__(self,c):
    self.c=c   
    
 
