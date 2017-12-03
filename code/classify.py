import json
from kw import features as kw_features
import numpy

if __name__ == '__main__':

  tweets_data_paths = ["1103_compress.json","1104_compress.json","1105_compress.json","1107_compress.json"] 
  # tweets_data_paths = [ "1103_compress.json","1104_compress.json","1105_compress.json",\
  # "1106_compress.json","1107_compress.json","1108_compress.json","1109_compress.json",\
  # "1110_compress.json","1112_compress.json","1113_compress.json","1114_compress.json",\
  # "1115_compress.json","1116_compress.json","1117_compress.json","1118_compress.json",\
  # "1119_compress.json","1120_compress.json","1121_compress.json","1127_compress.json",\
  # "1128_compress.json"]

  out_files = []
  li_type = ['disaster','entertainment','holiday','sport']
  for ty in li_type:
    out_files.append(open('data/'+ty+'.txt', 'w'))

  for path in tweets_data_paths:
    print("processing ", path)
    tweets_file = open('data/'+path, 'r',encoding='utf-8', errors='ignore')
    for line in tweets_file:
      try:
        tweet = json.loads(line)
        tw = tweet['text'].lower()
        s = []
        features_type = [0]*4
        for w in tw.split():
          w = w.strip('’…,….;:?!\r\b\t\'\",()[]{}|-=+*_ \n')  
          for i in range(len(li_type)):
            if w in kw_features[li_type[i]]:
              features_type[i] += 1        
          s.append(w)
        
        
        if sum(features_type) == 0:
          continue
        doc_type = numpy.argsort(features_type)[-1]
        simple_tweet = ""
        simple_tweet += tweet['id_str'] + ', '
        simple_tweet += tweet['user']['screen_name'] + ', '
        simple_tweet += path[0:4] + ', '
        simple_tweet += ' '.join(s) + '\n'
        print(simple_tweet)
        out_files[doc_type].write(simple_tweet)
        
      except:
        continue