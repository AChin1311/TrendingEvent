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

  ps = PorterStemmer()
  tweets_data_paths = ["holiday.txt"] 

  stopset = set(stop_ls)
  stopWords = set(stopwords.words('english'))

  docLabels = []
  data = []
  month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  
  for path in tweets_data_paths:
    tweets_file = open('data/'+path, 'r',encoding='utf-8', errors='ignore')
    for line in tweets_file:
      try:
        line_list = line.split(',')       
        text_data = []
        for w in line_list[3]:
          w = ps.stem(w)
          if w in stopWords:
            continue
          if w in stopset:
            continue
          if w in kw_features['date']:
            w = w.split('/')[0]
            w = month[int(w)-1]
          text_data.append(w)
        data.append(text_data)
        docLabels.append(line_list[0])

      except:
        continue

  it = LabeledLineSentence(data, docLabels)
  print(len(data))
  model = gensim.models.Doc2Vec(size=100, min_count=0, alpha=0.025, min_alpha=0.025)
  model.build_vocab(it)
  #print(model.wv.vocab)
  #training of model
  print("train")
  model.train(it, total_examples=model.corpus_count, epochs=100, start_alpha=0.025)

 
  model.save('data/doc2vec_txt.model')

  print('model saved')

