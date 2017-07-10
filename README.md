Openedoo module to upload media, like discussion attachments. curresnt status is WIP.


### Upload file ###
curl example:
```
curl -X POST \
  --data-binary '@some_file_with_image.jpg' \
  http://127.0.0.1:5000/media/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: image/jpeg' \
```


Content-type header request must match with the file mime-type, [list of mime-type](https://www.iana.org/assignments/media-types/media-types.xhtml)


### Download file ###
```
[GET] http://<hostname>/media/static/<file_name>
```
