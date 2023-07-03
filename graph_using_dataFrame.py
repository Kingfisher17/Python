import pandas as pd
import matplotlib.pyplot as graph

rowData = {
    "Year" : [i for i in range(2001,2024)],
    "Income_in_crores": [2.4,2.2,10,2.5,3.0,3.2,2.6,4.1,5.0,2.5,3.5,30,4.2,4.2,4.3,5.1,4.1,4.1,15,5.1,4.2,6.0,4.6]
}

data = pd.DataFrame(rowData)
data.plot(x="Year",y="Income_in_crores",kind="scatter",title="Income")
graph.show()
