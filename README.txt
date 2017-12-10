streaming.py - streamiing data from twitter using "date" and "disaster" in kw.py
parse.py- try to split json 
table.py - table for id_str, user screen name
kw.py - data & disaster for streaming, detail and types for compress
display_text.py - compress the json according to kw.py

=======attempt 1=======
build_vocab.py - build the dictionary with whole data set (length over 7000)

happy_train_friend.py - covert each tweet into len 7000+ dimension feature vector base on dictionary
kmeans.py - didn't work

=======attempt 2========
train_doc2vec.py - word embedding

=======attempt 3=======
baseline.py - group into four category, then cluster by date 
classify.py - group compress.json files into 4 txt

=======attempt 3=======
txt2dic.py - build dictionary for each txt
kw_one_hoc_vector.py - covert tweet into feature vector according to correspond dictionary, store the result
kmeans_cos.py - didn't use
kmeanscosine.py - for kmeans

get sport_result.txt
sort sport_result.txt into 400_kmeans.txt manually

cal_result.py - calculate purity and plot histogram


=======attemp 4=======
ranking.py - get top 20 tweets
DBscan.py - 


text_kmeans.py - kmeans
train_text_vector.py - ???

