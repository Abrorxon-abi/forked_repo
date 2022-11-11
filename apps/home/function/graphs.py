from .dates import date_s, dates
from datetime import timedelta

def graph_1_paymant(x, dan, gacha):
    data = {'lable':[],'name':['Оборот', "Приболь"], "data":[[], []]}
    i, j = 0, 0,
    hour = date_s(x = dan, y = 0)
    circulation = 0
    profit = 0
    while gacha > hour: 
        if (len(x)- 1) >= i:
            if hour <= (x[i].created_at) < (hour + timedelta(hours = 2)): 
                if str(hour) not in data['lable']:
                    data['lable'].append(str(hour))
                    data['data'][0].append(x[i].sum)
                    data['data'][1].append(x[i].sum * x[i].tarif.fee)
                    circulation += x[i].sum
                    profit += (x[i].sum * x[i].tarif.fee)
                    i += 1
                    j += 1
                else:
                    data['data'][0][j-1] += x[i].sum
                    data['data'][1][j-1] += x[i].sum * x[i].tarif.fee
                    circulation += x[i].sum
                    profit += (x[i].sum * x[i].tarif.fee)
                    i += 1
            else:
                if str(hour) not in data['lable']:
                    data['lable'].append(str(hour))
                    data['data'][0].append(0)
                    data['data'][1].append(0)
                    j +=1
                    hour += timedelta(hours=2)
                else:
                    hour += timedelta(hours=2)
        else:
            if str(hour) not in data['lable']:
                data['lable'].append(str(hour))
                data['data'][0].append(0)
                data['data'][1].append(0)
                j +=1
                hour += timedelta(hours=2)
            else:
                hour += timedelta(hours=2)
    return {'data':data, 'circulation':circulation, 'profit':profit}


def graph_2_paymant(x, dan, gacha, z):
    data = {'lable':[], 'data': {}}
    for i in z:
        data['data'][i] = []
    i, j = 0, 0
    hour = date_s(x = dan, y = 0)
    while gacha > hour:
        if (len(x)- 1) >= i:    
            if hour <= (x[i].created_at) < (hour + timedelta(hours = 2)): 
                if str(hour) not in data['lable']:
                    data['lable'].append(str(hour))   
                    for key in data['data']:
                        if key == x[i].status.name:
                            data['data'][key].append(1)
                        else:
                            data['data'][key].append(0)
                    i += 1
                    j += 1
                else:
                    data['data'][x[i].status.name][j-1] += 1
                    i += 1
            else:
                if str(hour) not in data['lable']:
                    data['lable'].append(str(hour))
                    for key in data['data']:
                        data['data'][key].append(0)
                    j +=1
                    hour += timedelta(hours=2)
                else:
                    hour += timedelta(hours=2)
        else:
            if str(hour) not in data['lable']:
                data['lable'].append(str(hour))
                for key in data['data']:
                    data['data'][key].append(0)
                j +=1
                hour += timedelta(hours=2)
            else:
                hour += timedelta(hours=2)
    list_1 = list(data['data'].keys())
    list_2 = list(data['data'].values())
    data['data'] = list_2
    data['name'] = list_1
    return data

def graph_1_transfer(x, dan, gacha):
    data = {'lable':[],'name':['Оборот', "Приболь"], "data":[[], []]}
    i, j = 0, 0
    day = date_s(x = dan, y = 0)
    circulation = 0
    profit = 0
    while gacha > day: 
        if (len(x)- 1) >= i:
            if day <= (x[i].created_at) < (day + timedelta(days= 1)): 
                if str(day) not in data['lable']:
                    data['lable'].append(str(day.strftime("%d-%m-%Y")))
                    data['data'][0].append(x[i].sum)
                    data['data'][1].append(x[i].sum * x[i].fee)
                    circulation += x[i].sum
                    profit += (x[i].sum * x[i].fee)
                    i += 1
                    j += 1
                else:
                    data['data'][0][j-1] += x[i].sum
                    data['data'][1][j-1] += x[i].sum * x[i].fee
                    circulation += x[i].sum
                    profit += (x[i].sum * x[i].fee)
                    i += 1
            else:
                if str(day) not in data['lable']:
                    data['lable'].append(str(day.strftime("%d-%m-%Y")))
                    data['data'][0].append(0)
                    data['data'][1].append(0)
                    j +=1
                    day += timedelta(days= 1)
                else:
                    day += timedelta(days= 1)
        else:
            if str(day) not in data['lable']:
                data['lable'].append(str(day.strftime("%d-%m-%Y")))
                data['data'][0].append(0)
                data['data'][1].append(0)
                j +=1
                day += timedelta(days= 1)
            else:
                day += timedelta(days= 1)
        
    return {'data':data, 'circulation':circulation, 'profit':profit}


def graph_2_transfer(x, dan, gacha, z):
    data = {'lable':[], 'data': {}}
    for i in z:
        data['data'][i] = []
    i, j = 0, 0
    day = date_s(x = dan, y = 0)
    while gacha > day:
        if (len(x)- 1) >= i:    
            if day <= (x[i].created_at) < (day + timedelta( days= 1)): 
                if str(day) not in data['lable']:
                    data['lable'].append(str(day))   
                    for key in data['data']:
                        if key == x[i].status.name:
                            data['data'][key].append(1)
                        else:
                            data['data'][key].append(0)
                    i += 1
                    j += 1
                else:
                    data['data'][x[i].status.name][j-1] += 1
                    i += 1
            else:
                if str(day) not in data['lable']:
                    data['lable'].append(str(day))
                    for key in data['data']:
                        data['data'][key].append(0)
                    j +=1
                    day += timedelta(days= 1)
                else:
                    day += timedelta(days= 1)
        else:
            if str(day) not in data['lable']:
                data['lable'].append(str(day))
                for key in data['data']:
                    data['data'][key].append(0)
                j +=1
                day += timedelta(days= 1)
            else:
                day += timedelta(days= 1)
    list_1 = list(data['data'].keys())
    list_2 = list(data['data'].values())
    data['data'] = list_2
    data['name'] = list_1
    return data

