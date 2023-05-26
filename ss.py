import datetime
import platform
import socket

hostname = str(socket.gethostname())
os = str(platform.system())
now = str(datetime.datetime.now())


fruom = str("""
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
""")

print(fruom)
