import Queue
import threading
import urllib2

# Called by each thread
def make_conn(q, url):
    objConn = DataBaseBigQuery('config')

    q.put( objConn.get_data_bq( qry )

theurls = ["SELECT", "INSERT"]

q = Queue.Queue()

for qry in lstQueries:
    t = threading.Thread(target=make_conn, args = (q,qry))
    t.daemon = True
    t.start()

s = q.get()
print s
