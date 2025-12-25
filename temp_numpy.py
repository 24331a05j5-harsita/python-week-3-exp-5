import numpy as np
temps=[34,24,43,47,29,56,67]
nptemps=np.array(temps)
print("maximum temperature is:",np.max(temps))
print("minimum temperature is:",np.min(temps))
print("standard deviation is:",np.std(temps))
print(temps)
print(np.where(nptemps>30,"hot","cool"))


