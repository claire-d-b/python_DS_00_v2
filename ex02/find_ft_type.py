def all_thing_is_obj(object: any) -> int:
    if isinstance(object, str):
        print(object + " is in the kitchen : " + str(type(object)))
    try:
        iter(object)
    except TypeError:
        print("Type not found")     # is not iterable
    else:
        print(str(type(object))[8:-2].capitalize() + " : "
              + str(type(object)))
    finally:
        return 42

#       bloc 1
#  bloc 2      bloc 4
#       bloc 3
# try - except - else : bloc 4 is executed only if bloc 1 raises no error.
# try - except - else -finqlly :Whatever hapens, finally bloc will be executed.
# Running this alone does nothing. It is used as a module.
