import asyncio
import json
import time
import random
import os

from bilibili_api import video
from bilibili_api import Credential
from bilibili_api import user
from bilibili_api.user import RelationType


N = 500
EVERY_PAGE = 50 # default 50?


async def main() -> None:
    random.seed()

    user_config = get_user_config()
    credential = Credential(sessdata=user_config["session_data"],
                            bili_jct=user_config["bili_jct"],
                            buvid3=user_config["buvid3"],
                            dedeuserid=user_config["dedeuserid"],
                            ac_time_value=user_config["ac_time_value"])

    u = user.User(user_config["UID"], credential=credential)

    # get following user list
    total_page_number = int(N / EVERY_PAGE)
    total_following_user_list = []
    for i in range(total_page_number):
        user_list = await u.get_followings(pn=i, ps=EVERY_PAGE)
        user_list = user_list["list"]
        # print("getting %d users" % len(user_list))
        total_following_user_list.extend(user_list)
    print("total %d users" % len(total_following_user_list))

    # unfollowing
    for following in total_following_user_list:
        try:
            await unfollow_user(following, credential)
        except Exception as e:
            # error -352
            # unfollow on browser and pass the verification
            code = getattr(e, "code", 0)
            if code == 352:
                print("=========")
                print("error 352")
                print("unfollow on browser and pass the verification")
                os.exit(1)
            time.sleep(10)
        else:
            time.sleep(random.randrange(3))


async def unfollow_user(following, credential):
    uid = int(following["mid"])
    uname = following["uname"]
    following_u = user.User(uid=uid, credential=credential)
    try:
        await following_u.modify_relation(relation=RelationType.UNSUBSCRIBE)
    except Exception as e:
        print("!!!error user %s" % uname)
        print(getattr(e, "message", repr(e)))
        raise e
    else:
        print("unfollowing " + uname)


def get_user_config():
    config_path = "user.json"
    with open(config_path) as f:
        user_config = json.load(f)
        # print(user_config)
    return user_config


if __name__ == "__main__":
    asyncio.run(main())
