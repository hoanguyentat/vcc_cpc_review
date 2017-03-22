#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import re
import sys
import HTMLParser
from nltk import ngrams

reload(sys)
sys.setdefaultencoding('utf-8')

sex_words = [
			u"nâng ngực", 	u"nâng hông",
			u"nâng mông", 	u"săn chắc ngực",
			u"săn chắc vùng ngực", 	u"nội tiết tố nữ",
			u"mặt nạ ngực",	u"kem ngực",
			u"corset",	u" bra ",	u"áo ôm tạo dáng",
			u"bộ quần áo ngủ",	u"áo ngủ",
			u"đồ ngủ nữ",	u"vệ sinh phụ nữ",
			u"đồ bơi",	u"bộ bơi",
			u"áo tắm",	u"quần áo bơi",
			u"áo bơi nữ",	u"áo bơi một mảnh",
			u"áo bơi 1 mảnh",	u"quần bơi",
			u"bikini",	u"nội y",
			u"lót nữ",	u"đồ lót",
			u"lót nam",	u"quần nam form ngắn",
			u"quần đùi nam bó",	u"quần lót",
			u"đồ lót",	u"quần brief",
			u"quần boxer",	u"quần sịp",
			u"quần chip",	u"quần gen",
			u"quần ren",	u"quần tất",
			u"quần tàng hình",	u"quần tạo hình",
			u"quần ôm tạo dáng",	u"quần định hình",
			u"quần bà bầu",	u"quần bầu",
			u"nịt bụng",	u"gợi cảm",
			u"áo lót",	u"quần lọt khe",
			u"áo ngực",	u"áo thể thao cut out",
			u"áo ngang ngực thể thao",	u"áo hai dây",
			u"áo định hình",	u"áo tạo hình",
			u"nhũ hoa",	u"đầm ngủ sexy",
			u"đầm bơi",	u"cậu nhỏ",
			u"vùng kín",	u"âm đạo",
			u"băng vệ sinh",	u"bvs",
			u"bao cao su",	u"gel bôi trơn",
			u"que thử thai",	u"bút thử thai",	
			u"que thử rụng trứng", u"pyjama",
			u"croptop"
		]

def no_accent_vietnamese(s):
    # s = s.decode('utf-8')
    s = re.sub(u'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(u'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(u'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(u'[ìíịỉĩ]', 'i', s)
    s = re.sub(u'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(u'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(u'đ', 'd', s)
    return s
def remove_special(s):
	# s = re.sub(r'[^\x00-\x7F]+',' ', s)
	# s = re.sub(r'[0-9]+','',s)
	# s = re.sub(r'&[a-z]+;', '', s)
	s = re.sub(r' {1,}',' ', s)
	s = re.sub(r'\n','', s)
	s = re.sub(r'\"','', s)	
	# s = re.sub(r'[^a-z]+','',s)
	return s

data_contents = []
f_write = open("preprocessor.txt", "w")
# f_write = open("test/aolot_test8.txt", "w")
f_target = open("labels.txt", "w")
# f_target = open("test/aolot_labels8.txt", "w")
with open("datatxt.json") as json_data:
	d = json.load(json_data)
	html_parser = HTMLParser.HTMLParser()
	count = 0
	for x in d:
		content = x["categoryid2"] + " " + x["name"] + " " + x["description"]
		content = content.lower()
		content = html_parser.unescape(content)
		content = remove_special(content)
		check_sexcontent = False
		for i in sex_words:
			i = i.encode("utf-8")
			content = content.encode("utf-8")
			# print content
			if i in content:
				check_sexcontent = True
				count+=1
				break
		if check_sexcontent:
			f_target.write("1 ")
		else: f_target.write("0 ")
		content = remove_special(content)
		# print type(content)
		f_write.write(content.decode("utf8"))
		f_write.write("\n")

