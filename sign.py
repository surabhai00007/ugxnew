import requests

# Target URL
u = "https://media-cdn.classplusapp.com/720820/lc/nr8jn-3870135/master.m3u8"
token = "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MTI4OTk4NTc1LCJvcmdJZCI6Mzc5NzI3LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTYyNjA3MzI5MjMiLCJuYW1lIjoiQWJoaXNoZWsgZGhydXciLCJlbWFpbCI6bnVsbCwiaXNJbnRlcm5hdGlvbmFsIjowLCJkZWZhdWx0TGFuZ3VhZ2UiOiJFTiIsImNvdW50cnlDb2RlIjoiSU4iLCJjb3VudHJ5SVNPIjoiOTEiLCJ0aW1lem9uZSI6IkdNVCs1OjMwIiwiaXNEaXkiOnRydWUsIm9yZ0NvZGUiOiJyZnFuYiIsImlzRGl5U3ViYWRtaW4iOjAsImZpbmdlcnByaW50SWQiOiI4NDNkNDUzMjBkMzliNzhlZjU2Y2ViZTBmZmE4MDM4NiIsImlhdCI6MTc0OTczMTkxNCwiZXhwIjoxNzUwMzM2NzE0fQ.XpCY1oYbKLAUxDmjdmMkJtepLTOpavtj5eAe3aGuRTupaDVKdCQvwEN1PIvLu_Te"

# API request headers
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip',
    'accept-language': 'EN',
    'api-version': '35',
    'app-version': '1.4.73.2',
    'build-number': '35',
    'connection': 'Keep-Alive',
    'content-type': 'application/json',
    'device-details': 'Xiaomi_Redmi 7_SDK-32',
    'device-id': 'c28d3cb16bbdac01',
    'host': 'api.classplusapp.com',
    'region': 'IN',
    'user-agent': 'Mobile-Android',
    'webengage-luid': '00000187-6fe4-5d41-a530-26186858be4c',
    'x-access-token': token
}


# Send API request
r = requests.get(
    f"https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={u}",
    headers=headers
)

# Output
print("Response:")
print(r.json())
