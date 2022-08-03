from VK import VK
from pprint import pprint
from datetime import datetime

if __name__ == '__main__':
  with open('vk_data.txt', 'r') as file:
    token = file.readline().strip()
    id = file.readline().strip()
  access_token = token
  user_id = id
  vk = VK(access_token, user_id)
  answer = vk.get_photos()
  # pprint(answer['response']['items'])
  for data in answer['response']['items']:
    for key, value in data.items():
      # print(key)
      if key == 'likes':
        likes = value['count']
        # print(likes)
      elif key == 'date':
        data = datetime.utcfromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S')
        # print(data)
      elif key == 'sizes':
        for photo in value:
          if photo['type'] == "z":
            link = photo['url']
            # print(link)
