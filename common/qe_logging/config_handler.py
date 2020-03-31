import os


def get_dictionary_from_config(env):
    returnDict = {}
    dirPath = os.path.join("projectname", "configs", f"{env}.config")
    if os.path.exists(dirPath):
        try:
            fileOpen = open(dirPath, "r")
            for x in fileOpen:
                splitList = x.split("=")
                returnDict[splitList[0].strip()] = splitList[1].strip()
            fileOpen.close()
            return returnDict
        except FileNotFoundError:
            print(f"{env}.config file not found")
