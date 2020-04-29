import os
import sys
import pathlib
import shutil
import Description

def checkAndDelete(file):
    if os.path.isfile(file):
        os.remove(file)

def newFolderTree(pack_name):
    if not os.path.exists(pack_name + "\\content\\Model"):
        os.system("mkdir " + pack_name + "\\content\\Model")
    if not os.path.exists(pack_name + "\\content\\Actor\\Pack"):
        os.system("mkdir " + pack_name + "\\content\\Actor\\Pack")
    if not os.path.exists(pack_name + "\\content\\Pack"):
        os.system("mkdir " + pack_name + "\\content\\Pack")
    if not os.path.exists(pack_name + "\\content\\UI\\Stockitem"):
        os.system("mkdir " + pack_name + "\\content\\UI\\Stockitem")
    if not os.path.exists(pack_name + "\\content\\Actor\\ActorInfo"):
        shutil.copytree("BASE_unbuilt\\content\\Actor\\ActorInfo\\", pack_name + "\\content\\Actor\\ActorInfo\\")
    if not os.path.isfile(pack_name + "\\rules.txt"):
        os.system("copy BASE_unbuilt\\rules.txt " + pack_name + "  >nul")
    if not os.path.isfile(pack_name + "\\.done"):
        f = open(pack_name + "\\.done", 'wt')
        f.write('1587446924.393938')
        f.close()

def newActorpack(pack_name, csv_file, index):
    if os.path.exists(pack_name + "\\content\\Actor\\Pack\\" + csv_file[index][0] + ".sbactorpack"):
        shutil.rmtree(pack_name + "\\content\\Actor\\Pack\\" + csv_file[index][0] + ".sbactorpack")
    os.system("xcopy /E /I /q /f BASE_unbuilt\\content\\Actor\\Pack\\" + csv_file[index][13] +".sbactorpack " + pack_name + "\\content\\Actor\\Pack\\" + csv_file[index][0] + ".sbactorpack >nul")
    #ActorpackPath = pack_name + '_unbuilt\content\Actor\Pack\\'
    #os.rename(ActorpackPath + base + '.sbactorpack', ActorpackPath + new_weapon + '.sbactorpack')

def newActorinfo(csv_file, pack_name, index):
    ActorinfoPath_base = 'BASE_unbuilt\\content\\Actor\\ActorInfo\\'
    ActorinfoPath = pack_name + '\\content\\Actor\\ActorInfo\\'
    checkAndDelete(ActorinfoPath + csv_file[index][0] + '.info.yml')

    fin = open(ActorinfoPath_base + csv_file[index][13] + '.info.yml', 'rt')
    fout = open(ActorinfoPath + csv_file[index][0] + '.info.yml', 'wt')
    for line in fin:
        if 'bfres' in line or 'mainModel' in line or 'name' in line:
            fout.write(line.replace(csv_file[index][13], csv_file[index][0]))
        elif 'elink' in line:
            fout.write('elink: ' + csv_file[index][1] + '\n')
        elif 'itemBuyingPrice' in line:
            fout.write('itemBuyingPrice: 1000' + '\n')
        elif 'attackPower' in line:
            fout.write('attackPower: ' + csv_file[index][2] + '\n')
        elif 'weaponCommonGuardPower' in line:
            fout.write('weaponCommonGuardPower: ' + csv_file[index][3] + '\n')
        elif 'generalLife' in line:
            fout.write('generalLife: ' + csv_file[index][4] + '\n')
        elif 'instSize' in line:
            fout.write('instSize: 199999\n')
        else:
            fout.write(line)
    fin.close()
    fout.close()

def newActorLink(pack_name, csv_file, index):
    ActorLinkPath_Base = 'BASE_unbuilt\content\Actor\Pack\\' + csv_file[index][13] + '.sbactorpack\Actor\ActorLink\\'
    ActorLinkPath = pack_name + '\content\Actor\Pack\\' + csv_file[index][0] + '.sbactorpack\Actor\ActorLink\\'
    checkAndDelete(ActorLinkPath + csv_file[index][0] + '.bxml.yml')
    fin = open(ActorLinkPath_Base + csv_file[index][13] + '.bxml.yml', 'rt')
    fout = open(ActorLinkPath + csv_file[index][0] + '.bxml.yml', 'wt')
    for line in fin:
        if 'ElinkUser' in line:
            fout.write('      ElinkUser: ' + csv_file[index][1] + '\n')
        elif 'ModelUser' in line or 'GParamUser' in line:
            fout.write(line.replace(csv_file[index][13], csv_file[index][0]))
        else:
            fout.write(line)

    fin.close()
    fout.close()
    os.system('del ' + ActorLinkPath + csv_file[index][13] +'.bxml.yml')


def newGparam(pack_name, csv_file, index):
    #GeneralParamList
    GparamPath_base = 'BASE_unbuilt\content\Actor\Pack\\' + csv_file[index][13] + '.sbactorpack\Actor\GeneralParamList\\'
    GparamPath = pack_name + '\content\Actor\Pack\\' + csv_file[index][0] + '.sbactorpack\Actor\GeneralParamList\\'
    checkAndDelete(GparamPath + csv_file[index][0] + '.bgparamlist.yml')
    fin = open(GparamPath_base + csv_file[index][13] + '.bgparamlist.yml', 'rt')
    fout = open(GparamPath + csv_file[index][0] + '.bgparamlist.yml', 'wt')
    for line in fin:
        if 'IsLifeInfinite' in line:
            fout.write('      IsLifeInfinite: ' + csv_file[index][5] + '\n')
        elif '      Power: ' in line:
            fout.write('      Power: ' + csv_file[index][2] + '\n')
        elif '      Life: ' in line:
            fout.write('      Life: ' + csv_file[index][4] + '\n')
        elif '      ElectricalDischarge' in line:
            fout.write('      ElectricalDischarge: ' + csv_file[index][6] + '\n')
        #elif '      IsBurnOutBorn' in line:
        #    fout.write('      IsBurnOutBorn: ' + csv_file[index][7] + '\n')
        elif '      IsHammer' in line:
            fout.write('      IsHammer: ' + csv_file[index][8] + '\n')
        elif 'PodName: ' in line:
            fout.write('      PodName: !str32 ' + csv_file[index][9] + '\n')
        elif 'BuyingPrice: ' in line:
            fout.write('      BuyingPrice: 1000' + '\n')
        elif '      MagicName: ' in line:
            if csv_file[index][11] == '':
                fout.write(line)
            else:
                fout.write('      MagicName: !str32 ' + csv_file[index][11] + '\n')
        else:
            fout.write(line)
    fin.close()
    fout.close()
    os.system('del ' + GparamPath + csv_file[index][13] + '.bgparamlist.yml')

def newModelList(pack_name, csv_file, index):
    ModelListPath_base = 'BASE_unbuilt\content\Actor\Pack\\' + csv_file[index][13] + '.sbactorpack\Actor\ModelList\\'
    ModelListPath = pack_name + '\content\Actor\Pack\\' + csv_file[index][0] + '.sbactorpack\Actor\ModelList\\'
    checkAndDelete(ModelListPath + csv_file[index][0] + '.bmodellist.yml')
    fin = open(ModelListPath_base + csv_file[index][13] + '.bmodellist.yml', 'rt')
    fout = open(ModelListPath + csv_file[index][0] + '.bmodellist.yml', 'wt')
    for line in fin:
        if csv_file[index][13] in line:
            fout.write(line.replace(csv_file[index][13], csv_file[index][0]))
        else:
            fout.write(line)
    fin.close()
    fout.close()
    os.system('del ' + ModelListPath + csv_file[index][13] + '.bmodellist.yml')

def newModels(pack_name, csv_file, index):
    ModelPath_base = 'BASE_unbuilt\content\Model\\'
    ModelPath = pack_name + '\content\Model\\'

    checkAndDelete(ModelPath + csv_file[index][0] + '.sbfres')
    checkAndDelete(ModelPath + csv_file[index][0] + '.Tex1.sbfres')
    checkAndDelete(ModelPath + csv_file[index][0] + '.Tex2.sbfres')
    os.system('bfres_duplicator \"' + ModelPath_base + csv_file[index][13] + '.sbfres\" \"' + ModelPath + csv_file[index][0] + '.sbfres\"')
    os.system('bfres_duplicator \"' + ModelPath_base + csv_file[index][13] +'.Tex1.sbfres\" \"' + ModelPath + csv_file[index][0] + '.Tex1.sbfres\"')
    os.system('bfres_duplicator \"' + ModelPath_base + csv_file[index][13] +'.Tex2.sbfres\" \"' + ModelPath + csv_file[index][0] + '.Tex2.sbfres\"')

    ui = "UI"
    iconPath_base = "BASE_unbuilt\\content\\" + ui + "\\Stockitem\\"
    iconPath = pack_name + "\content\\" + ui + "\Stockitem\\"
    checkAndDelete(iconPath + csv_file[index][0] + '.sbitemico')
    os.system('bfres_duplicator \"' + iconPath_base + csv_file[index][13] +'.sbitemico\" \"' + iconPath + csv_file[index][0] + '.sbitemico\"')


def defineItemType(csv_file, index):
    if 'Shield' in csv_file[index][0]: return 'WeaponShield'
    elif 'Sword' in csv_file[index][0]: return 'WeaponSmallSword'
    elif 'Lsword' in csv_file[index][0]: return 'WeaponLargeSword'
    elif 'Bow' in csv_file[index][0]: return 'WeaponBow'
    elif 'Spear' in csv_file[index][0]: return 'WeaponSpear'
    elif 'Head' in csv_file[index][0]: return 'ArmorHead'
    elif 'Lower' in csv_file[index][0]: return 'ArmorLower'
    elif 'Upper' in csv_file[index][0]: return 'ArmorUpper'
    print("Cannot determine weapon profile")
    sys.exit()

def msytEntry(csv_file, index):
    Desc = Description.createDesc(csv_file[index][12], 35)
    to_insert =  '  ' + csv_file[index][0] + '_Desc:\n'
    to_insert += '    contents:\n'
    to_insert += "      - text: \"" + Desc + "\"\n"
    to_insert += "  " + csv_file[index][0] + "_Name:\n"
    to_insert += '    contents:\n'
    to_insert += "      - text: \"" + csv_file[index][10] + "\"\n"
    to_insert += "  " + csv_file[index][0] + "_PictureBook:\n"
    to_insert += '    contents:\n'
    to_insert += "      - text: \"" + Desc + "\"\n"
    return to_insert


def newDesc(pack_name, csv_file, index):
    type = defineItemType(csv_file, index)

    descPath = pack_name + "\\content\Pack\Bootup_EUen.pack\Message\Msg_EUen.product.ssarc\ActorType\\"
    if not os.path.exists(pack_name + "\\content\Pack\Bootup_EUen.pack\\"):
        shutil.copytree("BASE_unbuilt\\content\Pack\Bootup_EUen.pack\\",  pack_name + "\\content\Pack\Bootup_EUen.pack\\")
    to_insert = msytEntry(csv_file, index)
    fout = open(descPath + "\\" + type + '.msyt', 'a')
    fout.write(to_insert)
    fout.close()

def newRules(pack_name):
    rulesPath = pack_name + '\\'
    checkAndDelete(rulesPath + 'rules.txt')
    fout = open(rulesPath + 'rules.txt', 'wt')
    fout.write('[Definition]\n')
    fout.write('titleIds = 00050000101C9300,00050000101C9400,00050000101C9500\n')
    fout.write('name = ' + pack_name + '\n')
    fout.write('path = {BCML: DON\'T TOUCH}/ = ' + pack_name + '\n')
    fout.write('description =  ' + pack_name + '\n')
    fout.write('version = 4\n')
    fout.write('image = \n')
    fout.write('url =  \n')
    fout.close()

def deleteLooseFiles(pack_name):
    os.system('del /F /Q ' + pack_name + '_build\.done')
    checkAndDelete(pack_name + '_build\.done')
    if not os.path.exists('trash'):
        os.system("mkdir trash")
    checkAndDelete(pack_name + '_build\content\System\Resource\ResourceSizeTable.product.srsizetable')
    os.system('del /F /Q ' + pack_name + '_build\content\System\Resource\ResourceSizeTable.product.srsizetable >nul')
