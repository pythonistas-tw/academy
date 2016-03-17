#!/usr/bin/env python
# encoding: utf-8

import csv
import glob
import os
import chardet


def get_enc(file_path):
    try:
        with open(file_path, 'rb') as f:
            rawdata = f.read()
            enc_info = chardet.detect(rawdata)
            # print(enc_info)
            file_enc = enc_info['encoding']
            if not is_correct_enc(file_path, file_enc):
                if file_enc == 'GB2312':
                    file_enc = 'Big5'
                    if not is_correct_enc(file_path, file_enc):
                        file_enc = ''
                else:
                    file_enc = ''

            # if file_enc == 'windows-1252':
                # file_enc = 'CP950'

            return file_enc
    except(Exception) as err:
        print('get_enc except: ' + err.msg)


def is_correct_enc(file_path, enc):
    try:
        with open(file_path, encoding=enc) as f:
            f.read()
#            print('openfile ok: ' + enc)
            return True
    except(UnicodeDecodeError):
        # print('UnicodeDecodeError: ' + file_path + ' ' +enc)
        return False


def UTF8_translator(source_dir, dest_dir, print_fail_only):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    file_name_spc = 45
    enc_spc = 12
    translate_fail = 0
    translate_sucess = 0
    total = 0
    for file in glob.glob(source_dir + '/*.CSV'):
        total += 1
        try:
            print_str = file
            enc = get_enc(file)
            if not enc:
                translate_fail += 1
                print_str +=(file_name_spc - len(file)) * ' ' + enc_spc * ' ' + 'Fail(Unknow Enc)'
                print(print_str)
                continue
            with open(file, newline='', encoding=enc) as f:
                reader = csv.reader(f)
                with open(dest_dir + '/' + os.path.basename(file), 'w', newline='') as csvfile:
                    spanwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    for row in reader:
                        spanwriter.writerow(row)
            if not print_fail_only:
                print_str += (file_name_spc - len(file)) * ' ' +enc + (enc_spc - len(enc)) * ' ' + 'SUCSEE'
                print(print_str)
        except(UnicodeDecodeError):
            print_str += (file_name_spc - len(file)) * ' ' + enc_spc * ' ' + 'Fail(codecs)'
            print(print_str)
        translate_sucess += 1

    print((file_name_spc + enc_spc + 20) * '=')
    print('total:  ' + str(total))
    print('Sucess: ' + str(translate_sucess))
    print('Fail:   ' + str(translate_fail))


def singel_file(file_path, enc):
    try:
        temp_dir = 'tmp'
        if not os.path.exists(temp_dir):
            os.mkdir(temp_dir)
        with open(file_path, newline='', encoding=enc) as f:
            reader = csv.reader(f)
            with open(temp_dir + '/' + os.path.basename(file_path), 'w', newline='') as csvfile:
                spanwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    print(row)
                    spanwriter.writerow(row)

    except(UnicodeDecodeError) as err:
        print('except: ' + str(err))


UTF8_translator('lvr_landcsv', 'UTF8Files', False)
# singel_file('lvr_landcsv/E_LVR_LAND_A.CSV', 'CP950')
