// https: //www.codewars.com/kata/rail-fence-cipher-encoding-and-decoding/train/javascript  

function encodeRailFenceCipher(s, numberRails) {

    let len = s.length;
    let temp = [];
    let temp_num = 0;
    let is_incrementing = true
    for (let i = 0; i < len; i++) {
        if (!temp[temp_num])
            temp[temp_num] = [];

        temp[temp_num].push(s[i]);

        if (is_incrementing) {
            temp_num++
        } else {
            temp_num--;
        }
        if (temp_num === numberRails - 1) {
            is_incrementing = false;
        }
        if (temp_num === 0) {
            is_incrementing = true;
        }
    }
    s = '';
    temp.forEach(function(elements) {
        s += elements.join('');

    });
    return s;
}

function decodeRailFenceCipher(string, numberRails) {
    if (!string || !numberRails) {
        console.log('invalid input');
        return '';
    }
    var div = 2 * (numberRails - 2) + 2,
        stringArr = string.split(""),
        len = parseInt(stringArr.length / div),
        remainder = stringArr.length % div,
        splitArr = [],
        tempArr = [],
        result = [];
    for (var i = 0; i < numberRails; i++) {
        splitArr.push(i == 0 || i == numberRails - 1 ? len : 2 * len);
    }
    if (remainder > numberRails) {
        splitArr = splitArr.map(function(num) {
            return num + 1;
        });
        remainder = remainder - numberRails;
        for (var j = numberRails - 2; j >= numberRails - remainder - 1; j--) {
            splitArr[j]++;
        }
    } else {
        for (var j = 0; j < remainder; j++) {
            splitArr[j]++;
        }
    }
    tempArr = splitArr.map(function(len) {
        var ans = stringArr.splice(0, len);
        return ans;
    });
    var float = 0,
        k = 0;

    function lineUp(isAdd) {
        if (k == string.length) {
            return;
        }
        result.push(tempArr[float].shift());
        k++;
        isAdd ? float++ : float--;
        if (float == numberRails) {
            float = float - 2;
            isAdd = false;
        }
        if (float == 0) {
            isAdd = true;
        }
        lineUp(isAdd);
    }

    lineUp(true);
    return result.join("");
}

function decodeRailFenceCipher(string, numberRails) {
    // code
    let cycle = (numberRails * 2) - 2;
    let reamind = numberRails % cycle;
    let total_cycles = Math.floor(numberRails / cycle);
}