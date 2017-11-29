import json
import pandas as pd
import sys
import time
from kw import features as kw_features


def compress(tw_d):
    return json.dumps(tw_d) + '\n'    

if __name__ == '__main__':

    tweets_data_path = sys.argv[1]

    tweets_data = []
    tweets_text = []
    tweets_file = open(tweets_data_path, "r")
    total_msg = 0
    vectors = []
    with open(sys.argv[1].split('.')[0] + '_compress.json' , 'w') as f:
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tw_d = tweet
                tw = tweet['text'].lower()

                li_type = ['disaster','entertainment','holiday','sport']
                li_details = ['date','month','action','price','time','logistics','location']
                features_type ={}
                features_details ={}
                for l in li_type:
                    features_type[l] = 0
                for l in li_details:
                    features_details[l] = 0

                for w in tw.split():
                    for l in li_type:
                        if w in kw_features[l]:
                            features_type[l] += 1
                    for l in li_details:
                        if w in kw_features[l]:
                            features_details[l] += 1

                tmp_type = []
                tmp_deatails = []
                for l in features_type:
                    tmp_type.append(features_type[l])
                for l in features_details:
                    tmp_deatails.append(features_details[l])
                if sum(tmp_type) == 0 or sum(tmp_deatails) == 0:
                    continue
                vectors.append(tmp_type + tmp_deatails)
                print(tmp_type + tmp_deatails)
                f.write(compress(tw_d))
                total_msg += 1

            except:
                continue

    print("Total Msg:")
    print(total_msg)

