// https://www.codewars.com/kata/priori-incantatem/train/javascript
// class Wand{

//     //  let my_stack:Array<any>=new Array<any>;
//      constructor(spells){
//          if (spells){
//              Object.keys(spells).forEach(element => {
//                 this[element] =>{ 
//                     this.my_stack.push(element);
//                     return spells[element];
//                 }
//              });
//          }
//     }

//     prioriIncantatem(){
//     }

//     deletrius(){
//     }
// }

// function Wand(spells){
//     this.max_stack= ['test'];
//     if (spells){
//        Object.keys(spells).forEach(element => {
//          this[element] = spells[element];
//        });
//     }
// }
// Wand.prototype.get = function(obj,prop){
//   console.log(obj,prop,this);
//   if (this.hasOwnProperty(prop)){
//     this.max_stack.push(prop)
//   }
  
// }
// Wand.prototype.prioriIncantatem=function(){
//   return this.max_stack;
  
// }
// Wand.prototype.deletrius=function(){
//   this.max_stack=[]
// }

// let spls = {
//   alohomora: function() { console.log('unlocked!'); },
//   lumos: function() { console.log('let there be light!'); },
//   wingardiumLeviosa: function() { console.log('levitation!'); }
// };


// const Wand = new Proxy(Wand,{})

const handler = {
  construct(objTarget, args, oldConstructor) {
     console.log(objTarget);
     
     
     return new objTarget(...args)
  },
  set(target, key, value) {
    console.log(`Setting value ${key} as ${value}`)
    target[key] = value;
  },
  get(target, key) {
    console.log(`Reading value from ${key}`)
    return target[key];
  },
};

function test(args){
  if (args){
    Object.keys(args).forEach((ele)=>{
      this[ele] = args[ele];
    })
  }
}


let spls = {
  alohomora: function() { console.log('unlocked!'); },
  lumos: function() { console.log('let there be light!'); },
  wingardiumLeviosa: function() { console.log('levitation!'); }
};

const Wand = new Proxy(test,handler);

a = new Wand(spls);
a.alohomora();
console.log('121');