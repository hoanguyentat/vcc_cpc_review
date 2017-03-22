#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = u"đồ lót nữ bộ lót nữ"
x = u"đồ lót"
s = s.encode("utf-8")
x = x.encode("utf-8")
if x in s:
	print "x in s"
else:
	print "x not in s"
print s
