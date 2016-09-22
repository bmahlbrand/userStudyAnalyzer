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
    ret = clean_line(line)
    return tf.time_func_log_date_to_python_date(ret[0])


def extract_action(line):
    ret = clean_line(line)
    return ret[1].split(' ')[0]


def extract_operation(line):
    ret = clean_line(line)
    return ret[1].split(' ')[1]


def extract_durations(user_actions):

    stk = []

    for entry in user_actions:
        print(entry)
        stk.append(entry)

    while len(stk):
        en = stk.pop()
        for e in stk:
            if e['action'] == en['action']:
                print("found")
                stk.remove(e)


def build_table_from_files(filenames):
    thestructure = {}

    students = extract_students_interaction(data)
    for fn in students:
        ret = ff.read_file_into_list(fn)
        lst = []

        for e in ret:
            # print(e)
            entry = {'timestamp': extract_timestamp(e), 'action': extract_action(e), 'operation': extract_operation(e)}
            lst.append(entry)

        thestructure[fn] = lst

    return thestructure

if __name__ == '__main__':

    files = load('data/LOG', '.txt')
    # print(files)

    # for fn in files:
    #     print(ff.read_file_into_list(fn))

    # print(load_memory_usage_data())
    data = get_usage_and_interaction(files)

    # for fn in data['interaction']:
    #     print(fn)
    # print('---')
    # for fn in data['usage']:
    #     print(fn)
    print(extract_timestamp('May 06, 2016, 4:07 pm CLASSIFIER ENABLE'))
    print(extract_timestamp('February 21, 2016, 5:07 pm CLASSIFIER ENABLE'))

    table = build_table_from_files(data)
    print('table: ', table)
    print(table.keys())
    key = list(table.keys())[0]
    print(extract_durations(table[key]))

    print(tf.time_func_log_date_to_python_date('May 6, 2016, 4:07 pm'))

    print(extract_action('May 6, 2016, 4:07 pm CLASSIFIER ENABLE'))
    print(extract_operation('May 6, 2016, 4:07 pm CLASSIFIER ENABLE'))