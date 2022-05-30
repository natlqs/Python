# -*- coding:utf-8 -*-
'''learn how to use str.maketrans...'''

import string
normal = 'abcdefghijklmnopqrstuvwxyz'
changed = 'cdefghijklmnopqrstuvwxyzab'
transtab = str.maketrans(normal, changed)

original_str = input('please origin string')
translated_str = original_str.translate(transtab)
print(translated_str)



