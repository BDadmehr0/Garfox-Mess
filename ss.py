import datetime
import platform
import socket

hostname = socket.gethostname()
print("Hostname:", hostname)

os = platform.system()
print(os)

now = datetime.datetime.now()
print(now)

fruom = """
{
    "name":"Garfox-mess",
    "version":"0.0.1",
    "production-date":"2023-05-26",
    "last-update":"{}",

    "system" : {
        "OS":"{}",
        "host":"{}"
    }
}
"""