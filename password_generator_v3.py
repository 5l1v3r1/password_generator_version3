#!/usr/bin/env python

import random

def random_funct():
 
 # 63 random alpha-numeric characters (a-z, A-Z, 0-9)
 
 char = 'qKVmen[SkR\VMg~X{1+I{.weNH@Ei`DeH)I_N-k!2q^RKV7lWn&<^LuCg)4TI9C'
 length_object = raw_input('Choose your length password :')
 length_object = int(length_object)

 for b in range(15):
  password = ''

  for h in range(length_object):
   password += random.choice(char)

  print(password)

def main():

 random_funct()

main()
