from Utils.FileFunc import FileFunc as ff
import Utils.TimeFunc as tf
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


def extract_students_usage(filenames):

    ret = []

    for fn in filenames['usage']:
        if 'eaps' in fn:
            ret.append(fn)
    return ret


def extract_students_interaction(filenames):

    ret = []

    for fn in filenames['interaction']:
        if 'eaps' in fn:
            ret.append(fn)
    return ret


def extract_domainexperts(filenames):
    ret = []

    for fn in filenames:
        if 'eaps' not in fn:
            ret.append(fn)
    return ret


def clean_line(line):
    n = 5
    groups = line.split(' ')
    return ' '.join(groups[:n]), ' '.join(groups[n:])


def extract_timestamp(line):
    pass


if __name__ == '__main__':

    files = load('data/LOG', '.txt')
    # print(files)

    # for fn in files:
    #     print(ff.read_file_into_list(fn))

    # print(load_memory_usage_data())
    data = get_usage_and_interaction(files)

    for fn in data['interaction']:
        print(fn)
    print('---')
    for fn in data['usage']:
        print(fn)

    print(extract_students_interaction(data))
    print(extract_timestamp('May 6, 2016, 4:07 pm CLASSIFIER ENABLE'))
    print(tf.time_func_log_date_to_python_date('May 6, 2016, 4:07 pm'))