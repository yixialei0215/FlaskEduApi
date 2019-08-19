import hashlib


def pwd(txt):
    md5_ = hashlib.md5()
    md5_.update(txt.encode('utf-8'))
    return md5_.hexdigest()

if __name__ == '__main__':
    print(pwd('123456'))