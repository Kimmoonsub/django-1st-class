# 모두들 보쇼

title = 'Limjae'
date = "Limjae's Blind date"

class Blog():
    def __init__(self, title, date):
        self.title = title
        self.date = date
    def __str__(self):
        return '제목: {}, 날짜: {}'.format(self.title, self.date)    
Limjae = Blog('(주)와이엠', 19820714)
print(Limjae)





