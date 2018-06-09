// #https://www.codewars.com/kata/consonant-value/train/javascript
// https: //www.codewars.com/kata/vowel-consonant-lexicon/train/javascript
// https: //www.codewars.com/users/macobo/completed
// https://www.codewars.com/kata/myjinxin-katas-number-003-crossword-puzzle/train/javascript
function solve(s) {
    let temp = [];
    let temp1 = [];
    let temp2 = [];
    let temp3 = [];
    let temp4 = [];
    var split_arr = s;
    let asci_lowercase = 'abcdefghijklmnopqrstuvwxyz';

    split_arr = split_arr.split('a')
    temp.push(...split_arr)

    temp.forEach((ele) => {
        temp1.push(...(ele.split('e')))
    })
    temp1.forEach((ele) => {
        temp2.push(...(ele.split('i')))
    })
    temp2.forEach((ele) => {
        temp3.push(...(ele.split('o')))
    })
    temp3.forEach((ele) => {
        temp4.push(...(ele.split('u')))
    })
    let ss = 0;
    let fin = [];
    temp4.forEach((e) => {
        if (e) {
            e = e.split('')
            ss = 0
            e.forEach((t) => {
                ss += asci_lowercase.indexOf(t) + 1
            })
            fin.push(ss)

        }
    })
    return Math.max(...fin)
};

function solve(s) {
    let arr = s.replace(/[aeiou]/gi, ' ')
        .split(' ')
        .filter(x => x != '')
        .map(x => x.split('')
            .map(y => y.charCodeAt() - 96)
            .reduce((a, b) => a + b))
    return Math.max(...arr)
};
solve("zoedaics")


function capitalize(s) {

    let cs = ''
    let ss = ''
    for (var i = 0; i < s.length; i++) {
        if (i % 2 == 0) {
            cs += s[i].toUpperCase()
            ss += s[i].toLowerCase()
        } else {
            cs += s[i].toLowerCase()
            ss += s[i].toUpperCase()
        }
    }
    return [cs, ss];

};