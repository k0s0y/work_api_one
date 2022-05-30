import requests
from Token import TOKEN


class YaUploader:
    token = TOKEN

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, disc_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers(self=YaUploader)
        params = {'path': disc_file_path, 'overwrite': 'true'}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disc(self, disc_file_path, file_name):
        href = self.get_upload_link(self=YaUploader, disc_file_path=disc_file_path).get('href', '')
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')
