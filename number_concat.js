// function numbersConcatenation(n) {
//     let strlen = n.toString().length;
//     itObj = gen(n)
//     let temp = ''
//     for (const val of itObj) {
//       if (  (temp+val).toString().indexOf(n)>=0 )

//       {
//         return parseInt(temp);
//       }
//       temp = val.toString()
//     }


//   }

//   function* gen (n){
//     for (let i =0 ; i<=Math.pow(10,n) ; i++){
//        yield i 
//     }
//   }

function numbersConcatenation(n) {
    arr = n.toString().split('');
    al_combs= getCombinations(arr);

    len = al_combs;
    let res = [];
    for (let i =0 ; i<al_combs.length; i++){
        let a1 = parseInt(al_combs[i]);
        let a2 = parseInt(al_combs[i])+1;
        let a5 = parseInt(al_combs[i])-1;
        
      
        let a3 = a1.toString();
        let a4 = a2.toString();
//         console.log(a1,a2,typeof a1);
        if (  (a3+a4).indexOf(n.toString())>=0 ){
            res.push( a1);
        }
        res = res.sort()
        return res[0];
    }
}


function getCombinations(chars) {
    var result = [];
    var f = function (prefix, chars) {
        for (var i = 0; i < chars.length; i++) {
            result.push(prefix + chars[i]);
            f(prefix + chars[i], chars.slice(i + 1));
        }
    }
    f('', chars);
    return result;
}

function numbersConcatenation(n) {
    arr = n.toString().split('');
    al_combs= getCombinations(arr);

    len = al_combs;

    for (let i =0 ; i<al_combs.length; i++){
        let a1 = parseInt(al_combs[i]);
        let a2 = parseInt(al_combs[i])+1;
        let a5 = parseInt(al_combs[i])-1;
        
      
        let a3 = a1.toString();
        let a4 = a2.toString();
//         console.log(a1,a2,typeof a1);
        if (  (a3+a4).indexOf(n.toString())>=0 ){
            console.log(a1, '--')
        }
      
        if ( (a1+a5.toString()).indexOf(n.toString())  >=0 ){
            console.log(a1, "===")
            }
    }
}



