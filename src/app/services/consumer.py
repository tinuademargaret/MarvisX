import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/tinuade/Downloads/marvis-vdohmu-2777cc606436.json'
from google.cloud import pubsub_v1
from src.app.controllers.controller import Controller

controller = Controller()

project_id = "marvis-vdohmu"
subscription_name = "consumer"
timeout = 10.0  # "How long the subscriber should listen for
# messages in seconds"

subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_name}`
subscription_path = subscriber.subscription_path(
    project_id, subscription_name
)


def callback(message):
    Messages = []
    print("Received message: {}".format(message))
    Messages.append(message.data)
    message.ack()
    return Messages


def consumer():
    streaming_pull_future = subscriber.subscribe(
        subscription_path, callback=controller.run
    )
    print("Listening for messages on {}..\n".format(subscription_path))

    # result() in a future will block indefinitely if `timeout` is not set,
    # unless an exception is encountered first.
    try:
        data = streaming_pull_future.result(timeout=timeout)
        # print(data)
        # data = dict(data)
        return data
    except:  # noqa
        streaming_pull_future.cancel()


