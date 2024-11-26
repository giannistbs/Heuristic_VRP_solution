#from TSP_Model import Model
from Solver import *

m = Model()
m.load_model("Instance.txt")
s = Solver(m)
sol = s.solve()