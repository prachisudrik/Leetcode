data=[]
data = input("Enter a list of numbers:")
len_data = len(data)
for i in range(0,len_data):
    lv_index = i
    if lv_index != len_data:
        lv_jumps = data[i]
        lv_index += lv_jumps