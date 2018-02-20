Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> df.apply(np.cumsum)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'df' is not defined
>>> import pandas as pd
>>> import numpy as np
>>>
>>> import matplotlib.pyplot as plt
>>> s = pd.Series([1,3,5,np.nan,6,8])
>>> s
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
>>> dates = pd.date_range('20130101', periods=6)
>>>
>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
>>> df
                   A         B         C         D
2013-01-01  0.458114 -0.312330  0.474625  0.597751
2013-01-02 -0.156457  0.105275  2.461899  0.675910
2013-01-03 -0.258353  1.622126  1.343006  0.036481
2013-01-04  0.850478 -1.216040 -0.230575  1.022772
2013-01-05  0.024086  0.000870  0.989516 -0.494164
2013-01-06 -0.148205  0.213207 -0.386986 -0.268832
>>> df2 = pd.DataFrame({ 'A' : 1.,'B' : pd.Timestamp('20130102'),'C' : pd.Series(1,index=list(range(4)),dtype='float32'),'D' : np.array([3] * 4,dtype='int32'),'E' : pd.Categorical(["test","train","test","train"]),'F' : 'foo' })
>>> df2
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
>>> df2.dtypes
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
>>> df.head()
                   A         B         C         D
2013-01-01  0.458114 -0.312330  0.474625  0.597751
2013-01-02 -0.156457  0.105275  2.461899  0.675910
2013-01-03 -0.258353  1.622126  1.343006  0.036481
2013-01-04  0.850478 -1.216040 -0.230575  1.022772
2013-01-05  0.024086  0.000870  0.989516 -0.494164
>>> df.tail(3)
                   A         B         C         D
2013-01-04  0.850478 -1.216040 -0.230575  1.022772
2013-01-05  0.024086  0.000870  0.989516 -0.494164
2013-01-06 -0.148205  0.213207 -0.386986 -0.268832
>>> df.index
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> df.column
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Naveen Kumar\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\generic.py", line 3614, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'column'
>>> df.columns
Index(['A', 'B', 'C', 'D'], dtype='object')
>>> df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
>>> df1
                   A         B         C         D   E
2013-01-01  0.458114 -0.312330  0.474625  0.597751 NaN
2013-01-02 -0.156457  0.105275  2.461899  0.675910 NaN
2013-01-03 -0.258353  1.622126  1.343006  0.036481 NaN
2013-01-04  0.850478 -1.216040 -0.230575  1.022772 NaN
>>> fd.mean
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fd' is not defined
>>> dd.mean
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dd' is not defined
>>> df.mean
<bound method DataFrame.mean of                    A         B         C         D
2013-01-01  0.458114 -0.312330  0.474625  0.597751
2013-01-02 -0.156457  0.105275  2.461899  0.675910
2013-01-03 -0.258353  1.622126  1.343006  0.036481
2013-01-04  0.850478 -1.216040 -0.230575  1.022772
2013-01-05  0.024086  0.000870  0.989516 -0.494164
2013-01-06 -0.148205  0.213207 -0.386986 -0.268832>
>>> df.mean(1)
2013-01-01    0.304540
2013-01-02    0.771657
2013-01-03    0.685815
2013-01-04    0.106659
2013-01-05    0.130077
2013-01-06   -0.147704
Freq: D, dtype: float64
>>> s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
>>> s
2013-01-01    NaN
2013-01-02    NaN
2013-01-03    1.0
2013-01-04    3.0
2013-01-05    5.0
2013-01-06    NaN
Freq: D, dtype: float64
>>> df.sub(s, axis='index')
                   A         B         C         D
2013-01-01       NaN       NaN       NaN       NaN
2013-01-02       NaN       NaN       NaN       NaN
2013-01-03 -1.258353  0.622126  0.343006 -0.963519
2013-01-04 -2.149522 -4.216040 -3.230575 -1.977228
2013-01-05 -4.975914 -4.999130 -4.010484 -5.494164
2013-01-06       NaN       NaN       NaN       NaN
>>> df.apply(np.cumsum)
                   A         B         C         D
2013-01-01  0.458114 -0.312330  0.474625  0.597751
2013-01-02  0.301657 -0.207055  2.936524  1.273660
2013-01-03  0.043304  1.415071  4.279530  1.310142
2013-01-04  0.893782  0.199031  4.048954  2.332914
2013-01-05  0.917869  0.199901  5.038471  1.838750
2013-01-06  0.769664  0.413108  4.651484  1.569917
>>> df.apply(lambda x: x.max() - x.min())
A    1.108831
B    2.838166
C    2.848885
D    1.516936
dtype: float64
>>> s = pd.Series(np.random.randint(0, 7, size=10))
>>> s
0    2
1    2
2    2
3    4
4    0
5    1
6    2
7    1
8    3
9    1
dtype: int32
>>>
KeyboardInterrupt
>>>
>>> s.value_counts()
2    4
1    3
4    1
3    1
0    1
dtype: int64
>>> s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> s
0       A
1       B
2       C
3    Aaba
4    Baca
5     NaN
6    CABA
7     dog
8     cat
dtype: object
>>>  df = pd.DataFrame(np.random.randn(10, 4))
  File "<stdin>", line 1
    df = pd.DataFrame(np.random.randn(10, 4))
    ^
IndentationError: unexpected indent
>>> df
                   A         B         C         D
2013-01-01  0.458114 -0.312330  0.474625  0.597751
2013-01-02 -0.156457  0.105275  2.461899  0.675910
2013-01-03 -0.258353  1.622126  1.343006  0.036481
2013-01-04  0.850478 -1.216040 -0.230575  1.022772
2013-01-05  0.024086  0.000870  0.989516 -0.494164
2013-01-06 -0.148205  0.213207 -0.386986 -0.268832
>>> pd.concat(pieces)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pieces' is not defined
>>> pieces = [df[:3], df[3:7], df[7:]]
>>> pd.concat(pieces)
                   A         B         C         D
2013-01-01  0.458114 -0.312330  0.474625  0.597751
2013-01-02 -0.156457  0.105275  2.461899  0.675910
2013-01-03 -0.258353  1.622126  1.343006  0.036481
2013-01-04  0.850478 -1.216040 -0.230575  1.022772
2013-01-05  0.024086  0.000870  0.989516 -0.494164
2013-01-06 -0.148205  0.213207 -0.386986 -0.268832
>>> left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
>>> left
   key  lval
0  foo     1
1  foo     2
>>> right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
>>> right
   key  rval
0  foo     4
1  foo     5
>>> pd.merge(left, right, on='key')
   key  lval  rval
0  foo     1     4
1  foo     1     5
2  foo     2     4
3  foo     2     5
>>> df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
>>> df
          A         B         C         D
0 -0.039325 -1.740573 -0.722497  1.318077
1  1.383554  1.210230 -1.524066  1.516723
2 -0.261966 -0.554787  1.538982  1.473805
3 -0.001050 -0.137442 -1.056189  0.255116
4 -0.717922  1.133018 -1.148425  0.538739
5 -0.165489  0.671582  0.537779  1.186354
6  0.346733 -1.743798 -0.238033  2.546356
7  1.365446  0.013033 -0.508772 -1.794906
>>> s = df.iloc[3]
>>> s
A   -0.001050
B   -0.137442
C   -1.056189
D    0.255116
Name: 3, dtype: float64
>>> df.append(s, ignore_index=True)
          A         B         C         D
0 -0.039325 -1.740573 -0.722497  1.318077
1  1.383554  1.210230 -1.524066  1.516723
2 -0.261966 -0.554787  1.538982  1.473805
3 -0.001050 -0.137442 -1.056189  0.255116
4 -0.717922  1.133018 -1.148425  0.538739
5 -0.165489  0.671582  0.537779  1.186354
6  0.346733 -1.743798 -0.238033  2.546356
7  1.365446  0.013033 -0.508772 -1.794906
8 -0.001050 -0.137442 -1.056189  0.255116
>>> df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],'C' : np.random.randn(8),'D' : np.random.randn(8)})
>>> df
     A      B         C         D
0  foo    one  0.739236 -0.152383
1  bar    one -0.521581 -0.076293
2  foo    two -0.374781  0.912553
3  bar  three  0.040701 -1.624080
4  foo    two -2.103241 -0.635300
5  bar    two -1.763138  0.382205
6  foo    one  0.621142  1.846161
7  foo  three  1.044205  0.190554
>>> df.groupby('A').sum()
            C         D
A
bar -2.244018 -1.318168
foo -0.073439  2.161586
>>> df.groupby('A','B').sum()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Naveen Kumar\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\generic.py", line 5159, in groupby
    axis = self._get_axis_number(axis)
  File "C:\Users\Naveen Kumar\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\generic.py", line 357, in _get_axis_number
    .format(axis, type(self)))
ValueError: No axis named B for object type <class 'pandas.core.frame.DataFrame'>
>>> df.groupby(['A','B']).sum()
                  C         D
A   B
bar one   -0.521581 -0.076293
    three  0.040701 -1.624080
    two   -1.763138  0.382205
foo one    1.360378  1.693778
    three  1.044205  0.190554
    two   -2.478022  0.277253
>>>
