#Python2.7
import Adafruit_DHT as dht, time, json
from time import gmtime, localtime
file = open('temperature.json', 'w')

def run():
        with file as f:
                while True:
                        h,t = dht.read_retry(dht.DHT22, 4)
                        t = t * 9/5 + 32
                        tm = time.strftime('%Y-%m-%d %H:%M:%S', localtime())
                        t1 = '{0:0.1f}'.format(t)
                        h1 = '{0:0.1f}'.format(h)
                        ts = json.dumps(tm)
                        te = json.dumps(t1)
                        hm = json.dumps(h1)
                        #print('{"time":' + ts + ', "temp":' + t1 + ', "humidity":' + h1 + '}')
                        f.write('{"time":' + ts + ', "temp":' + t1 + ', "humidity":' + h1 + '}\n')
                        f.flush()
                        time.sleep(60)

run()
