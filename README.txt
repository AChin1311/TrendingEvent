in run.sh we sequentially execute these following codes:
python3 classify.py
    -classify the compressed json file from display_text.py into 4 different categories
    -the 4 categories are sport/entertainment/disasters/holiday
    -since the data are to large, we only select "sport" for simplification
python3 txt2dic.py
    -build dictionary file by reading the output from classify.py
python3 kw_one_hoc_vector.py
    -build vector of each tweet by using output from classify.py and txt2dic.py
python3 cal_results.py
    -use kmeans clustering with cosine distance
python3 ranking.py
    -rank top tweets from kmeans
python3 DBscan.py
    -use dbscan clustering and rank the output



The folloing are all the codes we wrote:

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

