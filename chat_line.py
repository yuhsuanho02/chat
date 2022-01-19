from os import name
from posixpath import split


def read_file(file):
    lines = []
    with open(file, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines
def convert(lines):
    person = None
    Allen_word_acount = 0
    Allen_sticker = 0
    Allen_photo = 0
    Viki_word_acount = 0
    Viki_sticker = 0
    Viki_photo = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                Allen_sticker += 1
            elif s[2] == '圖片':
                Allen_photo +=1
            else:
                for m in s[2:]:
                    Allen_word_acount += len(m)
        if name == 'Viki':
            if s[2] == '貼圖':
                Viki_sticker += 1
            elif s[2] == '圖片':
                Viki_photo +=1
            else:
                for m in s[2:]:
                    Viki_word_acount += len(m)
    print('Allen說了', Allen_word_acount, '個字,傳了', Allen_sticker, '個貼圖,還有', Allen_photo, '張照片。')
    print('Viki說了', Viki_word_acount, '個字,傳了', Viki_sticker, '個貼圖,還有', Viki_photo, '張照片。')
def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)    
main()




