import filecmp
import os
from pathlib import Path
from datetime import datetime
import shutil
from os import path


def rmdir(directory):
    directory = Path(directory)
    for item in directory.iterdir():
        if item.is_dir():
            rmdir(item)
        else:
            item.unlink()
    directory.rmdir()


def compare_difference_dir(beforechange, afterchange, forcecompare=False, skiptag=None):
    beforetimestamp = beforechange.split("/")[len(beforechange.split("/")) - 2]
    aftertimestamp = afterchange.split("/")[len(afterchange.split("/")) - 2]
    timestamp = "{:%Y%m%d_%H%M%S}".format(datetime.now())
    comparefile = (
        "compare"
        + "@"
        + beforetimestamp
        + "@"
        + aftertimestamp
        + "_"
        + timestamp
        + ".txt"
    )
    base_comp_dir = (
        "comparision/" + beforechange.split("/")[len(beforechange.split("/")) - 1]
    )
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
            additionalfilelist.append(beforechange + "/" + x)

    if right_only_files:
        for x in right_only_files:
            additionalfilelist.append(afterchange + "/" + x)

    returnList = []
    returnList.append(
        {
            "Compare Folder": "True",
            "Folder1": beforechange,
            "Folder2": afterchange,
            "Compare File Name": base_comp_dir + "/" + comparefile,
            "Content Match": "False",
            "Additional File Found": "",
            "Mismatch Content": "",
        }
    )

    if not additional_file_set or forcecompare:
        for x in common_files:
            returnList.append(
                compare_files(
                    beforechange + "/" + x,
                    afterchange + "/" + x,
                    base_comp_dir + "/" + comparefile,
                    skiptag=skiptag,
                )
            )

        returnList.append(
            compare_files(
                beforechange + "/" + x,
                afterchange + "/" + x,
                base_comp_dir + "/" + comparefile,
                forcewrite=True,
                additionalfile=additionalfilelist,
                skiptag=skiptag,
            )
        )
    else:
        print(
            "The following additional file present in any of the folder : "
            + str(additional_file_set)
        )

    return returnList


def compare_files(
    before, after, comparefile, forcewrite=False, additionalfile=None, skiptag=None
):
    diffdict = {}
    count = 0
    if not forcewrite and not additionalfile:
        with open(before, "r") as file1:
            with open(after, "r") as file2:
                for x, y in zip(list(file1), list(file2)):
                    count += 1
                    if x != y:
                        if not (skiptag and skiptag in x):
                            diffdict["Compare Folder"] = "False"
                            diffdict["Compare File Name"] = comparefile
                            diffdict["File1"] = file1.name
                            diffdict["File2"] = file2.name
                            diffdict["Additional File Found"] = ""
                            diffdict["Content Match"] = "False"
                            diffdict["Mismatch Content"] = (
                                diffdict["Mismatch Content"]
                                + "\n"
                                + "Line No:"
                                + str(count)
                                + " "
                                + x
                                + "Line No:"
                                + str(count)
                                + " "
                                + y
                                if "Mismatch Content" in diffdict.keys()
                                else "Line No:"
                                + str(count)
                                + " "
                                + x
                                + "Line No:"
                                + str(count)
                                + " "
                                + y
                            )

                if not diffdict:
                    diffdict["Compare Folder"] = "False"
                    diffdict["Compare File Name"] = comparefile
                    diffdict["File1"] = file1.name
                    diffdict["File2"] = file2.name
                    diffdict["Additional File Found"] = ""
                    diffdict["Content Match"] = "True"

        file2.close()
        file1.close()
    else:
        for x in additionalfile:
            diffdict["Compare Folder"] = "False"
            diffdict["Compare File Name"] = comparefile
            diffdict["File1"] = ""
            diffdict["File2"] = ""
            diffdict["Additional File Found"] = x
            diffdict["Content Match"] = "False"

    return diffdict


def write_to_file(adict, src):
    dst = adict.get("Compare File Name")
    if not path.exists(dst):
        shutil.copy(src, dst)

    with open(dst, "r") as file_read:
        readlist = file_read.readlines()

    file_read.close()

    if adict["Compare Folder"] == "True":
        readlist.insert(
            readlist.index(".\n"), adict["Folder1"] + "\n" + adict["Folder2"] + "\n"
        )
    elif adict["Content Match"] == "True":
        readlist.insert(
            readlist.index("...\n"),
            adict["File1"] + "------------" + adict["File2"] + "\n",
        )
    elif adict["Additional File Found"] != "":
        readlist.insert(readlist.index("....\n"), adict["Additional File Found"] + "\n")
    elif adict["Mismatch Content"] != "":
        readlist.insert(
            readlist.index("..\n"),
            adict["File1"]
            + "------------"
            + adict["File2"]
            + "\n"
            + adict["Mismatch Content"]
            + "\n",
        )

    with open(dst, "w") as file_out:
        for line in readlist:
            file_out.write(line)
    file_out.close()


def compare_master_folder(beforechange, afterchange, skiptag=None):
    comparision = filecmp.dircmp(beforechange, afterchange)
    common_files = comparision.common
    left_only_files = comparision.left_only
    right_only_files = comparision.right_only

    print(
        "====================================  Comparision Started  ====================================="
    )
    returnList = []
    for x in common_files:
        print(
            "Comparision Baseline Folder: "
            + beforechange
            + "/"
            + x
            + ", Post Baseline Folder: "
            + afterchange
            + "/"
            + x
        )
        returnList.append(
            compare_difference_dir(
                beforechange + "/" + x,
                afterchange + "/" + x,
                forcecompare=True,
                skiptag=skiptag,
            )
        )
        print("...Complete")
    print(
        "\n===============================  Congrats !! Comparision complete  ==============================\n"
    )

    if path.exists("compare_template.txt"):
        src = path.realpath("compare_template.txt")

    import pandas as pd

    df = pd.DataFrame(returnList)
    for i in range(len(df)):
        for j in range(len(df.columns)):
            if df.iat[i, j] is not None and df.iat[i, j]:
                write_to_file(df.iat[i, j], src)

    if left_only_files or right_only_files:
        left_only_files = map(lambda x: beforechange + "/" + x, left_only_files)
        right_only_files = map(lambda x: afterchange + "/" + x, right_only_files)
        print(
            "------------------------------------------ ! Warning ---------------------------------------------"
        )
        print(
            "Folders left out of comparision as corresponding folder in either source or destination is missing"
        )
        print(set(left_only_files).union(set(right_only_files)))
        print(
            "--------------------------------------------------------------------------------------------------"
        )


#########################################################################################################################
beforechange = "beforedeployement/production/20200403"
afterchange = "afterdeployement/production/20200403"

# compare_master_folder(beforechange, afterchange, skiptag="<DivideIntegerResult>")
compare_master_folder(beforechange, afterchange)
#########################################################################################################################
