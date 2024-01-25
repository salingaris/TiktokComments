##########################################################################################################
import asyncio
from tkinter.messagebox import WARNING 
from TikTokLive import TikTokLiveClient
from TikTokLive.client.base import LiveNotFound 
from TikTokLive.types.events import CommentEvent
logo="""\

    /^\    /^\
    {  O}  {  O}
     \ /    \ /
     //     //       _------_
    //     //     ./~        ~-_
   / ~----~/     /              \
 /         :   ./       _---_    ~-
|  \________) :       /~     ~\   |
|        /    |      |  :~~\  |   |
|       |     |      |  \___-~    |
|        \ __/`^\______\.        ./
 \                     ~-______-~\.
 .|                                ~-_
/_____________________________________~~____
salingaris
"""
async def main(client: TikTokLiveClient):
        while not client.connected:
            try:
                await client.start()
            except LiveNotFound:
                WARNING(f"User `@{client.unique_id}` seems to be offline, retrying after 1 minute...")
                await asyncio.sleep(60)
client:TikTokLiveClient = TikTokLiveClient(unique_id="USER_ID")  #USER_ID=www.tiktok.com/@?(without @)
@client.on("comment")
async def on_connect(event:CommentEvent):
 print(f"(event.user) -> {event.comment}")
if __name__ == '__main__':
   client.run()
