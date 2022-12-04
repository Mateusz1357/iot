from pm50003 import PMS5003
import requests
import json
from datetime import datetime 
from datetime import timedelta
import botocore
import botocore.session
from aws_secretsmanager_caching import SecretCache,SecretCacheConfig



def get_secret(secret_name)

  client = botocore.session.get_session().create_client(‘secretsmanager’)
  cache_config = SecretCacheConfig()
  cache - SecretCache(config=cache_config, client = client)
  secret = cache.get_secret_string(secret_name’)
  return secret

pm5003 = PM5003(
device=’dev/serial0’,
baudrate=9600,
pin_enable=22,
pin_reset=27
)

try:
  while True:
    now = datetime.utcnow()+timedelta(hours=1)
    data = pms5003.read()
    url = “https;//spaliny-backedn.onrender.com/api/add/measure”
    headers = {‘Content-type:’application/json’)
    data_obj=
    {
    DeviceCode: get_secret("DeviceCode")
    "pm1_0_particles”:data.data[0],
    “pm2_5_particles”:data.data[1],
    “pm10_particles”:data.data[2],
    “pm1_0_atmos”:data.data[3],
    “pm2_5_atmos”:data.data[4],
    “pm110_atmos”:data.data[5],
    “air_0_3”:data.data[6]
    “air_0_5”:data.data[7]
    “air_1_0”:data.data[8]
    “air_2_5”:data.data[9]
    “air_5_0”:data.data[10]
    “air_10”:data.data[11]
    }
    r = requests.post(url, data=json.dumps(data_obj),headers=headers)

except KeyboardInterrupt:
pass
