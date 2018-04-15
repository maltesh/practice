function sumIntervals(intervals){
  let s = 0;
  let min = 0;
  let max = 1;
  let diff =[];
  for( var i = 0 ; i < intervals.length -1 ; i++){
    base = intervals[i]
    for(var j = i+1; j< intervals.length; j++){      
      interval = intervals[j];     
      
      if(interval && base){
        
        if(base[min] <= interval[min]){        
          if(base[max]>=interval[min] &&    base[max]<= interval[max]){ 
            intervals[i]=null;
            intervals[j] = [base[0],interval[max]]
            diff.push([base[0],interval[max]]);
          }
          if(base[max]>interval[max]){
            diff.push(base)
            intervals[i]=null
            intervals[j]=base
          }
      }
  }
}
 
  }
     intervals.map((interval)=>{
      if(interval)
        s+= (interval[1]-interval[0]);
    })
    return s
    


}

# //Better ones
function sumIntervals(intervals){
  return intervals
    .sort(function(a, b){
      if (a[0] < b[0]) return -1;
      if (a[0] > b[0]) return 1;
      return 0;
    })
    .reduce(function(acc, interval) {
      if (interval[1] > acc.top) {
        acc.total += interval[1] - Math.max(interval[0], acc.top);
      }
      acc.top = Math.max(interval[1], acc.top);
      return acc;
    }, {total: 0, top: 0})
    .total;
}