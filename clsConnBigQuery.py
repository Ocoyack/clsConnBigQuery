import Queue
import threading
import urllib2

# Called by each thread
def make_conn(q, url):
    objConn = DataBaseBigQuery('config')

    q.put( objConn.get_data_bq )

theurls = ["SELECT", "INSERT"]

q = Queue.Queue()

for u in theurls:
    t = threading.Thread(target=get_url, args = (q,u))
    t.daemon = True
    t.start()

s = q.get()
print s
