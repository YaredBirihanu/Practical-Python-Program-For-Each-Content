#using replace()

# def replace_file_content(file_path, old_content, new_content):
#     with open(file_path, 'r') as file:
#         content = file.read()

#     updated_content = content.replace(old_content, new_content)

# list=['Gfg','is','best','for','Geeks']

# res=[sub.replace('G','-').replace('e','G').replace('-','e') for sub in list]
# print('List after performing character swap : ',str(res))

#using string function


list=['Gfg','is','best','for','Geeks']
res=",".join(list)
res=res.replace('G',"_").replace("e","G").replace("_","e").split(', ')

print('List after performing character swap : ',str(res))