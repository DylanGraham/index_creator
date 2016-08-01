import sys


def usage():
    print('Usage: index_creator.py <filename> <i7_index_set_id> [i5_index_set_id]')
    sys.exit(1)


def do_work(file, i7_set_id, i5_set_id):
    indexes = {'i7': [], 'i5': []}

    for line in open(file):
        words = line.split()
        if len(words) == 2:
            indexes['i7'].append('array("index_set_id"=>"' + i7_set_id + '", "index"=>"' + words[0] +\
                                 'A01", "sequence"=>"' + words[1] +\
                                 '", "created_at"=>Carbon::now(), "updated_at"=>Carbon::now()),')

        elif len(words) == 4:
            indexes['i7'].append('array("index_set_id"=>"' + i7_set_id + '", "index"=>"' + words[0] +
                                 'A01", "sequence"=>"' + words[1] +
                                 '", "created_at"=>Carbon::now(), "updated_at"=>Carbon::now()),')

            indexes['i5'].append('array("index_set_id"=>"' + i5_set_id + '", "index"=>"' + words[2] +
                                 'A01", "sequence"=>"' + words[3] +
                                 '", "created_at"=>Carbon::now(), "updated_at"=>Carbon::now()),')

    print('i7 indexes\n')
    for i in indexes['i7']:
        print(i)

    if indexes['i5']:
        print('\ni5 indexes\n')
        for i in indexes['i5']:
            print(i)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()

    do_work(sys.argv[1], sys.argv[2], sys.argv[3])
