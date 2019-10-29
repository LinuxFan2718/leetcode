def recursion(i, res):
  res.append(i)
  if i < 2:
    return
  else:
    recursion(i-1, res)

res = []
recursion(10, res)
print(res)