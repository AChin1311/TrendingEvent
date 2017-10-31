#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys
import keys

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        with open(sys.argv[1], 'a') as f:
          f.write(data)
          print('write')
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['LA', 'Los Angeles', 'California', 'Agoura Hills','Alhambra','Arcadia','Artesia','Avalon','Azusa','Baldwin Park','Bell','Bell Gardens','Bellflower','Beverly Hills','Bradbury','Burbank','Calabasas','Carson','Cerritos','Claremont','Commerce','Compton','Covina','Cudahy','Culver City','Diamond Bar','Downey','Duarte','El Monte','El Segundo','Gardena','Glendale','Glendora','Hawaiian Gardens','Hawthorne','Hermosa Beach','Hidden Hills','Huntington Park','Industry','Inglewood','Irwindale','La Cañada Flintridge','La Habra Heights','La Mirada','La Puente','La Verne','Lakewood','Lancaster','Lawndale','Lomita','Long Beach','Los Angeles','Lynwood','Malibu','Manhattan Beach','Maywood','Monrovia','Montebello','Monterey Park','Norwalk','Palmdale','Palos Verdes Estates','Paramount','Pasadena','Pico Rivera','Pomona','Rancho Palos Verdes','Redondo Beach','Rolling Hills','Rolling Hills Estates','Rosemead','San Dimas','San Fernando','San Gabriel','San Marino','Santa Clarita','Santa Fe Springs','Santa Monica','Sierra Madre','Signal Hill','South El Monte','South Gate','South Pasadena','Temple City','Torrance','Vernon','Walnut','West Covina','West Hollywood','Westlake Village','Whittier'], languages=['en'])