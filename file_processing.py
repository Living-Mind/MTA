import re
with open("text.txt", "r") as word_list:
    format_text = word_list.read().replace("\n", " ")
    #print(format_text)

    words = format_text.split(" ")
    #print(words)     

    words_dict = {}

    for i in words:
        reps = words.count(i)
        words_dict.update({i: reps})

    #print(words_dict)


    reversed_dict = {}
    for keys, values in words_dict.items():
        reversed_dict[values] = keys

    sorted_dict = sorted(words_dict.items(), key=lambda item: item[1])
    #print(type(sorted_dict))
    #print(sorted_dict)

    
    for list_itme in reversed(sorted_dict):
        #c = str(list_itme).replace("('","").replace("","").replace(")","")
        c = re.sub("['()\"]", "", str(list_itme)).replace(",", " :")
        print(c)