import os
os.system("python extract_countvector_notcross_all_one_single.py")#单值特征
os.system("python extract_countvector_notcross_all_two_single.py")#多值特征
os.system("python extract_countvector_notcross_all_lack_single.py")#缺失值比较严重特征
os.system("python extract_countvector_pos_neg_aid.py")#用户正负aid
os.system("python extract_countvector_pos_neg_creativeSize_tfidf.py")#用户正负creativeSize
os.system("python extract_countvector_pos_neg_productId_tfidf.py")#用户正负productId
os.system("python extract_countvector_pos_neg_adCategoryId_tfidf.py")#用户正负adCategoryId
os.system("python extract_countvector_pos_neg_productType_tfidf.py")#用户正负productType