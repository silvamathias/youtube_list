# %%
import pytube as yt
import httpx as hx
import asyncio as io
import datetime as dt

dt_0 = dt.datetime.now()

print(dt_0)

# %%
yt_list = yt.Playlist('https://www.youtube.com/watch?v=eVp_PnbIlAU&list=PLOQgLBuj2-3KwvqC1XXJT8LLTNTzmcKP_')

# %% [markdown]
# inicio do io

# %%
async def get_stream(url):
    #async with hx.AsyncClient(url)
    video = yt.YouTube(url)
    video_list = video.streams.filter(only_audio=True)
    dw = video_list.last()
    await dw.download()


# %%

async def core():
    url_io = io.create_task(*[get_stream(mp3) for mp3 in yt_list])
    await url_io
'''

async def core():
    t0 = io.create_task(get_stream(yt_list[0]))
    t1 = io.create_task(get_stream(yt_list[1]))
    t2 = io.create_task(get_stream(yt_list[2]))

    await t0
    await t1
    await t2
'''

# %%
io.run(core())

'''
for url in yt_list:
    io.run(get_stream(url))
'''
dt_1 = dt.datetime.now()
dt_1.st
print(dt_1)

dt_n = dt_1 - dt_0
dt_n.seconds
