from pylab import *
import os
import os.path as osp

def get_ids_to_rank(ids ,txt_path_list):
    """查询ids对应的排名""" 
    date_to_rank = {}
    for txt_path in txt_path_list:
        with open(txt_path,'r') as fp:
            contents = fp.readlines()
        date_time = txt_path.split('/')[-1][:-4]
        
        tmp_index = 0
        flag = 0
        for sample in contents:
            tmp_index +=1
            if ids in sample[:-1]:
                date_to_rank[date_time] = tmp_index
                flag= 1
                break
        if flag == 0 :
            if len(contents)==0:
                pass
            else:
                date_to_rank[date_time] = 50
        
            
    return date_to_rank     



def get_all_ids_list():
    """得到所有的ids排名"""
    folder_path = '/cloud/cloud_disk/users/huh/nlp/vision-reptile/dataset/rank_screenshots_10_11'
    files_list = os.listdir(folder_path)
    txt_list = []
    date_list = []
    txt_path_list = []
    ids_list = []
    for sample in  files_list:
        if 'txt' in sample:
            txt_list.append(sample)
            date_information = sample.split('-')[2]+sample.split('-')[3]   
            date_list.append(date_information)         
            txt_path = os.path.join(folder_path,sample)
            txt_path_list.append(txt_path)
            with open(txt_path,'r') as fp:
                contents = fp.readlines()
            tmp_index = 0
            for sample in contents:
                tmp_index +=1
                ids_list.append(sample[:-1])
                if tmp_index>10:
                    break
    ids_list = set(ids_list)
    return ids_list,date_list,txt_path_list

def generate_rank_dataset(date_to_rank,ids):
    """生成单个产品的排序数据集"""
    rank_list = []
    rank_list.append("date,rank\n")
    folder_path = '/home/huhao/scripts/time_series/data'
    for key,value in date_to_rank.items():
        rank_list.append('"{}",{}\n'.format(key[:-3],value))
    with open(osp.join(folder_path,ids+'_rank.csv'),'w') as fp:
        fp.writelines(rank_list)
    

if __name__ == '__main__':
    ids_list,date_list,txt_path_list = get_all_ids_list()
    ids = 'B06X6J3L65'
    date_to_rank = get_ids_to_rank(ids ,txt_path_list)
    generate_rank_dataset(date_to_rank,ids)
    
