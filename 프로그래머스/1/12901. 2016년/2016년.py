def solution(a, b):
    days = ['FRI', 'SAT','SUN', 'MON', 'TUE','WED','THU']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = sum(month[:a - 1]) + b
    
    return days[(day-1) % 7]
