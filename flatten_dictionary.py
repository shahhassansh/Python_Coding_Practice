## The below code takes input a dictionary and return flattened version of it.
##
## Input:
##
""" {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }
"""
##
## Output:
##
## {'Key1': '1', 'Key2': {'a': '2', 'b': '3', 'c': {'d': '3', 'e': {'': '1'}}}}

def flatten_dictionary(dictionary):
    output = {}
    helper(dictionary,"",output)
    return output

def helper(dictionary,prefix,output):
    for a in dictionary:
        if dictionary[a] != dict:
            if prefix == "":
                output[a] = dictionary[a]
            else:
                if a == "":
                    newprefix = prefix
                else:
                    newprefix = prefix + '.'+a
                output[newprefix] = dictionary[a]
        else:
            if prefix == "":
                output[a] = helper(dictionary[a],a,output)
            else:
                if a == "":
                    newprefix = prefix
                else:
                    newprefix = prefix+'.'+a
                output[newprefix] = helper(dictionary[a],newprefix,output)
    return output

dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

print(flatten_dictionary(dict))