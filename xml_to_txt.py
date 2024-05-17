import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_txt_function():
    data_path = "C:/Users/admin/Downloads/annotations/codes/codes/photos/" 
    savedir = "C:/Users/admin/Downloads/annotations/codes/codes/photos/"

    path=os.path.join(data_path, 'anno/')
    #print(path)
    # savedir = os.path.join(path, 'txt_annotations/')

    try:
        os.makedirs(savedir, exist_ok=True)                   
    except OSError as err:
        #print('====================')
        print(err.strerror)
    else:
        print("Successfully created save directory")
        print("dir",savedir)


    class_list=[]
    
    #os.chdir(dirdata_path)
    for root,dirs,files in os.walk(path):
        print(files)
        for filename in files:
            print(filename)
            
            if not filename.endswith('xml'):  
                continue

            if os.stat(path+filename).st_size == 0:
                os.remove(path+filename)
                
            if filename.endswith('.xml'):
                # print(filename)
                tree = ET.parse(path+filename)
                root = tree.getroot()
                
                for member in root.findall('object'):
                    # filename=root.find('filename').text
                    width=int(root.find('size')[0].text)
                    height=int(root.find('size')[1].text)

                    label=(member[0].text).strip()
                    # print(label)
                    
                    # width = 1280
                    # height = 720
                    # if label in ['person']:
                    #    x = 0
                    # #    print(x)
                    #    label='person'
                    #    if label not in class_list:
                    #         class_list.append(label)
                    if label in ['person','person','person','Person','p']:
                        x = 0
                        #    print(x)
                        label='cap'
                        if label not in class_list:
                                class_list.append(label)

                    if label in ['person','person','person','Person','p']:
                        x = 0
                        #    print(x)
                        label='person'
                        if label not in class_list:
                                class_list.append(label)

                    if label in ['person','person','person','Person','p']:
                        x = 0
                        #    print(x)
                        label='person'
                        if label not in class_list:
                                class_list.append(label)
                    # if label in ['motorcycle']:
                    #    x = 0
                    # #    print(x)
                    #    label='motorcycle'
                    #    if label not in class_list:
                    #         class_list.append(label)

                    # elif label in ['car']:
                    #    x = 1
                    # #    print(x)
                    #    label='car'
                    #    if label not in class_list:
                    #         class_list.append(label)

                    # elif label in ['bus','Bus']:
                    #     x=2
                    #     label = 'bus'
                    #     if label not in class_list:
                    #         class_list.append(label)
                            
                    # elif label in ['truck']:
                    #     x=3
                    #     label = 'truck'
                    #     if label not in class_list:
                    #         class_list.append(label)

                    # elif label in ['autorickshaw']:
                    #     x=4
                    #     label = 'autorickshaw'
                    #     if label not in class_list:
                    #         class_list.append(label)

                    # elif label in ['tractor']:
                    #     x=5
                    #     label = 'tractor'
                    #     if label not in class_list:
                    #         class_list.append(label)

                    if label in ['with_helmet','With_helmet','with helmet','with-helmet','With Helmet']:
                        x = 1
                    #    print(x)
                        label='with_helmet'
                        if label not in class_list:
                            class_list.append(label)

                    elif label in ['without_helmet','Without_helmet','without helmet','without-helmet','Without Helmet']:
                        x = 2
    #                 #    print(x)
                        label='without_helmet'
                        if label not in class_list:
                            class_list.append(label)
                
                    elif label in ['with_glove','with_safetyglove','witt_glove','with-glove','with_glove','with_safety_glove','with safetyglove','with safety glove']: 
                        x=3
                        label = 'with_glove'
                        if label not in class_list:
                            class_list.append(label) 
    # # # # ['without_vest\n',  'without_glove\n', 'with_shoe\n', 'without_shoe\n', 'with_vest\n', 'with_helmet\n', ,'witt_shoe\n', 'with_safetyshoe\n', 'without_safetyglove\n', 'with_safetyglove\n', 'with_safteyglove\n', 'with safetyshoe\n', 'with vest\n', 'without safetyglove\n', 'with weldingglove\n', 'with faceshield\n', 'without vest\n', 'without faceshield\n', 'with-vest\n', 'without_faceshield\n', 'with_welding_glove\n', 'with_safety_shoe\n', 'without_safety_shoe\n', 'with_faceshield\n', 'with_weldingglove\n', 'without_weldingglove\n', 'without weldingglove\n', 'without_safetyshoe\n', 'with_mask\n', 'without_mask\n', 'With_shoe\n', 'Without_vest\n', 'hand\n', 'With_mask\n']
    # #                 
                    elif label in ['without_glove','without glove','without_safetyglove','without_gloves','without-glove','without weldingglove','without_weldingglove','without_glove','without_safety_glove','without safetyglove','without safety glove','hand']:
                        x=4
                        label='without_glove'
                        if label not in class_list:
                            class_list.append(label) 

                    # elif label in ['with_suit']:
                    #     x=7
                    #     label='with_suit'
                    #     if label not in class_list:
                    #        class_list.append(label)

                    # elif label in ['without_suit']:
                    #     x=8
                    #     label='without_suit'
                    #     if label not in class_list:
                    #        class_list.append(label)
                    # #                                                                                         
                    # elif label in ['with_vest','with_safetyvest','with vest','with-vest','with_safety_vest','with safetyvest','with safety vest','vest']:
                    #     x=5
                    #     label='with_vest'
                    #     if label not in class_list:
                    #        class_list.append(label)

                    # elif label in ['without_vest','without_safetyvest','without vest','without-vest','without_safety_vest','without safetyvest','without safety vest']:
                    #     x=6
                    #     label='without_vest'
                    #     if label not in class_list:
                    #        class_list.append(label)                                                                    


                    # elif label in ['with_shoe','with_safetyshoe','witt_shoe','with shoe','with-shoe','with_safety_shoe','with safetyshoe','with safety shoe']:
                    #     x=7
                    #     label='with_shoe'
                    #     if label not in class_list:
                    #        class_list.append(label)                                                                     
                                                                        

                    # elif label in ['without_shoe','without_safetyshoe','without shoe','without-shoe','without_safety_shoe','without safetyshoe','without safety shoe']:
                    #     x=8
                    #     label='without_shoe'
                    #     if label not in class_list:
                    #        class_list.append(label)                                                                     


                    else:
                        # file=open(f"{savedir}{filename.rsplit('.xml')[0]}.txt","w")
                        # file.close
                        print("filename:",f"{filename} : {label} ")
                        continue                                  
                    # elif label in ['suv','Suv','SUV']:
                    #     x=3
                    #     label='suv'
                    #     if label not in class_list:
                    #         class_list.append(label)
                    # elif label in ['autorickshaw','Autorickshaw','AUTORICKSHAW']:
                    #     x=4
                    #     label = 'autorickshaw'
                    #     if label not in class_list:
                    #         class_list.append(label)
                    # elif label in ['motorcycle','Motorcycle','MOTORCYCLE']:
                    #     label = 'motorcycle'
                    #     x=5
                    #     if label not in class_list:
                    #         class_list.append(label) 
                    # elif label in ['without_shoe', 'without_shoes','without_safetyshoes','without_safetyshoe']:
                    #     x=6
                    #     label = 'without_shoe'
                    #     if label not in class_list:
                    #         class_list.append(label)
                    # elif label in ['with_mask','with_mask', 'With_Mask', 'Person_with_mask','With_mask','with-mask','with_maks']:
                    #    x=7
                    #    label='with_mask'
                    #    if label not in class_list:
                    #        class_list.append(label)
                    # elif label in ['without_mask', 'withou_mask','Person_without_mask', 'No_Mask', 'Without_Mask','Without_mask']:
                    #     x=8
                    #     label='without_mask'
                    #     if label not in class_list:
                    #         class_list.append(label)
                    # elif label in ['with_apron' ,'With_Apron','WITH_APRON','with_Apron','With_apron','blue_apron', 'Blue_apron','with_blueapron','with-blueapron' ]:
                    #      label = 'with_apron'
                    #      x=9
                    #      if label not in class_list:
                    #          class_list.append(label) 
                    # elif label in ['without_apron' ,'Without_Apron','WITHOUT_APRON','without_Apron','Without_apron']:
                    #     label = 'without_apron'
                    #     x=10
                    #     if label not in class_list:
                    #         class_list.append(label) 
                    # elif label in ['with_goggles', 'With_Goggles', 'WITH_GOGGLES','With_goggles','with_goggle']:
                    #      x=11
                    #      label='with_goggle'
                    #      if label not in class_list:
                    #          class_list.append(label)
                    # elif label in ['without_goggles', 'Without_Goggles', 'WITHOUT_GOGGLES','Without_goggles','without_goggle', 'Without_googles','Withuout_goggles', 'Withouy_goggles']:
                    #      x=12
                    #      label='without_goggle'
                    #      if label not in class_list:
                    #          class_list.append(label)

                    
                    # if label in ['machinee_glove','machine_glove','Machine_glove']:
                    #     x=2
                    #     label='with_glove'
                    #     if label not in class_list:
                    #         class_list.append(label)
                    

                    
                
                
                    
                
                    

                    '''    
                    xmin=int(member[4][0].text)
                    ymin=int(member[4][1].text)
                    xmax=int(member[4][2].text)
                    ymax=int(member[4][3].text)
                    '''
                    xmlbox = member.find('bndbox') 
                    xmin=int(xmlbox.find('xmin').text)
                    ymin=int(xmlbox.find('ymin').text)
                    xmax=int(xmlbox.find('xmax').text)
                    ymax=int(xmlbox.find('ymax').text)               

                    try:
                        x_center = (xmin + xmax) / (2 * width)
                        y_center = (ymin + ymax) / (2 * height)
                        w = (xmax - xmin) / width
                        h = (ymax - ymin) / height
                    except ZeroDivisionError:
                        print (filename, 'the width in question')

                    with open(os.path.join(savedir, filename.rsplit('.xml')[0]+'.txt'), 'a+') as f:
                        f.write(' '.join([str(x),str(x_center), str(y_center), str(w), str(h) + '\n']))
                        
    #with open(os.data_path.join(savedir,'classes.txt'),'a+') as c:
    #    c.write('\n'.join([str(classname) for classname in class_list ]))
            
    print('Successfully converted xml to txt')

xml_to_txt_function()