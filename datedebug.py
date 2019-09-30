import pandas as pd

listdate = pd.date_range('2019-09-06', '2019-09-12', freq='B').strftime("%Y-%m-%d").tolist()

# for i in listdate:
#     print(i)

length = len(listdate)
i = 0
while i < length:
    print(listdate[i])
    i += 1

#print(listdate[0])