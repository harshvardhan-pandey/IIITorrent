import functions_framework
from google.cloud import storage
from time import sleep
import os


@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    request_json = request.get_json(silent=True)
    magnet_link = request_json["magnet"]
    print(magnet_link)

    storage_client = storage.Client()
    bucket = storage_client.get_bucket("iiitorrent")

    os.makedirs("behera", exist_ok=True)
    for i in range(10):
        filepath = f"behera/ok{i}.txt"
        with open(filepath, "w") as f:
            f.write("random text from i = {i}")
        blob = bucket.blob(filepath)
        blob.upload_from_filename(filepath)
        sleep(1)
        os.remove(filepath)

    return "test!"
