object_need_to_check_all_attr=ss.base_columns
print('------------')
print('main','==>',object_need_to_check_all_attr)
print('main_type','==>',type(object_need_to_check_all_attr))

for i in dir (object_need_to_check_all_attr):
  print("------------")
  print(i,'==>')
  try:
  print(getattr(object_need_to_check_all_attr,i)())
  except Exception as e:

  print(getattr(object_need_to_check_all_attr,i))
#获得对象信息以及对象的dir属性运行的效果