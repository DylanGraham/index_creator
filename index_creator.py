import sys


def usage():
    print('Usage: index_creator.py <filename> <index_set_id>')
    sys.exit(1)


def do_work(argv):
    indexes = {'i7': [], 'i5': []}

    for line in open(argv[1]):
        words = line.split()

        indexes['i7'].append('array("index_set_id"=>"' + argv[2] + '", "index"=>"' + words[0] +
                             '"sequence"=>"' + words[1] +
                             '", "created_at"=>Carbon::now(), "updated_at"=>Carbon::now()),')

        if len(words) == 4:
            indexes['i5'].append('array("index_set_id"=>"' + argv[2] + '", "index"=>"' + words[2] +
                                 '"sequence"=>"' + words[3] +
                                 '", "created_at"=>Carbon::now(), "updated_at"=>Carbon::now()),')

    for key in indexes.keys():
        if indexes[key]:
            print(key + " indexes\n")
            for i in indexes[key]:
                print(i)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()

    do_work(sys.argv)
