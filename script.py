from pypresence import Presence
import time

while True:
    rpc = Presence("987863377462304829")
    rpc.connect()
    rpc.update(state="meu server ai ó.", details='python é mo legal :D', large_image="static2",small_image="static2",start=time.time(),buttons=[{"label":"Discord Server :D", "url":"https://discord.gg/JGcRUhHRkK"}] )