# **리트코드 Valid Paretheses python 풀이**

1. 문제 정의 - valid Paretheses 

[Valid Paretheses 문제](https://leetcode.com/problems/valid-parentheses/)

[![valid paretheses](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARMAAAC3CAMAAAAGjUrGAAAA2FBMVEX///8HBwYAAABiYmL4nxtycnK0srFnZ2dubm5mZmZqamphYWH6+vpwcHBbW1tdXV1UVFSvrKvQ0NDm5ubd3d3t7e329vZSUlLT09OCgoLDw8N5eXmSkpK8vLzp6ekAAAWMjIyampr4mQChoaH/+fQuLi34nQD/7t5KSkqGhobAwMD2oRwyMjGfn58oKSgvNz4oFAD6yo4xIgj6qzz+5sv7t2YuGQAsBgD4vnH89OwnIx7+6tP92LEVFRQyKyecXwBTNwtnRA7HhBebaBO7jlCvbADnlRT3q0WTQMyJAAAK1klEQVR4nO2di3bbuBGGtaYpEABv4k2URDmi5fXK2nXaNNl20227vef936gzIEWCNzlRGMu15js+xzaHxAx+AgMIAqXJhCAIgiAIgiAIgiAIgiAIgiAIgiAIgiAI4v+ByL96Ozt3EC+L9ArZnDuMlwRI8h1wlZw7kJdDUEjy3VVw7kheDGUrAU3Cc4fyUqgl8c8dykuhluR7+9yxvBBqSX4iSQoCkqQNdZwOJEmHWpLfkSQFlSRvfv/uh3MH8zKo0uubP/x4f/v+w7njeQGkmiTXwO3Pd+cO6dy0Jbm+vr++8A4UdCRBVT6eO6xz0isJiHLBLaWW5I/3t8A9iVJP6P/0y4ePdx8//Hx76aLUU7U/HxT49cK7T++E/q4S5fYCRak7zlt9Qq+JcnGjz+DLvrvrMtPe/3Km0M5F2t9KkLtqVD5LZGfjiCS1KJ/OENj5iI5Jcug+t3959rjOSHJcEhDlPUzg3j1zVOdl94QkwA8fLmvU2T8tycXx9orWXlukpSR/JUkqHkpNonMH8oL4qdhP4ejHoukR0nNF+nyUe0yW2qFodkyT2avfehGXXSfWjh1TBEV57ZnnptRE24tkH20moEk8XNyr4JR28ur3cn15PlkOlvVa6B13Zkd49Sl2aH5iD3KmMJ8Vmsf2cHi9QzuSavYDK7EXTbV+8v3gKZe2fgJTlCc29F3gOpu2HtvbfS5xPbax9bNrvMx1+6M7He9+vL/I93eObBKu3vK6uPcBB0Wp3wW8xN1KvaJoklzgvgJdlL9V+08qSS5xqwVSi/Jbe5/SpUpSjz5v/q62s9X72S5XkqqlvPnHdYNLluQgytU/SRIN6D5vrv6lK3Lx+6hh9P33f/7baCS03x748L5Krve3n+i5jIJf333Cgef+Ez2/0+DuI/UZgiAIgiAIgiAIgiAIgiAunTAdd39iEgw/U5CEaZBGX7W/PnqGh6XWu507pijhbrfrf0wpzY1dgbc5+VGMbLdbnRzb5+K67nw9Ynn53PV7oran/s733ZK5eWLp8c51d9+6pdgQ53zMj4jeQIHdGgdy7urMTyw9BE3m3/qpBdTE/+aabHeFFP5c4e+yE0t/Lk28UTXJfK+jyWLueSjIahpEN1E6zU52GEJJ314T1xtZE7ejycL3QJP5doRn3F6LJhlK4q9GeervlWiyhmp483yc0lET/xk0kSNrIj19LI7nnpT+dqTSwzkU9u01kdId1sQOo+hmcErXZ0VNzAgoP7F9gw42T0QRw/nDs1vNTeh3NUnAPOrjuMc0iWemD8z91bon4IPVbVpBEwgbDaq1YCWkcXSiHGzkHM+XWV8DuJk58yKIadKjSbQVyuwtlqPNxm1o2e6015L7WD2okfRcf9vymBRWA09oTHAyz5AG/EjDx4dkH+Es/9jTsoHwPbwA8HzRflWQZIUbQ7nZTm58Q9fk5gHMyh9cLMeajtueYfRqEknwViFdFrWshobLqu82AE1KlBSojjjiP59rXqC+zVycup5uda0A3LqVJku/YR5pbFOaeD2aBL7y4+Hs0ys8avdw6cshK2jC4ZYCiwl+ucyA5KX3hZJWYkGeKtJ90Mx7LQhZnGhomsx8g4OzOgrPuPlKOYqoJOc9mkBdOAcf2TJIlzl38T+/aikpWuFgYYXTwOqW1kxyYxUecuza49wfDnQBZlBwNV2my9nKhVi4V4sSqCBcni+DYL+ReC5y0GTtczSLLZozTxVljPGcf78miVTRHD5xwp6qavPkYFXBTJtWVliVJlVBWzhVDjrfuijC6qB1tMJ6Vc0qRmvdiBN1dq1JhJJIfshVySOa5eJLBegBNZEdTTJVay2DRAwdPmpWrlvxf+/xYNQ02YBag+sdIdbC1TNIhqL4ZVZYKKW1L2EJPF0TE82mlkECDMvdP1Xjp7GNHk1UsF7jK2FmkjPuxsNWXlpzg2kqQL0MPUM02BiMyWZS3YAbo3jRnKpm0uh3cIgx5ilNlmgWja6SGRCj+Poh2ca42po8wkFPE9yeMsmqaPKOlTetuiYQ5ZAmsccYt1rhMKi1p2qaGYcia2ay8rOCE12trcZbaWAU7ten2V5NwB2vP5gCvKk6H9oJWs0ea1GVpiYbzgb7zlp2Kz3Zw0GJOcKGP7qXVu0kdtmhQSEhDHcqCnnqCp6GzZkwWprceKI+FmWuIRAYEVR/CT3BGlYGRnawTnIueJ3otoZgQ9OTjAvWyb+JZIJjf4o8JmQnOWy5EBI1CWT5B5IuXI4hMkPmJww87d5mc9HRJEV/RbMMYLQsFJF5mUGCHqtRWVETVmuyBj29gZmUyQTr9qsVK65fghuv8y1XlRRTKFiq+tt702MqCslP+xiiPk14SxMMR94ob7LwZrD6A36WGE08ZG1pEkFRxsDU3gTPj52jGZSJ7X9dVVonOmgyg7gZ/E6mQopCEWd9YnrtaMKE1dFEhZPMGPy20Jupe9OtaJbmXi80Z5aoNbFRtYGEgpp01xDygybYSzqVDKUlJE6ZURMxCR+NoqEyuTh9BeFzNAkMqGsGI50F1N7CfVRYrcqqxRIuy3zS0AT/tWT/mw8rYbHuWvVGFNcvOVzY6QqpURY3BbMFQ1MZxaZ0ES1HeMljQ8xtTUIDHVlKESOrZpku99JBa+oV1kkuGppEqGB/Q8mgEKdzFA6KvLyQd+49SmFgtVGyMgrOt4fxdw0z6hHGYiiXtTRBnYo6c21deQGVVSmRl1bea21pMnkABz1dBOsHbox2FlVS4Iv+hJfiNFiBXzXa3hiHKKxplXVUZb5+0RCKcdqaqDsI3oS+WKRu+GNpdTCWptWxhKo5aGLpmoQST+6bcWODE5vWwQfhWMXktf6rJkChCoHNQpGVnsD3fMDVl2FD+xVtTVLuOI5oDhcry3GKu5oaXatZWXOoSuOF2BQLM/rWexZwEW+Ws4eTrWKADvDP5ku6xMEriqa1ZmB2Gpkq5nCzxAivjKGuVifTYbRWo+FuBBzZfIY1t9o1QaPD8+5AqaTn+tJaoPSLqsicRu+xleNDsALN+t1M8IIRuo6qQzMuJFQN5aFKF+FKOKbD49pqNq2m6bDi/5kwHatxr7Aqpimc7oJppkqtmxA0KbOWAfqjqbuJoDHWQSj9TFZLnUKmMR1zjFXZgJngeR3bdgI/SVnkksNRi22jZGLHaQ6xmmbdzPdNK9OtWJ61Ce2kDs5egGZQWWsbhHGS3KTrcjyxVxY6X63DZJKEaxNPs+pBalq6SWNwE2RFEPVQtFWnW9MQowg2GIXDxtlzsFBxQRYoyLV4ICALbXiGqY/Ys8rqtK22qj929roV2xkKDxcIHNFYPXOOTUupBQVBYY6SRGtjW1ZcJWo3evrJmRYjXux0B+/TiFUsFaxsynvROGyxRjJcs4ZVT7lLVh7Ue+TessxGceXxRDWhGvHQ6HZT1rA6olnnbdPcSrlfw81Kj7e6vdFDrYrDNq1RMdIq47BMnz3OykgbQ1O8FZoXp87CU+241RkBwc2RICbBqo4COtmIH7pqz4SwDvB6FpVmxXFh5T03IM2KiXXXGqyYuqoZYrzfCFFcwRbaVC2ersoZ+mraMzGHRFEEIfKeLWH28qG82NmO/FXRdrRcF+zj1vH9PhhyNmzF4vbdu2aHwXK9DKL22BCn+/UyHXqlkig3nYs0M5Q5ypsYBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQI/E/BzTiD283KlEAAAAASUVORK5CYII=)](https://leetcode.com/problems/valid-parentheses/)

![image](https://blog.kakaocdn.net/dn/3D7hu/btrOwNRT0tC/wCPMwKye3cLmhBK6DjCykK/img.png)

문제 이해 : 괄호의 짝이 맞는가 확인하는 문제 즉 열린 부호는 반드시 닫힌 부호와 같이 있어야함 없으면 False 둘이 짝이 맞으면 True

2. 필요문법: for ,  dic,  stack,  list, append, pop (cf get())

3. 문제 풀이 개요

  * dic을 정의 할때 열린괄호를 key로 정의하는 것과 닫힌 괄호를 key로 정의하는 것 두가지에 따라서 문제를 푼다.

4. Test Case
   
   ![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F1rDOa%2FbtrOw0XVIco%2FAYvy57p9TDbNBjaF2kUux1%2Fimg.png)

3-1 문제풀이(dic의 key가 열린괄호)

![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQ1C7f%2FbtrOwxhCXab%2FksOLTw0ryMfEF5J2nuKBIk%2Fimg.png)

* time complexcity: O(N)인듯
* space complexcity: O(1)

3-2 문제풀이(dic에서 닫힌 괄호가 key)

![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FpAbsK%2FbtrOwN5B51g%2FpoL9e3kS3AA4mZLNUHkYB1%2Fimg.png)

* time complexcity 동일
  
* space complexcity 동일 
  
* 하지만 닫힌 괄호를 key로 두고 푸는 것이 속도가 더 빠름 한번에 처리하기 때문에 열린 괄호를 key로 뒀을 때는 다시 저장하고 넣는 작업을 해야함 

# **카카오 멘토링 부산대**

'''
Input: s = "()"
Output: true

() [] {}
Example 2:
Input: s = "()[]{}"
Output: true


Example 3:
Input: s = "(]"
Output: false

Example 4:
s = "({})()"

- worst case
s = "((((((((((((((((((((((((((()))))))))))))))))))))))))))"
'''
#https://leetcode.com/problems/valid-parentheses/
#parentheses -> stack
#Time Complexity: O(N)
#Space Complexity: O(N)

def solve(s: str):
    stack = []

    for blanket in s:
        if blanket in ['(', '{', '[']:
            stack.append(blanket)
        else:
            if blanket is ')' and stack[-1] == '(':
                stack.pop_back()
            elif blanket is '}' and stack[-1] == '{':
                stack.pop_back()
            elif blanket is ']' and stack[-1] == '[':
                stack.pop_back()
            else:
                return false
            
    # (((((
    if len(stack) != 0: return False
    return True
    
    if len(stack) == 0: 
        return True
    elif len(stack) != 0:
        return False
        