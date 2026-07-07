from sklearn.datasets import load_iris #데이터 가져오기
import pandas as pd #판다스 사용
from sklearn import svm #모델 사용
import plotly.express as px #3차원 그래프 그리기

iris= load_iris() #iris 데이터 가져오기
df = pd.DataFrame (iris.data) #2차원으로
s=svm.SVC(gamma=0.1, C=10)
s.fit(iris.data, iris.target) #학습해

new_d=[[5.1, 3.5, 1.4, 0.2], [6.7, 3.1, 4.7, 1.5], [7.2, 3.6, 6.1, 2.5]]
res=s.predict(new_d) # 위에 숫자 4개 예측해
print("새로운 2개 샘플의 부류는", res) #결과 출력

df = px.data.iris() #plotly express에서 iris 데이터 가져오기
# petal_length를 제외하여 3차원 공간 구성
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
fig.show(renderer="browser")