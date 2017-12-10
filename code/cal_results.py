import matplotlib.pyplot as plt
import numpy as np
#import plotly.plotly as py


with open("kmeans-400.txt", 'r') as f:
  content = f.readlines()
f.close()

dic = {}
for l in content:
  if l[0] != ',':
    text = l.split(',')
    correct = text[0]
    label = text[1]
    if label not in dic:
      dic[label] = []
    dic[label].append(int(correct))

acc = [0] * 400
for d in dic:
  acc[int(d)] = sum(dic[d])/len(dic[d])
print(sum(acc)/len(dic))
print(acc)


accc = []
for ac in acc:
  if ac==0:
    continue

  accc.append(ac)
plt.hist(accc)
plt.ylabel('Appearance')
plt.show()



