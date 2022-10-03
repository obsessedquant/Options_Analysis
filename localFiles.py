def getLocalFileNameDict(path_input: str) -> dict:
    '''Get list of local files'''
    import glob
    import os
    from collections import defaultdict
    import datetime
    
    list_of_files = glob.glob(path_input) # * means all if need specific format then *.csv
    files_dict = defaultdict(list)
    
    for file in list_of_files:
        
        filename = os.path.basename(file)
        
        file_mod_date = os.path.getmtime(file)
        file_mod_datetime_str = datetime.datetime.fromtimestamp(file_mod_date).strftime('%Y-%m-%d %H:%M:%S.%f')
        file_mod_datetime_datetime = datetime.datetime.strptime(file_mod_datetime_str,'%Y-%m-%d %H:%M:%S.%f')
        
        file_create_date = os.path.getctime(file)
        file_create_datetime_str = datetime.datetime.fromtimestamp(file_create_date).strftime('%Y-%m-%d %H:%M:%S.%f')
        file_create_datetime_datetime = datetime.datetime.strptime(file_create_datetime_str,'%Y-%m-%d %H:%M:%S.%f')
        
        files_dict['filename'].append(filename)
        files_dict['create_time'].append(file_create_datetime_datetime)
        files_dict['mod_time'].append(file_mod_datetime_datetime)
        
    return files_dict

# local_files_dict = getLocalFileNameDict(local_file_path_string)
# local_files_dict