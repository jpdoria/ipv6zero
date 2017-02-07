#!/usr/bin/env python

import sys


def save_file(ok_list, dst_file):
    try:
        with open(dst_file, 'a') as fh:
            for elem in ok_list:
                fh.write('{}\n'.format(elem))
    except:
        raise


def process_file(src_file):
    try:
        with open(src_file, 'r') as fh:
            lines = fh.readlines()
    except:
        raise

    ip_addresses = [(line.strip()) for line in lines]
    chunks = [(ip.split(':')) for ip in ip_addresses]
    chunks_len = len(chunks)
    index = 0
    ok_list = []

    while index != chunks_len:
        print('Checking {}...'.format(ip_addresses[index]))

        for elem in chunks[index]:
            if len(elem) != 4:
                new_elem = '{}0'.format(elem)
                elem_index = chunks[index].index(elem)
                chunks[index][elem_index] = new_elem

                print('3-char chunk found: {}'.format(elem))
                print('NewValue: {}'.format(new_elem))

        ok_list.append(':'.join(chunks[index]))
        index += 1

    return ok_list


def main():
    src_file = sys.argv[1]
    dst_file = sys.argv[2]

    ok_list = process_file(src_file)
    save_file(ok_list, dst_file)


if __name__ == '__main__':
    main()
