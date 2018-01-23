import docx
def readdocx(docname):
	fulltext=[]
	doc=docx.Document(docname)
	paras = doc.paragraphs
	for x in  paras:
		fulltext.append(x.text)
	return  '\n'.join(fulltext) #原本换行作为分割标志，
	#print将每一段落用''框起来；用了这个则用换行表示出段落
	# return  fulltext
print(readdocx('用户访谈.docx'))
