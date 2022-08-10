# -*- coding: utf-8 -*-
# @Time  : 2022/8/8 10:45 PM
# Author : 拒绝内卷的小测试

import pytest
from testcases.bd_fy import bd_fy
from testcases.yd_fy import yd_fy

# 断言查询出的响应结果相同
@pytest.mark.parametrize("word", ["测试"])
def test_fy_001(word):
    bd = bd_fy(word)
    yd = yd_fy(word)
    assert bd == yd, f"百度翻译的结果为{bd}, 有道翻译的结果为{yd}"


if __name__ == '__main__':
    pytest.main()