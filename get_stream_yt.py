# %%
import pytube as yt
import httpx as hx
import asyncio as io
import datetime as dt

dt_0 = dt.datetime.now()

print(dt_0)

# %%
yt_list = yt.Playlist('https://www.youtube.com/watch?v=_-G_7y9wAxM&list=PLpB8v4o_VMVFaTzgNfNCAYRQlC5cl8kp2')

# %% [markdown]
# inicio do io

# %%
async def get_stream(url):
    #async with hx.AsyncClient(url)
    video = yt.YouTube(url)
    video_list = video.streams.filter(only_audio=True)
    dw = video_list.last().download()
    dw.download()


# %%
'''
async def core():
    url_io = io.create_task(
    *[get_stream(mp3) for mp3 in yt_list]
    )
    await url_io
'''

async def core():
    t0 = io.create_task(get_stream(yt_list[0]))
    t1 = io.create_task(get_stream(yt_list[1]))
    t2 = io.create_task(get_stream(yt_list[2]))
    t3 = io.create_task(get_stream(yt_list[3]))
    t4 = io.create_task(get_stream(yt_list[4]))
    t5 = io.create_task(get_stream(yt_list[5]))
    t6 = io.create_task(get_stream(yt_list[6]))
    t7 = io.create_task(get_stream(yt_list[7]))
    t8 = io.create_task(get_stream(yt_list[8]))
    t9 = io.create_task(get_stream(yt_list[9]))
    t10 = io.create_task(get_stream(yt_list[10]))

    await t0
    await t1
    await t2
    await t3
    await t4
    await t5
    await t6
    await t7
    await t8
    await t9
    await t10

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
