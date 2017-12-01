import json

tweets_data_paths = [ "1103","1104","1105","1106","1107","1108","1109","1110","1112","1113","1114","1115","1116","1117","1118","1119","1120","1121","1127","1128"]

for path in tweets_data_paths:
        tweets_file = open('data/'+path+'_compress.json', "r")
        table_file = open('data/'+path+'_table',"w")
        tweets_data = []
        count = 0;
        for line in tweets_file:
            wvector=[];
            tweet = json.loads(line)
            wvector.extend((count, tweet['id_str'], tweet['user']['screen_name']))
            #print(wvector)
            count = count +1
            table_file.write(str(wvector[0])+' '+wvector[1]+' '+wvector[2]+'\n')
        print(path, 'done')