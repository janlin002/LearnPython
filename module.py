# import sys
# print(sys.platform)

import sys
sys.path.append('modules')
print(sys.path)

import mod
print(mod.a(2, 3), 'mod')