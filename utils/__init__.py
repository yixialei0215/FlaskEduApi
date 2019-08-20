from redis import Redis

rd = Redis(host='10.36.174.23',
           db=4,
           decode_responses=True)
