def perms(list_):
    result =[]
    for i in range(len(list_)):
    # for i in range(len(list_)):
        Per = list_[i]
        Rest_list = list_[:i]+list_[i+1:]
        res = ([Per]+Rest_list)
        # result.append(res)
        # for i in perms(Rest_list):
        #     res = [Per]+
        # for i in res[1:]:
            
        # print(res)
        for k in perms(Rest_list):
            print([Per]+Rest_list[k])
            result.append(Per+Rest_list[k])
    return result

print(perms([1,2,3]))


		# if len(list_) == 0:
		# 	return None
		# elif len(list_) == 1:
		# 	result.append(list_)
		# # elif len(lis_) == 2:
		# # 	result.append(list_)
		# # 	result.append([::list_])
        # else: