import pandas as pd
import matplotlib
import numpy
import seaborn

df = pd.read_csv('/home/ubantu/Desktop/dataset/qs-world-university-rankings-2017-to-2022-V2.csv')

df.head()#starting data

university	year	rank_display	score	link	country	city	region	logo	type	research_output	student_faculty_ratio	international_students	size	faculty_count
0	Massachusetts Institute of Technology (MIT)	2017	1	100.0	https://www.topuniversities.com/universities/m...	United States	Cambridge	North America	https://www.topuniversities.com/sites/default/...	Private	Very High	4.0	3,730	M	3,065
1	Stanford University	2017	2	98.7	https://www.topuniversities.com/universities/s...	United States	Stanford	North America	https://www.topuniversities.com/sites/default/...	Private	Very High	3.0	3,879	L	4,725
2	Harvard University	2017	3	98.3	https://www.topuniversities.com/universities/h...	United States	Cambridge	North America	https://www.topuniversities.com/sites/default/...	Private	Very High	5.0	5,877	L	4,646
3	University of Cambridge	2017	4	97.2	https://www.topuniversities.com/universities/u...	United Kingdom	Cambridge	Europe	https://www.topuniversities.com/sites/default/...	Public	Very high	4.0	7,925	L	5,800
4	California Institute of Technology (Caltech)	2017	5	96.9	https://www.topuniversities.com/universities/c...	United States	Pasadena	North America	https://www.topuniversities.com/sites/default/...	Private	Very High	2.0	692	S	968
ns datatype

df.info() #tells columns datatype

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6482 entries, 0 to 6481
Data columns (total 15 columns):
 #   Column                  Non-Null Count  Dtype  
---  ------                  --------------  -----  
 0   university              6482 non-null   object 
 1   year                    6482 non-null   int64  
 2   rank_display            6414 non-null   object 
 3   score                   2820 non-null   float64
 4   link                    6482 non-null   object 
 5   country                 6482 non-null   object 
 6   city                    6304 non-null   object 
 7   region                  6482 non-null   object 
 8   logo                    6482 non-null   object 
 9   type                    6470 non-null   object 
 10  research_output         6480 non-null   object 
 11  student_faculty_ratio   6407 non-null   float64
 12  international_students  6318 non-null   object 
 13  size                    6480 non-null   object 
 14  faculty_count           6404 non-null   object 
dtypes: float64(2), int64(1), object(12)
memory usage: 759.7+ KB

df.describe()

year	score	student_faculty_ratio
count	6482.000000	2820.000000	6407.000000
mean	2019.693613	46.595532	13.264554
std	1.716683	18.813110	6.604294
min	2017.000000	23.500000	1.000000
25%	2018.000000	31.800000	9.000000
50%	2020.000000	40.600000	12.000000
75%	2021.000000	58.025000	17.000000
max	2022.000000	100.000000	67.000000
ues

df.tail(10)#show last 10 values

university	year	rank_display	score	link	country	city	region	logo	type	research_output	student_faculty_ratio	international_students	size	faculty_count
6472	University of Sarajevo	2022	1201	NaN	https://www.topuniversities.com/universities/u...	Bosnia and Herzegovina	Sarajevo	Europe	https://www.topuniversities.com/sites/default/...	Public	Medium	23.0	1,003	XL	1,306
6473	University of Split	2022	1201	NaN	https://www.topuniversities.com/universities/u...	Croatia	Split	Europe	https://www.topuniversities.com/sites/default/...	Public	High	16.0	373	L	1,005
6474	Università degli studi di Bergamo	2022	1201	NaN	https://www.topuniversities.com/universities/u...	Italy	Bergamo	Europe	https://www.topuniversities.com/sites/default/...	Public	High	24.0	1,244	L	787
6475	Université Mohammed V de Rabat	2022	1201	NaN	https://www.topuniversities.com/universities/u...	Morocco	Rabat	Africa	https://www.topuniversities.com/sites/default/...	Public	Very High	45.0	2,441	XL	1,806
6476	Université de Caen Normandie	2022	1201	NaN	https://www.topuniversities.com/universities/u...	France	Caen	Europe	https://www.topuniversities.com/sites/default/...	Public	High	19.0	1,976	L	1,535
6477	Université de Tunis	2022	1201	NaN	https://www.topuniversities.com/universities/u...	Tunisia	Tunis	Africa	https://www.topuniversities.com/sites/default/...	Public	High	17.0	57	L	1,174
6478	Université de Tunis El Manar	2022	1201	NaN	https://www.topuniversities.com/universities/u...	Tunisia	Tunis	Africa	https://www.topuniversities.com/sites/default/...	Public	Very High	8.0	585	L	3,504
6479	Yarmouk University	2022	1201	NaN	https://www.topuniversities.com/universities/y...	Jordan	Irbid	Asia	https://www.topuniversities.com/sites/default/...	Public	Medium	31.0	2,826	XL	1,113
6480	Yildiz Technical University	2022	1201	NaN	https://www.topuniversities.com/universities/y...	Turkey	Istanbul	Asia	https://www.topuniversities.com/sites/default/...	Public	High	20.0	2,394	XL	1,688
6481	Zagazig University	2022	1201	NaN	https://www.topuniversities.com/universities/z...	Egypt	Zagazig	Africa	https://www.topuniversities.com/sites/default/...	Public	High	26.0	2,300	XL	5,871

df = df.dropna()#to drop null

df['year'] = df['year'].astype('string')#to change datatype of column

df.info()

<class 'pandas.core.frame.DataFrame'>
Int64Index: 2716 entries, 0 to 5682
Data columns (total 15 columns):
 #   Column                  Non-Null Count  Dtype  
---  ------                  --------------  -----  
 0   university              2716 non-null   object 
 1   year                    2716 non-null   string 
 2   rank_display            2716 non-null   object 
 3   score                   2716 non-null   float64
 4   link                    2716 non-null   object 
 5   country                 2716 non-null   object 
 6   city                    2716 non-null   object 
 7   region                  2716 non-null   object 
 8   logo                    2716 non-null   object 
 9   type                    2716 non-null   object 
 10  research_output         2716 non-null   object 
 11  student_faculty_ratio   2716 non-null   float64
 12  international_students  2716 non-null   object 
 13  size                    2716 non-null   object 
 14  faculty_count           2716 non-null   object 
dtypes: float64(2), object(12), string(1)
memory usage: 339.5+ KB
region

pd.get_dummies(df['region']) #to change categorical data to quantitative data

Africa	Asia	Europe	Latin America	North America	Oceania
0	0	0	0	0	1	0
1	0	0	0	0	1	0
2	0	0	0	0	1	0
3	0	0	1	0	0	0
4	0	0	0	0	1	0
...	...	...	...	...	...	...
5678	0	1	0	0	0	0
5679	0	0	0	0	1	0
5680	0	1	0	0	0	0
5681	0	0	1	0	0	0
5682	0	0	0	0	1	0
2716 rows × 6 columns
