Openedoo module to upload media, like discussion attachments. curresnt status is WIP.


curl example:
```
curl -X POST \
  --data-binary '@some_file_with_image.jpg' \
  http://127.0.0.1:5000/media/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: image/jpeg' \
```
