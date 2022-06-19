from pypresence import Presence
import time

while True:
    rpc = Presence("your-id")
    rpc.connect()
    rpc.update(state="msg1", details='msg2', large_image="image-name",small_image="image-name",start=time.time(),buttons=[{"label":"Text", "url":"any-link"}] )
