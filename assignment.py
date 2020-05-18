class assignment:

    str2 = "Error MSB003: Dir\source\app\app.cpp"
    str3 = "FATAL Error: Could not read files.txt"

# convert str1 into uppercase
    def upperfunctionstring(self):
        str1 = "Error MSB123: Directory\File\Solution\project.sln"
        str1 = str1.upper()
        print("This is Upper case String:- " + str1)
        print()
# Split the given string and print the substrings individually.
# Example: if the string is str = "Error MSB123: Directory\File\Solution\project.sln" then print Error, MSB123, Directory, File, Solution, project
# in different variables.

    def splitthesubstring(self):
        str1 = "Error MSB123: Directory\File\Solution\project.sln"
        str1 = str1.split()
        strmain = str(str1).replace('\\', ' ')
        strmain = str(strmain).split(' ')
        print("This is split of line: " + str(strmain))
        print()


# Read the error.log file from your code and print each substring in independent variables.
# Write your code here
    def printSubstringFromFile(self):

        f = open('D:\PythonLearning\error.log', "r")
        allLines = f.readlines()
        strsplit = str(allLines).split()
        strsplit = str(strsplit).split('\\')
        print("This is spliting of each word from file: ")
        print()
        for val in strsplit:
            if(val):
                print(val)
        print()
# Consider the list below and perform  the tasks given
# Sort the list
# reverse the list
# create a new list copyList and copy the elements of List into copyList
# Print elements form index 2 to 6 in List.
# Print last 3 elements of the list List.

    #List = [6, 8, 9, 4, 5, 12, 13]

    def printSortList(self):
        List = [6, 8, 9, 4, 5, 12, 13]
        List.sort()
        print("This is Sorted List: " + str(List))
        print()

    def printReverse(self):
        List = [6, 8, 9, 4, 5, 12, 13]
        List.reverse()
        print("This is Reverse List: " + str(List))
        print()

    def printLast3(self):
        List = [6, 8, 9, 4, 5, 12, 13]
        result = List[-3:]
        print("The last 3 numbers of list: " + str(result))
        print()

    def copyAllList(self):
        List = [6, 8, 9, 4, 5, 12, 13]
        copyList = list()
        copyList = List.copy()
        print("This is copy of List: " + str(copyList))
        print()

    def printInCondition(self):
        List = [6, 8, 9, 4, 5, 12, 13]
        result = List[2:]
        print("This is the element from 2 to 6: " + str(result))
        print()

obj = assignment()

obj.upperfunctionstring()
obj.splitthesubstring()
obj.printSortList()
obj.printReverse()
obj.printLast3()
obj.copyAllList()
obj.printInCondition()
obj.printSubstringFromFile()