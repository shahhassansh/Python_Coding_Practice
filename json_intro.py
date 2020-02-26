import json

## JSON is text written with Javascript Object Notation

## ------------------ ##
## Playing with JSON

person_dict = {'name': 'Bob',
'age': 12,
'children': None
}

person_json = json.dumps(person_dict)
#print(type(person_json)) ## str
person_final = json.loads(person_json)
#print(type(person_final)) ## dict

## --------------------------- ##
## Playing with another JSON

person_dict2 = [{'name': 'Bob',
'age': 12,
'children': 0
},
{'name': 'Shah',
'age': 45,
'children': 1
},
{'name': 'Charlie',
'age': 65,
'children': 3
},
{'name': 'Ardhy',
'age': 36,
'children': 1
}]

person_json2 = json.dumps(person_dict2)
print(type(person_json2)) ## str
person_final2 = json.loads(person_json2)
print(type(person_final2)) ## list

## Function to return age to people with only 1 child
def age_with_one_child(x):
    arr = []
    for a in x:
        print(a)
        if a['children'] == 1:
            arr.append(a['age'])
    return arr

print(age_with_one_child(person_final2))

## ----------------------------    
## Playing with Another JSON

office_dict = { "office": 
    {"medical": [
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }
    ],
    "parking": {
      "location": "premium",
      "style": "covered",
      "price": 750
    }
  }
}
## To dump into a JSON string
office_json = json.dumps(office_dict) #str
## To load JSON into a Dictionary
office_final = json.loads(office_json) #dict

# Function to return room number and use pair in dictionary for medical offices. 
def room_num_use(x):
    data = x["office"]["medical"] #list
    out = {}
    for a in data:
        s = a["room-number"]
        out[s] = a["use"]

    return out

print(room_num_use(office_final))





