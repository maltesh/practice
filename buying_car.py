# https://www.codewars.com/kata/554a44516729e4d80b000012/train/python

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):

        if startPriceOld >= startPriceNew :
            return [0,startPriceOld - startPriceNew]

        total = 0
        mnths = 0

        spo = startPriceOld
        spn = startPriceNew

        while (total+spo) <= spn:

            mnths = mnths + 1
            if mnths %2 == 0 :
                percentLossByMonth = percentLossByMonth + 0.5
            total+= savingperMonth
            spo = spo - spo * percentLossByMonth/100
            spn = spn - spn * percentLossByMonth/100

        return [mnths, round(total - spn+spo)]

print (nbMonths(12000, 8000, 1000, 1.5))