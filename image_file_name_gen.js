// https: //www.codewars.com/kata/image-host-filename-generator/train/javascript

let i = 60466175
let generateName = () => (++i).toString(36)

function getRandomNo() {
    s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c';
    n = parseInt(Math.random() * 100)
    return s[n]
}

function generateName() {
    let rd = getRandomNo();
    let name = Math.round((new Date()).getTime()).toString().substr(0, 5)
    let cr = rd + name;
    if (photoManager.nameExists(cr)) {
        generateName();
    } else {
        return cr;
    }
}