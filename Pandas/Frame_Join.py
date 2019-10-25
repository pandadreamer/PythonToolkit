import pandas as pd

df1 = pd.DataFrame({
    'id' : [1,2,3,4,5],
    'price' : [10, 11, 15, 20, 8]})
'''
df1:
----------------
    id	price
0	1	10
1	2	11
2	3	15
3	4	20
4	5	8
'''

df2 = pd.DataFrame({
    'id' : [1,2,3,4,5],
    'label' : [1,0,0,1,0]})
'''
df2:
----------
    id	label
0	1	1
1	5	0
2	3	0
3	2	1
4	4	0
'''

combine = pd.merge(left=df1, right=df2, how='inner', on='id')
'''
combine:
----------

    id	price	label
0	1	10	    1
1	2	11	    1
2	3	15	    0
3	4	20	    0
4	5	8	    0
'''