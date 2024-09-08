def NULL_not_found(object: any):
    match str(type(object))[8:-2].capitalize():
        case 'Nonetype':
            print("Nothing: ", object, type(object))
            return 0
        case 'Float' | 'Int':
            if object != object:
                print("Cheese: ", object, type(object))
                return 0
            elif object == 0:
                print("Zero: ", object, type(object))
                return 0
            else:
                print("Type not found")
                return 1
        case 'Str':
            if object:
                print("Type not found")
                return 1
            else:
                print("Empty: ", object, type(object))
                return 0
        case 'Bool':
            print("Fake: ", object, type(object))
            return 0
        case _:
            print("Type not found")
            return 1

# You can combine several literals in a single pattern using | (“or”):

# Ex: case 401 | 403 | 404:
# return "Not allowed"
