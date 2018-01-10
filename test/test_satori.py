import sys
import time
from satori.rtm.client import make_client, SubscriptionMode


class SubscriptionObserver(object):

    # Called when the subscription is established.
    def on_enter_subscribed(self):
        print('Subscribed to the channel')

    # This callback allows us to observe incoming messages
    def on_subscription_data(self, data):
        for message in data['messages']:
            print('Animal is received:', message)

    def on_enter_failed(self, reason):
        print('Subscription failed, reason:', reason)
        sys.exit(1)


def main():
    satori_config = {
        "endpoint": "",
        "appkey": "",
        "channel": "discovery_staging.bievent",
        "sub_id": "discovery_staging_bievent"
    }
    stream_filter = "SELECT * FROM `disocovery_staging.bievent`"

    subscription_observer = SubscriptionObserver()

    # init RTM client
    with make_client(endpoint=satori_config['endpoint'], appkey=satori_config['appkey']) as client:
        print 'Connected to Satori RTM!'
        print "Running Stream SQL: {}".format(stream_filter)
        client.subscribe(
            satori_config['sub_id'],
            SubscriptionMode.SIMPLE,
            subscription_observer,
            args={'filter': stream_filter}
        )
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass

    sys.exit(0)


if __name__ == '__main__':
    main()
