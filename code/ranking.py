import numpy

if __name__ == '__main__':

    with open("../data/kmeans-400.txt", 'r') as f:
      content = f.readlines()
    f.close()

    dic = {}
    tweet = {}
    for l in content:
      if l[0] != ',':
        text = l.split(',')
        #print(l)
        tweet[text[1]] = l
        #print(text[1])
        correct = text[0]
        label = text[1]
        if label not in dic:
          dic[label] = []
        dic[label].append(int(correct))

    point = [0] * 400
    for d in dic:
      point[int(d)] = sum(dic[d])
    #print(point)
    vals = numpy.array(point)
    sort_index = numpy.argsort(vals)
    #print(sort_index)
    for i in range(10):
        print(sort_index[len(vals)-i-1],":",vals[sort_index[len(vals)-i-1]])
        #print(tweet[str(sort_index[len(vals)-i-1])])   

    with open("../data/"+"sport_ranking_result.txt", 'w') as f:
        for i in range(20):
            f.write(str(i+1)+ ". "+str(vals[sort_index[len(vals)-i-1]]) + ", ")
            text = tweet[str(sort_index[len(vals)-i-1])].split(',')
            f.write(tweet[str(sort_index[len(vals)-i-1])])
            f.write("\n")