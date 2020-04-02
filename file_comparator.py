import filecmp
import os
from pathlib import Path
from datetime import datetime


def rmdir(directory):
    directory = Path(directory)
    for item in directory.iterdir():
        if item.is_dir():
            rmdir(item)
        else:
            item.unlink()
    directory.rmdir()


def compare_difference_dir(beforechange, afterchange, forcecompare=False):
    beforetimestamp = beforechange.split("/")[len(beforechange.split("/"))-2]
    aftertimestamp = afterchange.split("/")[len(afterchange.split("/"))-2]
    timestamp = "{:%Y%m%d_%H%M%S}".format(datetime.now())
    comparefile = "compare"+"@"+beforetimestamp+"@"+aftertimestamp+"_"+timestamp+".txt"
    base_comp_dir = "comparision/"+beforechange.split("/")[len(beforechange.split("/"))-1]
    compdir = os.path.join(*(base_comp_dir,))
    if not os.path.exists(compdir):
        os.makedirs(compdir)

    comparision = filecmp.dircmp(beforechange, afterchange)
    common_files = comparision.common
    left_only_files = comparision.left_only
    right_only_files = comparision.right_only

    additionalfilelist = []
    additional_file_set = set(left_only_files).union(set(right_only_files))

    if left_only_files:
        for x in left_only_files:
            additionalfilelist.append(beforechange + '/' + x)

    if right_only_files:
        for x in right_only_files:
            additionalfilelist.append(afterchange + '/' + x)

    initialList = []
    initialList.append("==========================================================================================================================\n")
    initialList.append("                                               <<<<< Comparing Folder >>>>>     \n                                         " + beforechange +
                       "\n                                         " + afterchange+"\n")
    initialList.append("==========================================================================================================================\n\n")
    write_to_file(base_comp_dir + '/' + comparefile, initialList)

    if not additional_file_set or forcecompare:
        for x in common_files:
            compare_files(beforechange + '/' + x, afterchange + '/' + x, base_comp_dir + '/' + comparefile)

        compare_files(beforechange + '/' + x, afterchange + '/' + x, base_comp_dir + '/' + comparefile, forcewrite=True,
                      additionalfile=additionalfilelist)
    else:
        print("The following additional file present in any of the folder : " + str(additional_file_set))


def compare_files(before, after, comparefile, forcewrite=False, additionalfile=None):
    difference = []
    if not forcewrite and not additionalfile:
        with open(before, 'r') as file1:
            with open(after, 'r') as file2:
                for x, y in zip(list(file1), list(file2)):
                    if x != y:
                        difference.append(
                            "                                                <<<<< Content Mismatch "
                            ">>>>>                                               \n")
                        difference.append(
                            "---------------------------------------------------------------------------------------------------------------------------\n")
                        difference.append(file1.name + "----->>>>>" + x)
                        difference.append(file2.name + "----->>>>>" + y)
                        difference.append("\n")
                if not difference:
                    difference.append("                                               <<<<< Content Matched "
                                      ">>>>>                                                 \n")
                    difference.append(
                        "---------------------------------------------------------------------------------------------------------------------------\n")
                    difference.append(file1.name + " <<<<<>>>>> " + file2.name)
                    difference.append("\n\n")
        file2.close()
        file1.close()
    else:
        for x in additionalfile:
            difference.append(
                "                                              <<<<< Additional File Found "
                ">>>>>                                          \n")
            difference.append(
                "---------------------------------------------------------------------------------------------------------------------------\n")
            difference.append("<<<<< File Name  >>>>> " + x)
            difference.append("\n\n")

    write_to_file(comparefile, difference)


def write_to_file(comparefile, difference):
    with open(comparefile, 'a') as file_out:
        for line in list(difference):
            file_out.write(line)

    file_out.close()


def compare_master_folder(beforechange,afterchange):
    comparision = filecmp.dircmp(beforechange, afterchange)
    common_files = comparision.common
    left_only_files = comparision.left_only
    right_only_files = comparision.right_only

    print("====================================  Comparision Started  =====================================")

    for x in common_files:
        print("Comparision Baseline Folder: "+beforechange+'/'+x+", Post Baseline Folder: "+afterchange+'/'+x)
        compare_difference_dir(beforechange+'/'+x, afterchange+'/'+x, forcecompare=True)
        print("...Complete")
    print("\n===============================  Congrats !! Comparision complete  ==============================\n")

    if left_only_files or right_only_files:
        left_only_files = map(lambda x : beforechange+'/'+x, left_only_files)
        right_only_files = map(lambda x: afterchange + '/' + x, right_only_files)
        print("------------------------------------------ ! Warning ---------------------------------------------")
        print("Folders left out of comparision as corresponding folder in either source or destination is missing")
        print(set(left_only_files).union(set(right_only_files)))
        print("--------------------------------------------------------------------------------------------------")


beforechange = "beforedeployement/qa1/20200402"
afterchange = "afterdeployement/qa1/20200402"

compare_master_folder(beforechange, afterchange)
