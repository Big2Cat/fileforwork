#!/usr/bin/env python
# encoding: utf-8
import re
aa = '中国大唐集团新能源股份有限公司2016年公开发行绿色公司债券（第二期）(G16唐新3)'
bb = re.sub('\(.*?\)$','',aa)
print bb
