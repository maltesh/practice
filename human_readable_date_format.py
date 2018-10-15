def format_duration(seconds):
    temp = []
    if not seconds:
        return 'now'
    consts = [31536000 ,86400,3600,60,1]

    consts_dict = {
        31536000 : 'years',
        86400:'days',
        3600: 'hours',
        60: 'minutes',
        1: 'seconds'
    }
    consts_dict_sglr = {
        31536000 : 'year',
        86400:'day',
        3600: 'hour',
        60: 'minute',
        1: 'second'
    }

    q,r=0,0
    for slot in consts:
        q,r = divmod(seconds,slot)
        if q >= 1:
            if q > 1:
                temp.append( str(q) + ' '+ str(consts_dict[slot]) )
            else:
                temp.append( str(q) + ' '+ str(consts_dict_sglr[slot]) )
                
            seconds = r
            print q,r , ' --->>'  ,seconds
        if r ==0 :
            break;
    if r>0:
        if r> 1:
            temp.append( str(r)+ ' ' + 'seconds')
        else:
            temp.append(str(r)+ ' ' + 'second')
    if len(temp)>=2:
        t_s = temp[-2:len(temp)]
        t_s = ' and '.join(t_s)
        temp.pop()
        temp.pop()
        temp = temp + [t_s]
        
    return ', '.join(temp)
    #your code here



if __name__ == '__main__':
    # print format_duration(1), "1 second"
    # print format_duration(62), "1 minute and 2 seconds"
    # print format_duration(120), "2 minutes"
    print   format_duration(132030240)
    # print format_duration(3662), "1 hour,"
