import threading
import time
import sys
import requests
import json

def getThreadId():
   """Returns OS thread id - Specific to Linux"""
   return libc.syscall(SYS_gettid)

def make_request():
	addr='http://18.188.145.20'
	payload = {'url':'http://photos.petfinder.com/photos/pets/40708150/1/?bust=1516322759&width=500&-x.jpg'}
	header = {'content-type':'application/json'}
	response = json.loads(requests.post(addr, data=json.dumps(payload), headers=header).text)
	# response=json.loads(r.text)

	if response['breed']!='Basenji':
		print("TID #" +str(threading.currentThread())+ "INCORRECT")
	else:
		print("TID #" +str(threading.currentThread())+ "CORRECT")

def main():
	if len(sys.argv)!=2:
		print("Enter the number of threads to test with")
		return -1
	else:
		NUM_THREADS=int(sys.argv[1])
		t0 = time.time()
		pool = []
		for i in range(NUM_THREADS):
			t = threading.Thread(target=make_request)
			t.start()
			pool.append(t)

		for t in pool:
			t.join()
		t1=time.time()
		print("Testing with " +str(NUM_THREADS)+ " concurrent users took " +str(t1-t0)+ " seconds")
if __name__ == "__main__":
	main()