import os
'''
	
	之前的shrec文件是MeshCNN网络数据增强后的数据集，该脚本是删除那些增强的mesh
'''

path_in = '/home/kang/SSD/datasets/MeshWalker/datasets_raw/shrec11/SHREC11-MAPS-48-4-split16/'

shrec11_labels = [
    'armadillo', 'man', 'centaur', 'dinosaur', 'dog2',
    'ants', 'rabbit', 'dog1', 'snake', 'bird2',
    'shark', 'dino_ske', 'laptop', 'santa', 'flamingo',
    'horse', 'hand', 'lamp', 'two_balls', 'gorilla',
    'alien', 'octopus', 'cat', 'woman', 'spiders',
    'camel', 'pliers', 'myScissor', 'glasses', 'bird1'
]

shrec11_shape2label = {v: k for k, v in enumerate(shrec11_labels)}

for name in shrec11_shape2label:
    print('-->>>', name)
    for part in ['test', 'train']:
        print('-->>>', part)
        pin = os.path.join(path_in, name, part)
        
        # 使用 try/except 语句以处理可能的异常
        try:
            # 获取所有匹配的文件
            files_to_remove = [file for file in os.listdir(pin) if "-" in os.path.basename(file)]
            
            # 删除每个文件
            for file in files_to_remove:
                file_path = os.path.join(pin, file)
                os.remove(file_path)
                print(f"成功删除文件: {file_path}")
        except Exception as e:
            print(f"删除文件时发生异常: {e}")

                 
