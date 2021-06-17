import pandas as pd
import numpy as np
p= pd.panel()
print(p)

#panel creation using items
d = {'point1' : pd.DataFrame(np.random.randn(4, 4)), 
   'point2' : pd.DataFrame(np.random.randn(4, 3))}
p = pd.Panel(d)
print(p)
print(p['point1'])
print(p['point2'])

#using major axis
print(p.major_xs(1))

#using minor axis
print(p.minor_xs(1))