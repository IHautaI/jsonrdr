import json
import os


def menu():
    print("Commands:\n")
    print("Add new object: o")
    print("Add new value: v")
    print("Add new list: l")
    print("Exit: q")


def mod_menu():
    print("Commands:\n")
    print("Add items: a")
    print("Remove items: r")
    print("Exit: q")


def modify(objects, inp):
    os.system("clear")

    if inp in "aA":
        while inp not in "qQ":
            os.system("clear")
            menu()
            print(objects)
            inp = input("->")
            objects = loop(objects, inp)

    elif inp in "rR":
        objects = remove(objects)

    elif inp in "qQ":
        pass

    else:
        print("invalid input")

    return objects


def loop(objects, inp):
    os.system("clear")

    if inp in "oO":
        objects = add(objects, "o")
    elif inp in "vV":
        objects = add(objects, "v")
    elif inp in "lL":
        objects = add(objects, "l")
    elif inp in "qQ":
        pass
    else:
        print("invalid input")

    return objects


def list_loop(new_list, inp):
        os.system("clear")

        if inp in "oO":
            new_list = list_add(new_list, "o")
        elif inp in "vV":
            new_list = list_add(new_list, "v")
        elif inp in "lL":
            new_list = list_add(new_list, "l")
        elif inp in "qQ":
            pass
        else:
            print("invalid input")

        return new_list


def add(objects, which):

    if which == "o":
        new_item = {}
        print("Enter the key for this object:")
        name = input("->")

        os.system("clear")

        print("Now modifying new object " + name)
        inp = " "
        while inp not in "qQ":
            mod_menu()
            print(new_item)
            inp = input("->")
            new_item = modify(new_item, inp)

        objects[name] = new_item

    elif which == "v":
        print("Enter the key for this value:")
        name = input("->")
        print("Enter the value:")
        val = input("->")
        os.system("clear")
        objects[name] = val

    elif which == "l":
        new_list = []
        print("Enter the key for this list:")
        name = input("->")

        inp = " "
        os.system("clear")
        print("Now adding items to " + name)

        while inp not in "qQ":
            menu()
            print(new_list)
            inp = input("->")
            new_list = list_loop(new_list, inp)

        objects[name] = new_list

    return objects


def list_add(objects, which):

    if which == "o":
        new_item = {}
        os.system("clear")

        print("Now modifying new object")
        inp = " "
        while inp not in "qQ":
            mod_menu()
            print(new_item)
            inp = input("->")
            new_item = modify(new_item, inp)

        objects.append(new_item)

    elif which == "v":
        print("Enter the value:")
        val = input("->")
        os.system("clear")
        objects.append(val)

    elif which == "l":
        new_list = []

        inp = " "
        os.system("clear")
        print("Now adding items to new list")

        while inp not in "qQ":
            menu()
            print(new_list)
            inp = input("->")
            new_list = list_loop(new_list, inp)

        objects.append(new_list)

    return objects


def remove(objects):
    print("Remove which item?")
    items = enumerate(sorted(objects.keys()))

    for num, item in items:
        print(num + ") " + item)

    inp = input("->")

    if inp in range(0, len(items)):
        objects.pop(items.pop(inp)[1])

    else:
        print("invalid input")


def main(**kwargs):
    os.system("clear")
    item = {}

    if kwargs:
        try:
            with open(kwargs["file"], "r") as fh:
                item = json.load(fh)

        except ValueError:

            item = {}

            with open(kwargs["file"], "w") as fh:
                json.dump(item, fh)



        print(json.dumps(item, sort_keys=True, indent=4))
        inp = " "
        while inp not in "qQ":
            mod_menu()
            inp = input("->")
            item = modify(item, inp)
            os.system("clear")

        with open(kwargs["file"], "w") as fh:
            json.dump(item, fh)

    else:
        inp = " "
        while inp not in "qQ":
            menu()
            print(item)
            inp = input("->")
            item = loop(item, inp)
            os.system("clear")

        print("Enter file name or q to quit without saving:")
        name = input("->")

        if name not in "qQ":

            with open("./" + name + ".json", "w") as fh:
                json.dump(item, fh)
