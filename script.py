from datetime import date

def get_day_of_year():
  today = date.today()
  day_of_year = today.strftime('%j')
  return day_of_year

if __name__ == "__main__":
  day = get_day_of_year()
  print(day)
