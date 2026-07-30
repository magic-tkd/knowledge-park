# -*- coding: utf-8 -*-
# 用微软 Aria 英文神经嗓音批量生成英语启蒙单词音频
# 解决浏览器 TTS 设备依赖、语速过快、发音不标准的问题（与拼音音频同一思路）
import asyncio
import os

import edge_tts

VOICE = "en-US-AriaNeural"
RATE = "-10%"  # 比正常稍慢，幼儿更易听清
OUT_DIR = os.path.join(os.path.dirname(__file__), "audio", "en")

WORDS = [
    "cat", "dog", "rabbit", "cow", "pig", "fish", "bird", "elephant", "lion", "bear",
    "apple", "banana", "orange", "grape", "strawberry", "watermelon", "carrot", "tomato", "pear", "peach",
    "red", "blue", "yellow", "green",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "mom", "dad", "baby", "grandma", "grandpa", "brother", "sister",
    "eye", "ear", "nose", "mouth", "hand", "foot",
    "ball", "doll", "teddy", "balloon", "kite", "robot",
    "car", "bus", "train", "bike", "boat", "plane", "rocket",
]


async def gen_one(word):
    path = os.path.join(OUT_DIR, word + ".mp3")
    communicate = edge_tts.Communicate(word, VOICE, rate=RATE)
    await communicate.save(path)
    return word


async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    done = await asyncio.gather(*[gen_one(w) for w in WORDS])
    print("完成生成 %d 个英文单词音频" % len(done))


if __name__ == "__main__":
    asyncio.run(main())
