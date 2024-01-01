'''
if -elif -else 格式 
'''

def is_week_day(day):
    if day == '1' or day == '一':
        print('星期一')
    elif day == '2' or day == '二':
        print('星期二')
    elif day == '3' or day == '三':
        print('星期三')
    elif day == '4' or day == '四':
        print('星期四')
    elif day == '5' or day == '五':
        print('星期五')
    elif day == '6' or day == '六':
        print('星期六')
    elif day == '7' or day == '日':
        print('星期日')
    else:
        print('输入的日期不对')


d = input('input:')
is_week_day(d)
    
    