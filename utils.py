import machine, os


def get_machine_id():
    m_id_str = ''
    m_id = machine.unique_id()
    for d in m_id:
        m_id_str += '{:0>3}'.format(d)
    return 'trigger_{}'.format(m_id_str)


def mkdir(path):
    assert path[0:1] == '/', 'Please specify an absolute path'
    apath = path.split('/')
    for i in range(1,len(apath)-1):
        parent_path = '/'+ '/'.join(apath[1:i])
        cur_dir = apath[i]
        print('Checking for {} in {}'.format(cur_dir,parent_path))
        if not cur_dir in os.listdir(parent_path):
            print('Creating {}'.format(cur_dir))
            os.mkdir('/'.join([parent_path,cur_dir]))
     