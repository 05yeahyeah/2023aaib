a = 1234567890
b = 3394723097

def gcd(a, b):
  print(a, b)
  if a==0: return b #終止條件，遇到0的話，另一邊是答案
  if b==0: return a #終止條件，遇到0的話，另一邊是答案
  return gcd(b, a%b) #函式呼叫函式 一直做到成功為止

ans = gcd(a, b)
print(ans)