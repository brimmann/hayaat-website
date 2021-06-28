from django import template

from persiantools.jdatetime import JalaliDate
from persiantools.digits import en_to_fa
import datetime

register = template.Library()

@register.filter
def to_jalali(value):
    months_name = {
        1: 'حمل',
        2: 'ثور',
        3: 'جوزا',
        4: 'سرطان',
        5: 'اسد',
        6: 'سنبله',
        7: 'میزان',
        8: 'عقرب',
        9: 'قوس',
        10: 'جدی',
        11: 'دلو',
        12: 'حوت'
    }
    
    j_date = JalaliDate.to_jalali(value.year, value.month, value.day)
    j_date_display_string = en_to_fa(str(j_date.day)) + '/' + en_to_fa(months_name[j_date.month]) + '/' + en_to_fa(str(j_date.year))

    return j_date_display_string
    