# Bilibili 批量取关脚本

## Start

### Configuration

```bash
cp template.json user.json
```

参考 [credential 获取方式](https://nemo2011.github.io/bilibili-api/#/get-credential)

修改 `bili.py` 的 `N` 为想要取关的数量（以最近关注排序）

### Dependency

```bash
pip install bilibili-api-python
```

### Run

```bash
python3 bili.py
```

## Reference

* https://pypi.org/project/bilibili-api-python/
* https://nemo2011.github.io/bilibili-api/#/get-credential
* https://nemo2011.github.io/bilibili-api/#/modules/user?id=async-def-get_followings
* https://nemo2011.github.io/bilibili-api/#/examples/user?id=%e7%a4%ba%e4%be%8b%ef%bc%9a%e7%a7%bb%e9%99%a4%e6%89%80%e6%9c%89%e7%b2%89%e4%b8%9d
* https://im.salty.fish/index.php/archives/revengr-bilibili-352.html
