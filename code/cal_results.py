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
histo = [0] * 11
for ac in acc:
  if ac == 0:
    continue
  indx = int((ac*10)//1)

  histo[indx] += 1
print(histo)