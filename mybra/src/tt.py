from pandas import *
from matplotlib import *
from numpy import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy


engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
sales = read_sql('select source,size1,color1 from t_sales', engine)
zbBlack = []
bra = ['A','B','C']
for zb in bra:
    size1Count = sales[sales['size1']== zb].groupby(['size1','color1'])['size1'].count()
    size1Total = size1Count.sum()
    
    size1 = size1Count.to_frame(name='销量')
    size1 = size1.sort_values(['销量'], ascending=[0])
    size1.insert(0,'比例',100 * size1Count / size1Total)
    size1Count = size1.iloc[0,0]
    zbBlack.append(size1Count)
print(zbBlack)

bar([1,2,3],zbBlack)
xlabel(bra)
show()



