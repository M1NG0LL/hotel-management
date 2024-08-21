def calc_bill(room_number, nights_number):
    bill = 0
    
    if 46 <= room_number <= 50:
        bill += 200
    elif 36 <= room_number <= 45:
        bill += 150
    elif 11 <= room_number <= 35:
        bill += 100
    else:
        bill += 50
    
    bill += (100 * nights_number)
    
    return bill