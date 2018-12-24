<script>
  var DI = function (dependency) {
    this.dependency = dependency;
  };

DI.prototype.inject = function (f) {
  let bdy = f.toString()
  deps = bdy.toString().match(/^function\s*[^\(]*\(\s*([^\)]*)\)/m)[1].replace(/ /g, '').split(',');
  var body = bdy.slice(bdy.toString().indexOf("{") + 1, bdy.toString().lastIndexOf("}"));  
  
  var t = deps.map((dep) => this.dependency[dep])
  return function(){
    f.apply({},t.concat(Array.prototype.slice.call(arguments, 0)))
  }

  }

var deps = {
    'dep1': function () {return 'this is dep1';},
  'dep2': function () {return 'this is dep2';},
  'dep3': function () {return 'this is dep3';},
  'dep4': function () {return 'this is dep4';}
};

var di = new DI(deps);

var myFunc = di.inject(function (dep3, dep1, dep2) {
  console.log( [dep1(), dep2(), dep3()].join(' -> '))
  console.log( [dep1(), dep2(), dep3()].join(' -> '))
  return [dep1(), dep2(), dep3()].join(' -> ');
});


console.log(myFunc())


var DI = function (dependency) {
  this.dependency = dependency;
};

