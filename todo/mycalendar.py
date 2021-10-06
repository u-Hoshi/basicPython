import calendar 
from datetime import datetime

class MyCalendar(calendar.LocaleHTMLCalendar):
  pass



def __init__(self,username,linked_date:dict):
  calendar.LocaleHTMLCalendar.__init__(self,
                                      firstweekday=6,
                                      locale="ja_jp")

  self.username=username
  self.linked_date=linked_date


def formatmonth(self,theyear,themonth,withyear=True):
  v=[]
  a=v.append

  a('<table class="table table-bordered table-sm" style="table-layout: fixed;">')
  a("\n")
  a(self.formatmonthname(theyear,themonth,withyear=withyear))
  a("\n")
  a(self.formatweekheader())
  a("\n")
  for week in self.monthdays2calendar(theyear,themonth):
    a(self.formatweek(week,theyear,themonth))
    a("\n")
  a('</table><br>')
  a("\n")
  return "".join(v)


