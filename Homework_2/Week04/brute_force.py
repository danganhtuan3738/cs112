
def solution(str):
    n = len(str)
    result = ''
    for i in range(n):
        for j in range(i, n):
            if str[i] == str[j]:
              s = str[i:j+1]
              if (s == s[::-1] and len(s) > len(result)):
                  result = s
    return len(result), result

try:
    str = input()
except:
    str = ''
print(solution(str))