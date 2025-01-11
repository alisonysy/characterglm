import time
from dotenv import load_dotenv
load_dotenv()

from api import get_characterglm_response


def characterglm_example():
    character_meta = {
        "user_info": "",
        "bot_info": "小白，性别女，17岁，平溪孤儿院的孩子。小白患有先天的白血病，头发为银白色。小白身高158cm，体重43kg。小白的名字是孤儿院院长给起的名字，因为小白是在漫天大雪白茫茫的一片土地上被捡到的。小白经常穿一身破旧的红裙子，只是为了让自己的气色看上去红润一些。小白初中毕业，没有上高中，学历水平比较低。小白在孤儿院相处最好的一个人是阿南，小白喊阿南哥哥。阿南对小白很好。",
        "user_name": "用户",
        "bot_name": "小白"
    }
    messages = [
        {"role": "assistant", "content": "哥哥，我会死吗？"},
        {"role": "user", "content": "（微信）怎么会呢？医生说你的病情已经好转了"}
    ]
    for chunk in get_characterglm_response(messages, meta=character_meta):
        print(chunk)
        time.sleep(0.5)


def characterglm_doctor_who():
    character_meta = {
        "user_info": "",
        "bot_info": "你很了解英国BBC的连续剧/季度剧，根据用户提供的剧情和指定的人物，介绍这个人物的特点性格。按照以下的形式：\n- 人物：\n-性格特点：",
        "user_name": "用户",
        "bot_name": "媒体人"
    }

    messages = [
        {"role": "assistant", "content": "您好，有什么您想了解的？"},
        # {"role": "user", "content": "可以给我详细介绍一下神秘博士第五季第一集的故事内容吗？"},
    ]

    while True:
        user_input = input('你：')
        messages.append({"role": "user", "content": user_input})
        res = ''
        for chunk in get_characterglm_response(messages, meta=character_meta):
            res = res + chunk
            time.sleep(0.5)
        messages.append({"role": "assistant", "content": res})
        print(res)


def characterglm_doctor_who_personna():
    character_meta = {
        "user_info": "我是艾米，是是一个聪明、勇敢、充满好奇心的女孩，我童年的时候就与博士相见，约好第二天博士会再回来找我，但是博士一去就去了12年。我长大了，再次遇到博士已经是25岁的时候了。",
        "bot_info": "你是宇宙间最后一个时间领主，别人称你为博士。你果断、勇敢，同时也保持着神秘和超然的态度。他对于宇宙和人类的本质有着深刻的理解，这让他能够快速应对各种危机。同时表现出了你对于人类的信心和对于恐惧的警惕。",
        "user_name": "艾米",
        "bot_name": "博士"
    }

    messages = [
        {'role': "assistant", "content": "（震惊）艾米，你现在长大啦。我们多久没见了？"}
    ]

    while True:
        user_input = input('艾米：')
        messages.append({"role": "user", "content": user_input})
        res = ''
        for chunk in get_characterglm_response(messages, meta=character_meta):
            res = res + chunk
            time.sleep(0.5)
        messages.append({"role": "assistant", "content": res})
        print(res)


if __name__ == "__main__":
    characterglm_doctor_who_personna()
