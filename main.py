"""
This will import all modules with name group*.py
and print the result of the corresponding tweet() function
implemented in group*.py.
"""
#HELLO!
import os

for filename in os.listdir("."):
    if filename.startswith("group") and filename.endswith(".py"):
        module_name = filename[:-3]
        try:
            module = __import__(module_name)
            group_name = module_name.replace("group", "") \
                                    .replace("_", "") \
                                    .replace("-", "")
            print("group {0} says: {1}".format(group_name, module.tweet()))
        except ImportError:
            pass
