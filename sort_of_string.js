function sortString(s1,ordering) {
    let s2 = ''
    let o2 = new Set(ordering).forEach((a)=>{
      if(a){
        var re = new RegExp(a, 'g');
        let count = (s1.match(re) || []).length ;
        s1 = s1.replaceAll(a,'')      
        s2 = s2.padEnd(s2.length+count, a);
      }
    });

    if(s1){
        s2  =  s2+ s1.split('').sort().join('')
    }    
    return s2
  }
  sortString("foos", "of")