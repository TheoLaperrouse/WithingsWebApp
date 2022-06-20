import os
import time
from dotenv import load_dotenv
from withings_api import WithingsAuth, WithingsApi, AuthScope
from withings_api.common import get_measure_value, MeasureType


load_dotenv()

auth = WithingsAuth(
    client_id=os.getenv('CLIENT_ID'),
    consumer_secret=os.getenv('CONSUMER_SECRET'),
    callback_uri='http://0.0.0.0:5000/',
    mode='demo',
    scope=(
        AuthScope.USER_ACTIVITY,
        AuthScope.USER_METRICS,
        AuthScope.USER_INFO,
        AuthScope.USER_SLEEP_EVENTS,
    )
)

authorize_url = auth.get_authorize_url()
print(authorize_url)
oauth_verifier = input('Please enter your oauth_verifier: ')
credentials = auth.get_credentials(oauth_verifier)

api = WithingsApi(credentials)

while True:
    meas_result = api.measure_get_meas()
    weight_or_none = get_measure_value(meas_result, with_measure_type=MeasureType.WEIGHT)
    print(weight_or_none)
    time.sleep(10)