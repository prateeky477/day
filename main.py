import streamlit as st

days = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}
months = {
    "Jan": 0,
    "Feb": 3,
    "Mar": 3,
    "Apr": 6,
    "May": 1,
    "Jun": 4,
    "Jul": 6,
    "Aug": 2,
    "Sep": 5,
    "Oct": 0,
    "Nov": 3,
    "Dec": 5
}

month_of_30 = ["Jun", "Nov", "Apr", "Sep"]

month = st.selectbox("Select Month", months)
month_code = months[month]
year = int(st.number_input("Enter Year (1900-2099)",
                           min_value=1900, max_value=2099, step=1))
if month == "Feb" and year % 4 == 0:
    date = int(st.number_input("Enter date (1-29)",
                               min_value=1, max_value=29, step=1))
elif month == "Feb" and year % 4 != 0:
    date = int(st.number_input("Enter date (1-28)",
                               min_value=1, max_value=28, step=1))
elif month in month_of_30:
    date = int(st.number_input("Enter date (1-30)",
                               min_value=1, max_value=30, step=1))
else:
    date = int(st.number_input("Enter date (1-31)",
                               min_value=1, max_value=31, step=1))


if date < 0 and date > 31:
    print("Enter a valid date !!! (•_•)(•_•)")
if year < 1900 and year > 2099:
    print("Enter a valid year !!! (•_•)(•_•)")


def findDay(date, month_code, year):
    if year >= 1900 and year <= 1999:
        leap_year = (year-1900) // 4
        day = (date+month_code+year % 100+leap_year) % 7

    else:
        year = year-1900
        leap_year = year//4
        day = (date+month_code+year+leap_year) % 7

    return days[day]


if date != 0 and year != 0:
    if (st.button("SUBMIT")):
        day = findDay(date, month_code, year)
        st.text(day)
