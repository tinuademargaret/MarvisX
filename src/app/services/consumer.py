import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/tinuade/Downloads/marvis-vdohmu-2777cc606436.json'
from google.cloud import pubsub_v1
from src.app.controllers.controller import Controller

controller = Controller()

project_id = "marvis-vdohmu"
subscription_name = "consumer"
timeout = 10.0  # "How long the subscriber should listen for
# messages in seconds"
#
subscriber = pubsub_v1.SubscriberClient()
# # The `subscription_path` method creates a fully qualified identifier
# # in the form `projects/{project_id}/subscriptions/{subscription_name}`
# subscription_path = subscriber.subscription_path(
#     project_id, subscription_name
# )
# print("Listening for messages on {}..\n".format(subscription_path))
# streaming_pull_future = subscriber.subscribe(
#         subscription_path, callback=controller.run
#     )
# print("messages recieved")

# try:
# /    message = streaming_pull_future.result(timeout=timeout)
#    / print(message)
#     /data = dict(data)
# except:  # noqa
#     streaming_pull_future.cancel()



#
#
def consumer_listener():
    print('i got here 1')
    subscription_path = subscriber.subscription_path(
        project_id, subscription_name
    )
    streaming_pull_future = subscriber.subscribe(
        subscription_path, callback=controller.run
    )

    print("Listening for messages on {}..\n".format(subscription_path))

    # result() in a future will block indefinitely if `timeout` is not set,
    # unless an exception is encountered first.
    try:
        message = streaming_pull_future.result(timeout=timeout)
        # print('i got here 2')
        # print(data)
        # data = dict(data)
        return message
    except:  # noqa
        streaming_pull_future.cancel()


