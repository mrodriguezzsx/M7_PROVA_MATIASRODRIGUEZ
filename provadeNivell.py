import pandas as pd
import matplotlib.pyplot as plt

arxiu = pd.read_csv("Llistat.csv", usecols=['NAME','NOTES'])
df = pd.DataFrame(arxiu)

def mitjanaAlumne() :
    mitjanes = df.groupby(by='NAME').mean()
    print(mitjanes)
    df.plot.bar()
    plt.xlabel('ALUMNAT')
    plt.ylabel('NOTES')
    plt.show()



