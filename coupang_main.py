#-*- coding: utf-8 -*-
import json 

# with open("C:\\Users\\bel03\OneDrive\\바탕 화면\\WORK\\coupang\\jdx\\jdx_all_code.txt", "r") as ff:
#     codes = json.load(ff)
#     for code in codes:
#         print(code)
#         break
# with open("C:\\Users\\bel03\OneDrive\\바탕 화면\\WORK\\coupang\\jdx\\jdx_category_real.py", "r") as f:
#     data = json.load(f)
#     # print(type(data))
#     # print(data["M"]["TL"]) 

# data_M = data["M"]
# data_W = data["W"]
# displayCategoryCode = []

# for code in codes:
#     if code[6] == "M":
#         data = data_M
#     else:
#         data = data_W
    
#     if code[4:6] in list(data.keys()):
#         pro_code = code[4:6]
#         displayCategoryCode = data[pro_code]
#         category_num_list.append(category_num)

# with open("C:\\Users\\bel03\OneDrive\\바탕 화면\\WORK\\coupang\\jdx\\jdx_displayCategoryCode.py", "w") as fff:
#     json.dump(displayCategoryCode, fff)


##############start#################

#get category num from jdx code
with open("C:\\Users\\bel03\OneDrive\\바탕 화면\\WORK\\coupang\\jdx\\jdx_category_real.py", "r") as ff:
    data = json.load(ff)

data_M = data["M"]
data_W = data["W"]
displayCategoryCode = []

#get jdx info
with open("C:\\Users\\bel03\OneDrive\\바탕 화면\\WORK\\coupang\\jdx\\jdx_info.txt", "r", encoding="utf-8") as f:
    codes = json.load(f)

final_jdx_result = {}
jdx_result = {}
for code in codes:

    #get info to coupang.api setting
    name1 = codes[code][0]['name']
    ori = codes[code][1]['ori_price']
    sale = codes[code][2]['sale_price']
    photo_f = codes[code][3]['photo_front']
    photo_d = codes[code][4]['photo_detail']

    sellerProductName = name1[:-8] + name1[-6:-4]
    displayProductName = sellerProductName[3:-11] + "평촌점"
    generalProductName = displayProductName[4:]
    originalPrice = ori
    salePrice = sale
    imageType_REPRESENTATION = photo_f
    imageType_DETAIL = photo_d

    jdx_result["sellerProductName"] = sellerProductName
    jdx_result["displayProductName"] = displayProductName
    jdx_result["generalProductName"] = generalProductName
    jdx_result["originalPrice"] = originalPrice
    jdx_result["salePrice"] = salePrice
    jdx_result["imageType_REPRESENTATION"] = imageType_REPRESENTATION
    jdx_result["imageType_DETAIL"] = imageType_DETAIL
    
    # final_jdx_result[code] = jdx_result
    if code[6] == "M":
        data = data_M
    else:
        data = data_W

    if code[4:6] in list(data.keys()):
        pro_code = code[4:6]
        displayCategoryCode = data[pro_code]
    
    jdx_result["displayCategoryCode"] = displayCategoryCode

    final_jdx_result[code] = jdx_result


with open("C:\\Users\\bel03\OneDrive\\바탕 화면\\WORK\\coupang\\jdx\\jdx_result.py", "w", encoding="utf-8") as f:
    json.dump(final_jdx_result, f)
        
