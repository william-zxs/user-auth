# -*- coding=utf-8 -*-
#!/usr/bin/env python
import crypt

crypt_type = ''
crypt_str = ''
crypt_pw = ''


def user_auth(user, password):
    try:
        with open("/etc/shadow", "r") as sa:
            for line in sa:
                row = line.split(":")
                if row[0] == user:
                    crypt_pw = row[1]
                    _, crypt_type, crypt_str = row[1].split("$", 2)
                    break

            salt = "${}${}".format(crypt_type, crypt_str)
            res = crypt.crypt(password, salt)
            if res == crypt_pw:
                return True
            else:
                return False
    except IOError as e:
        if e.errno == 2:
            print "ERROR: Please confirm if the system is linux!"
            return
        if e.errno == 13:
            print "ERROR: need to be root,please confirm your permission!"
            return


if __name__ == '__main__':
    res = user_auth("root", "abcd1234")
    if res == True or res == False:
        print res
