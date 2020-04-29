import sys
import os
import functions as f
import zlib
import shutil

def calculateCRC32(new_weapon):
    x = zlib.crc32(b'IsGet_' + new_weapon.encode())
    if x >= 0x80000000:
        x = x - 0x100000000
    return str(x)

def boolEntry(csv_file, index):
    to_import =  '- DataName: IsGet_' + csv_file[index][0] + '\n'
    to_import += '  DeleteRev: -1\n'
    to_import += '  HashValue: ' + calculateCRC32(csv_file[index][0]) + '\n'
    to_import += '  InitValue: 0\n'
    to_import += '  IsEventAssociated: false\n'
    to_import += '  IsOneTrigger: true\n  IsProgramReadable: true\n  IsProgramWritable: true\n  IsSave: true\n  MaxValue: true\n  MinValue: false\n  ResetType: 0\n'
    return to_import


def changeFlags(pack_name, csv_file, index):
    boolPath_base = 'BASE_unbuilt\content\Pack\Bootup.pack\GameData\gamedata.ssarc\\'
    if not os.path.exists(pack_name + '\\content\Pack\Bootup.pack'):
        shutil.copytree('BASE_unbuilt\content\Pack\Bootup.pack', pack_name + '\\content\Pack\Bootup.pack')
    boolPath = pack_name + '\content\Pack\Bootup.pack\GameData\gamedata.ssarc\\'
    #f.checkAndDelete(boolPath + 'bool_data_0.bgdata.yml')
    to_import = boolEntry(csv_file, index)

    #fin = open(boolPath_base + 'bool_data_0.bgdata.yml', 'rt')
    fout = open(boolPath + 'bool_data_0.bgdata.yml', 'a')
    #for line in fin:
    #        fout.write(line)
    fout.write(to_import)
    #fin.close()
    fout.close()