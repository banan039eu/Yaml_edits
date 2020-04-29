import os
import sys
import functions as f
import shutil
import pathlib
import Flags
import Description

def newWeaponPack(input, pack_name):
    print("Creating file tree...")
    f.newFolderTree(pack_name)
    for index in range(len(input)):
        if index > 0:
            print("Adding " + input[index][0] + " to the pack")
            f.newActorpack(pack_name, input, index)
            f.newActorinfo(input, pack_name, index)
            f.newActorLink(pack_name, input, index)
            f.newGparam(pack_name, input, index)
            f.newModelList(pack_name, input, index)
            f.newModels(pack_name, input, index)
            f.newDesc(pack_name, input, index)
            Flags.changeFlags(pack_name, input, index)
    f.newRules(pack_name)
    print("Building with hyrule_builder...\n")
    os.system("hyrule_builder build --be " + pack_name)
    f.deleteLooseFiles(pack_name)
    os.system('move ' + pack_name + ' trash >nul')
