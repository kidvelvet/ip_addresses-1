import requests

api_key = 'd5645a210a5065b0df6a2851db470f2a771ea67ce0975d39db1b3d31'

filename = 'addresses.txt'

# open the file
file_handle = open(filename, 'r')

# read the contents of the file
file_content = file_handle.read()

# split the text of the file at each line, which
# should correspond to an IP address.
file_lines = file_content.split('\n')

for ip in file_lines:
    api_url = f'https://api.ipdata.co/{ip}?api-key={api_key}'
    response = requests.get(api_url)

    if response.ok:
        print(response.json())

# Make sure to close the file!
file_handle.close()