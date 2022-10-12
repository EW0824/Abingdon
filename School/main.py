# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
import csv

travelToWork = np.genfromtext('~/Desktop/Copy of Method of travel to work by age DATA1.csv', delimiter=',')
travelToWorktwo = pd.read_csv('~/Desktop/Copy of Method of travel to work by age DATA1.csv', sep=',',header=None)

print(travelToWorktwo)


