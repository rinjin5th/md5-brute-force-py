import sys
import hashlib
import argparse

allowChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def bfa(target, salt) :
    for length in range(32):
        result = _bfa(target, salt, length+1, length+1)        
        if result:
            return result
        print(str(length+1) + '桁目終了')

def _bfa(target, salt, length, count, base=''):
    if count == 0:
        md5 = hashlib.md5()
        plane = base+salt
        md5.update(plane.encode('utf-8'))
        if target == md5.hexdigest():
            return base
        else:
            return
    for c in allowChars :
        result = _bfa(target, salt, length, count-1, base + c)
        if result:
            return result

def main():
    parser = argparse.ArgumentParser(description='md5 brute force attack.')
    parser.add_parser('target', action='store', nargs=None, type=str, metavar='HASH')
    parser.add_parser('-s', '--salt', nargs='?', type=str)
    
    args = parser.parse_args()
    target = args.target
    salt = args.salt if args.salt else ''

    if len(target) != 32 :
        print('this is incorrect md5 hash.')
        sys.exit(1)
    print('hash is ' + target)
    result = bfa(target, salt)
    if not result:
        print('can\'t analized')
        sys.exit(1)
    print('analyzed hash. answer is ' + result)

if __name__ == '__main__':
    sys.exit(main())
