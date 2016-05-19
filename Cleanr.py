from Utils.FileFunc import FileFunc as ff
import glob

def load(foldername, filetype):
    ret = []
    files = glob.glob(foldername + '/*' + filetype)
    for f in files:
        if f is foldername:
            continue
        ret.append(f)
    return ret

def load_memory_usage_data():

    ret = []
    ret = load('data/LOG', 'memory_usage.txt')
    return ret

def filter_out_memory_data(filenames):

    ret = []
    for fn in filenames:
        if 'memory_usage' not in fn:
            ret.append(fn)

    return ret

def get_usage_and_interaction(filenames):

    filenames = filter_out_memory_data(filenames)

    data = dict(usage=[], interaction=[])

    for fn in filenames:
        if 'usage' in fn:
            data['usage'].append(fn)
        elif 'interaction' in fn:
            data['interaction'].append(fn)

    return data

if __name__ == '__main__':

    files = load('data/LOG', '.txt')
    # print(files)

    # for fn in files:
    #     print(ff.read_file_into_list(fn))

    # print(load_memory_usage_data())

    print(get_usage_and_interaction(files))