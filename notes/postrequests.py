import requests

user_params = {
    'token': 'user_keyyy',
    'username': 'boss0123',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
pixela_endpt = 'https://pixe.la/v1/users'
#
# response = requests.post(url='https://pixe.la/v1/users', json=user_params)
# print(response.text)
# response.raise_for_status()  # to get text use response.text

# graph_params = {
#     'id': "a23",
#     'name': 'Gaming Hours',
#     'unit': 'min',
#     'type': 'float',
#     'color': 'momiji',
#
# }
#
# headers = {
#     'X-USER-TOKEN': user_params['token']
#
# }
#
# response = requests.post(url=f"{pixela_endpt}/{user_params['username']}/graphs", json=graph_params, headers=headers)
# print(response.text)
# response.raise_for_status()
