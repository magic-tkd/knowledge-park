# -*- coding: utf-8 -*-
# 用微软 Xiaoxiao 神经女声批量生成拼音教学音频
# 关键：TTS 不认裸拼音字母，全部改用对应汉字，保证读成中文而非英文
import asyncio
import os

import edge_tts

VOICE = "zh-CN-XiaoxiaoNeural"
OUT_DIR = os.path.join(os.path.dirname(__file__), "audio")

# (输出文件名, 用于朗读的汉字) —— 韵母 24 个
finals = [
    ("a.mp3", "啊"), ("o.mp3", "哦"), ("e.mp3", "鹅"),
    ("i.mp3", "衣"), ("u.mp3", "乌"), ("v.mp3", "迂"),
    ("ai.mp3", "爱"), ("ei.mp3", "欸"), ("ui.mp3", "威"),
    ("ao.mp3", "熬"), ("ou.mp3", "欧"), ("iu.mp3", "忧"),
    ("ie.mp3", "耶"), ("ve.mp3", "约"), ("er.mp3", "儿"),
    ("an.mp3", "安"), ("en.mp3", "恩"), ("in.mp3", "因"),
    ("un.mp3", "温"), ("vn.mp3", "晕"),
    ("ang.mp3", "昂"), ("eng.mp3", "鞥"), ("ing.mp3", "英"),
    ("ong.mp3", "翁"),
]

# (输出文件名, 用于朗读的汉字) —— 题库音节 20 个（带声调，用现成汉字）
syllables = [
    ("ma1.mp3", "妈"), ("ba4.mp3", "爸"), ("mi3.mp3", "米"),
    ("hua1.mp3", "花"), ("ge1.mp3", "歌"), ("di4.mp3", "地"),
    ("shu1.mp3", "书"), ("shui3.mp3", "水"), ("huo3.mp3", "火"),
    ("yu2.mp3", "鱼"), ("che1.mp3", "车"), ("niao3.mp3", "鸟"),
    ("yue4.mp3", "月"), ("feng1.mp3", "风"), ("xue3.mp3", "雪"),
    ("he2.mp3", "河"), ("cao3.mp3", "草"), ("xing1.mp3", "星"),
    ("yang2.mp3", "羊"), ("niu2.mp3", "牛"),
]


async def gen_one(filename, text):
    path = os.path.join(OUT_DIR, filename)
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(path)
    return filename


async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    tasks = [gen_one(f, t) for f, t in (finals + syllables)]
    done = await asyncio.gather(*tasks)
    print("完成生成 %d 个文件" % len(done))


if __name__ == "__main__":
    asyncio.run(main())
