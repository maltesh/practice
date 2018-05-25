def identify_weapon(character):
    d = {'Laval':'Laval-Shado Valious',
        'Cragger':'Cragger-Vengdualize',
        'Lagravis':'Lagravis-Blazeprowlor',
        'Crominus':'Crominus-Grandorius',
        'Tormak':'Tormak-Tygafyre',
        'LiElla':'LiElla-Roarburn.'
    }
    return d.get(character,'Not a character')