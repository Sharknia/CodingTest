s = []

s.append(5)
s.append(4)
s.pop()
s.append(1)

print(s)
#최상단 원소부터 출력하는 방법
print(s[::-1])

from collections import deque
#큐 구현을 위해서는 deque 라이브러리를 사용한다. 
#deque는 스택과 큐의 장점을 모두 채용한 것으로, 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue라이브러리를 이용하는것보다 간단하다. 
#대부분의 코딩테스트에서는 collections 모듈과 같은 기본 라이브러리 사용을 허용한다. 

#deque 객체를 리스트 자료형으로 변경하고자 한다면 list() 메소드를 이용한다. 

#메소드와 함수의 차이점 : 메소드는 클래스에 종속되어 이름만으로 호출이 불가능하다. 함수는 이름만으로 호출이 가능하다. 메소드는 함수의 하위 개념

q = deque()

q.append(5)
q.append(4)
q.popleft()
q.append(1)

q = list(q)
print(q)
print(q[::-1])

#q.reverse() 함수를 사용하면 역순으로 바꿔준다.
