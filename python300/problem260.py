# error 발생 원인
class OMG :
    def print() :
        print("Oh my god")

>>> >>> myStock = OMG()
>>> myStock.print()
TypeError Traceback (most recent call last)
<ipython-input-233-c85c04535b22> in <module>()
----> myStock.print()

TypeError: print() takes 0 positional arguments but 1 was given

'''
def print()에서 문제가 생김
()안에 self를 써줘야한다.
--> 클래스의 메서드에서는 첫번째 매개변수를 self로 지정해줘야 한다.
'''