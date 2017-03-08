def find_max_min(array):
  min_num=max_num=array[0]
  for i in array[1:]:
    if i < min_num:
      min_num = i
    else:
      if i > max_num:
        max_num = i
    if min_num==max_num:
      return [i]
  return [min_num,max_num]    
