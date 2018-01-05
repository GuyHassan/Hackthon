from firebase import firebase
import requests
import sys

print('blabla')
print("New Edit")
def main():
    def getHelp():
        """ returns the help string """
        str = '=========================================\n\nWelcome to The BB Manager!\n\n* Please notice that the first argument after the filename must be an option,         *\n* while the order of the rest doesn\'t matter                                          *\n* (except for secondary names,where last name must come after first name).            *\n* Also please separate the argument marks and the values with a blank space.          *\n* In addition you can use " " to mark few words as one argument(notes for example).   *\n* "<" and ">" are used to demonstrate the syntax,using them is not necessary.         *\n\nHere are your options:\n\n==========================================================================================================\n"-h" or "--help" to print this message\n==========================================================================================================\n"-li" or "--login" to log into The BB Manager:\n\nPlease use the following format:\n\'python tbbm.py -li <password> \'\nPlease note that you won\'t be asked to login again until you log out.\n==========================================================================================================\n"-lo" or "--logout" to log out The BB Manager\n==========================================================================================================\n"-cp" or "--changePassword" to change the current password:\n\nPlease use the following format:\n\'python tbbm.py -cp (or --changePassword) op: <old_password> np: <new_password> \n==========================================================================================================\n"-ut" or "--unitTests" to run the unit tests.\n==========================================================================================================\n"-ap" or "--addProject" to add a new project:\n\nPlease use the following format:\n\'python tbbm.py -ap (or --addProject) n: "Project Name"  \' \nwhile "n:" is used to mark the name of the project\n==========================================================================================================\n"-ep" or "--editProject" to edit an existing project:\n\nPlease use the following format:\n\'python tbbm.py -ep (or --editProject) id: <id> pn: "Updated Name" \'\nwhile "<id>" is the id of the project you want to update \nor\n\'python tbbm.py -ep (or --editProject) id: <id> s: "Updated State" \'\nwhile "s:" is to mark the state of your project (Active/Projected/Archived) \n==========================================================================================================\n"-dp" or "--deleteProject" to delete a project:\n\nPlease use the following format:\n\'python tbbm.py -dp (or --deleteProject) id: <id> \'\nwhile "<id>" is the id of the project you want to delete \n==========================================================================================================\n"-acat" or "--addCategory" to add a new category:\n\nPlease use the following format:\n\'python tbbm.py -acat (or --addCategory) n: "Category Name"  \' \nwhile "n:" is used to mark the name of the category\n==========================================================================================================\n"-ecat" or "--editCategory" to edit an existing category:\n\nPlease use the following format:\n\'python tbbm.py -ecat (or --editCategory) id: <id> catn: "Updated Name" \'\nwhile "<id>" is the id of the Category you want to update \n==========================================================================================================\n"-dcat" or "--deleteCategory" to delete a category:\n\nPlease use the following format:\n\'python tbbm.py -dcat (or --deleteCategory) id: <id> \'\nwhile "<id>" is the id of the category you want to delete \n==========================================================================================================\n"-ac" or "--addCitation" to add a new citation:\n\nPlease use the following format:\n\'python tbbm.py -ac (or --addCitation) <mark1>: <value1> <mark2>: <value2> ... \' \nHere is the list of the marks you can use ( most of them are mandatory ):\n"s:"   - source type (Available source types are: Book, Journal, Newspaper, Online, Magazine)\n"pid:" - the ID(s) of the project(s) that the citation is related to (for example pid: "1 2 3 4")\n"t:"   - title \n"fn:"  - main author\'s first name\n"ln:"  - main author\'s last name\n"cid:"   - the ID(s) of the category(ies) that the citation is relevant to \n"f:"   - will the file appear in the final version (use true/false only )\n"n:"   - a note\n"y:"   - publishing year \n"pub:" - publisher 		                  (optionally) \n"m:"   - publishing month 		          (optionally) \n"d:"   - publishing day  			  (optionally) \n"ps:"  - from page __     			  (optionally) \n"pe:"  - to page __       			  (optionally) \n"u:"   - URL              			  (optionally) \n"sfn:" - secondary author\'s first name            (optionally)\n"sln:" - secondary author\'s last name             (optionally)\n==========================================================================================================\n"-ec" or "--editCitation" to edit an existing citation:\n\nPlease use the following format:\n\'python tbbm.py -ec (or --editCitation) id: <id> <mark>: <new_value> \'\nwhile "<id>" is the id of the citation you want to update \nand   "<mark>" is the mark of the field you want to update \n==========================================================================================================\n"-dc" or "--deleteCitation" to delete an existing citation:\n\nPlease use the following format:\n\'python tbbm.py -dc (or --deleteCitation) id: <id> \'\nwhile "<id>" is the id of the citation you would like to delete\n==========================================================================================================\n"-pap" or "--printAllProjects" to print all the projects\n==========================================================================================================\n"-paca" or "--printAllCategories" to print all the categories\n==========================================================================================================\n"-paci" or "--printAllCitations" to print all the citations\n==========================================================================================================\n"-ppc" or "--printProjectCitations" to print all the citations that are related to a particular project:\n\nPlease use the following format:\n\'python tbbm.py -ppc (or --printProjectCitations) <id> \' \nwhile "<id>" is the id of the project you are intrested in\n==========================================================================================================\n"-pcc" or "--printCategoryCitations" to print all the citations that are related to a particular category:\n\nPlease use the following format:\n\'python tbbm.py -pcc (or --printCategoryCitations) <cid> \' \nwhile "<cid>" is the id of the category you are intrested in\n==========================================================================================================\n"-eieee" or "--exportIEEE" to export a bibliography in IEEE format to a textfile:\n\nPlease use the following format:\n\'python tbbm.py -eieee (or --exportIEEE) <id> \' \nwhile <id> is the id of the project you would like to export in IEEE format\nPlease note that only the citations that are marked as "Will be exported" will be exported.\n==========================================================================================================\n"-emla" or "--exportMLA" to export a bibliography in MLA format to a textfile:\n\nPlease use the following format:\n\'python tbbm.py -emla (or --exportMLA) <id> \' \nwhile <id> is the id of the project you would like to export in MLA format\nPlease note that only the citations that are marked as "Will be exported" will be exported.\n==========================================================================================================\n"-eh" or "--exportHarvard" to export a bibliography in Harvard format to a textfile:\n\nPlease use the following format:\n\'python tbbm.py -eieee (or --exportHarvard) <id> \' \nwhile <id> is the id of the project you would like to export in Harvard format\nPlease note that only the citations that are marked as "Will be exported" will be exported.\n==========================================================================================================\n"-eapa" or "--exportAPA" to export a bibliography in APA format to a textfile:\n\nPlease use the following format:\n\'python tbbm.py -eieee (or --exportAPA) <id> \' \nwhile <id> is the id of the project you would like to export in APA format\nPlease note that only the citations that are marked as "Will be exported" will be exported.\n==========================================================================================================\nFor more information please contact the developers.\nThank you for using The BB Manager :) \n\n=========================================\n'
        return str
    print(sys.argv[0],sys.argv[1])
    if sys.argv[1]:
        if '-h' in sys.argv[1] or '--help' in sys.argv[1]:
            print(getHelp())
        if '-paci' in sys.argv[0] or '--printAllCitations' in sys.argv[0]:
            printAllCitation()
        if '-pap' in sys.argv[0] or '--printAllProjects' in sys.argv[0]:
            printAllProject()


f = firebase.FirebaseApplication('https://hackathon2-f3e3b.firebaseio.com/')


def DeleteProject(numProject):
    f.delete("Users/Projects", ("Project" + str(numProject)))


def DeleteCitation(numCitation):
    f.delete("Users/Citations", ("Citation" + str(numCitation)))


def AddProject(id, state, name):
    f.put("Users/Projects", "Project" + str(id), {'ID': id, 'Name': name, 'State': state})


def EditProject(id, state, name):
    f.put("Users/Projects", "Project" + str(id), {'ID': id, 'Name': name, 'State': state})


def AddCitation(id=None, source=None, projectId=None, title=None, fName=None, lName=None, category=None, note=None,
                publisher=None,
                url=None, d=None, m=None, y=None, From=None, to=None):
    f.put("Users/Citations", "Citation" + str(id),
          {"Author": {'First Name': fName, 'Last Name': lName}, "Category IDs": category,
           "Date": {'Day': d, 'Month': m, 'Year': y}, "ID": id,
           "Pages": {'From': From, 'To': to}, 'Note': note,
           "Projects IDs": projectId, "Publisher": publisher, "Secondary Authors": 'guy', "Source": source,
           'Title': title, 'URL': url})


def addCategory(nCategory):
    f.put('Users/Categories', 'Category' + str(nCategory), {'Name': 'None', 'ID': 'None'})


def editCategory(catId, catName):
    f.put('Users/Categories', 'Category' + str(catId), {'Name': catName, 'ID': catId})


def delCategory(numCategory):
    f.delete('Users/Categories', 'Category' + str(numCategory))
    print('Category ' + str(numCategory) + ' has been deleted if it Existed')


def printAllProject():
    fb, cou = f.get("Users/Projects", None), 1
    print('\n' + 27 * '=' + '\n' + '__ That is all Projects __' + '\n' + 27 * '=')
    if not fb:
        print("Projects Not exist")
    else:
        for Proj in fb:
            print('Project ' + str(cou) + '\n' + 10 * '-')
            cou += 1
            for ProjCount in fb[Proj]:
                print(ProjCount, ':', fb[Proj][ProjCount])
            print(27 * '=')


def printAllCitation():
    fb, cou = f.get("Users/Citations", None), 1
    print('\n' + 27 * '=' + '\n' + '__ This is all Citations __' + '\n' + 27 * '=')
    if not fb:
        print("Projects Not exist")
    else:
        for citation in fb:
            print('Citation ' + str(cou) + '\n' + 10 * '-')
            cou += 1
            for x in fb[citation]:
                if isinstance(fb[citation][x], dict):
                    print(x, ' : ', end='')
                    for y in fb[citation][x]:
                        print('{' + y + ': ', fb[citation][x][y], end='},')
                    print()
                else:
                    print(x, ':', fb[citation][x])
            print(30 * '=')


main()
# addCategory(1)

# delCategory(1)
# AddCitation(1, 'Book', 2, 'Test Title', 'Guy', 'Hassan', 'Test Category', 'Test Note', 'Sce Engineer Students',
#             'www.sce.co.il', 23, '05', 1992, '35', '40')
# AddCitation(2, 'Book', 2, 'Test Title 2', 'yahav', 'mizrahi', 'Test Category', 'Test Note', 'Sce Engineer Students',
#             'www.sce.co.il', 18, '12', 1991, '35', '40')
# EditProject(1, 222, 'guy')
# PrintAllProject()
# PrintAllCitation()

# DeleteCitation(1)
# DeleteProject(3)
# AddProject(1,"Editing","Guy")#State:Active , Editing , Final
