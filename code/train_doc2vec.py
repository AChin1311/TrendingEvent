import gensim
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from os import listdir
from os.path import isfile, join
import json
from kw import features as kw_features
from stoplist import stop_ls
from nltk.stem import PorterStemmer

class LabeledLineSentence(object):
  def __init__(self, doc_list, labels_list):
    self.labels_list = labels_list
    self.doc_list = doc_list
  def __iter__(self):
    for idx, doc in enumerate(self.doc_list):
      yield gensim.models.doc2vec.LabeledSentence(doc, [self.labels_list[idx]])

if __name__ == '__main__':
  #now create a list that contains the name of all the text file in your data #folder
  tweets_data_paths = ["1103_compress.json","1104_compress.json","1105_compress.json"] 
  # tweets_data_paths = [ "1103_compress.json","1104_compress.json","1105_compress.json",\
  # "1106_compress.json","1107_compress.json","1108_compress.json","1109_compress.json",\
  # "1110_compress.json","1112_compress.json","1113_compress.json","1114_compress.json",\
  # "1115_compress.json","1116_compress.json","1117_compress.json","1118_compress.json",\
  # "1119_compress.json","1120_compress.json","1121_compress.json","1127_compress.json",\
  # "1128_compress.json"]
  ps = PorterStemmer()
  docLabels = []
  data = []
  disaster = 0
  stopset = set(stop_ls)
  stopWords = set(stopwords.words('english'))
  for path in tweets_data_paths:
    print("processing ", path)

    tweets_file = open('data/'+path, 'r',encoding='utf-8', errors='ignore')
    for line in tweets_file:
      try:
        tweet = json.loads(line)
        tw = tweet['text'].lower()
        s = []
        for w in tw.split():
            w = w.strip('’…,.;:?!\r\b\t\'\",()[]{}|-=+*_ \n')
            w = ps.stem(w)
            if w in stopWords:
                continue
            if w in stopset:
                continue
            s.append(w)
        
        flag = False
        for w in s:
          if w in kw_features['disaster']:
            disaster += 1
            flag = True
            break
        if flag and disaster%10 != 0:
          continue
        data.append(tw.split())
        docLabels.append(tweet['id_str'])      
      except:
        continue
    print(len(data))

  tokenizer = RegexpTokenizer(' ')
  stopword_set = set(stopwords.words('english'))
  
  # def nlp_clean(data):
  #   new_data = []
  #   for d in data:
  #     new_str = d.lower()
  #     dlist = tokenizer.tokenize(new_str)
  #     dlist = list(set(dlist).difference(stopword_set))
  #     new_data.append(dlist)
  #   return new_data
  
  # data = nlp_clean(data)

  it = LabeledLineSentence(data, docLabels)
  print(len(data))
  model = gensim.models.Doc2Vec(size=100, min_count=0, alpha=0.02, min_alpha=0.02)
  model.build_vocab(it)
  #print(model.wv.vocab)
  #training of model
  print("train")


  model.train(it, total_examples=model.corpus_count, epochs=200, start_alpha=0.02)
 
  model.save('data/doc2vec.model')

  print('model saved')
