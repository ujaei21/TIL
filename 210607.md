# 2021/06/07

## Jupyter Notebook 

### 초기 설정

```python
conda deactivate 
conda activate multi
#package 설치
pip install pandas==1.2.3
pip install pandas-profiling==2.12.0
pip install ipywidgets
```

![Cognitive](https://user-images.githubusercontent.com/54794815/120935624-ac723e00-c73e-11eb-8587-a84653756c70.jpg)

기억의 종류 

1. 감각기억
2. 워킹메모리
3.  장기기억

스마트폰으로 읽으면 감각에 변화가 생기지 않는다. 책은 읽고 나면 어디다 두었는지 보인다. 

즉 책으로 읽으면 책의 위치정보 두께 장소 냄새 글의 위치 촉감 등이 어디에 두었는지 다양한 정보들이 같이 저장이 된다. 감각 + 뜻이 저장됨으로 생각의 우물에서 건져올 수 있다. 

 그러나 스마트폰은 다 똑같다고 느끼기 때문에 중첩된 정보가 많아지기 때문에 기억이 잘나지 않는다.

### 지난번에 배운 것

```python
pandas.info()
pandas.decribe()
df.profile_report()

df.Series() #key,value -> Map/Reduce
df.DataFrame() #index, Column 

```

논리적인 사고를 바탕으로 문제 해결 능력이 필요하다. (논리적인 사고, 문제해결능력)

```python
import pandas as pd
# 파일 읽기
variable = pd.read_csv('FileName.csv',index_col=0)
# index_col = 0 인덱스 없애기
# 파일 쓰기
variable.to_csv('FileName.csv')

```

