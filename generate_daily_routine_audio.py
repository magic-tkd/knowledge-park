# -*- coding: utf-8 -*-
# 生成 "Daily Routine" 原创日常场景句绘本的英文音频
# 原创句子零版权，用微软 Aria 神经嗓音预生成，句子比单词再慢一点更易跟读
import asyncio
import os

import edge_tts

VOICE = "en-US-AriaNeural"
RATE = "-12%"  # 句子较长，比单词(-10%)再慢一点
OUT_DIR = os.path.join(os.path.dirname(__file__), "audio", "books", "daily-routine")

# (文件名, 英文句子)
SENTENCES = [
    ("page01", "Wake up, little one."),
    ("page02", "It is a new day."),
    ("page03", "Stretch your arms."),
    ("page04", "Let us get up."),
    ("page05", "Wash your hands."),
    ("page06", "Time to eat."),
    ("page07", "Use your spoon."),
    ("page08", "Chew slowly."),
    ("page09", "Yummy!"),
    ("page10", "All done."),
    ("page11", "Take a bath."),
    ("page12", "Put on your pajamas."),
    ("page13", "Hug your bear."),
    ("page14", "Good night."),
    ("page15", "Sweet dreams."),
]


async def gen_one(fname, text):
    path = os.path.join(OUT_DIR, fname + ".mp3")
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
    await communicate.save(path)
    return fname


async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    done = await asyncio.gather(*[gen_one(f, t) for f, t in SENTENCES])
    print("完成生成 %d 句 Daily Routine 音频" % len(done))


if __name__ == "__main__":
    asyncio.run(main())
