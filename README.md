Your goal is to implement a WSGI server with an HTTP wrapper without using any external
dependencies (see "Reading" section). It should listen on local port 8888 and parse GET
parameters from a URL, for any species title giving you back a JSON (it should be HTTP code 200,
also mind the appropriate 'Content-Type' header and URL encoding). Exaple using cURL might look
like this:

~$ curl http://127.0.0.1:8888/?species=Time%20Lord
{"credentials": "Rassilon"}


If it doesn't know the species passed it should return {"credentials": "Unknown"} along with
HTTP status code 404
The whole application for this task should be just a single file credentials.py.