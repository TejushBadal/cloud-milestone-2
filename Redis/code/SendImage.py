import redis        # pip install redis
import io;

ip="34.130.57.88"
r = redis.Redis(host=ip, port=6379, db=0,password='sofe4630u')

with open("SOFE4630U-MS2\Redis\code\ontarioTech.jpg", "rb") as f:
    value = f.read();
r.set('OntarioTech',value);
print('Image sent')