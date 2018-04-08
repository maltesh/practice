//http: //www.codewars.com/kata/streams-endless-arrays/train/javascript
//https://stackoverflow.com/questions/310870/use-of-prototype-vs-this-in-javascriptx`

//Solve this once first one is done -> http://www.codewars.com/kata/prime-streaming-pg-13/train/javascript


function add(n) {
    var fn = function(x) {
        return add(n + x);
    };

    fn.valueOf = function() {
        return n;
    };

    return fn;
}

function add(n) {
    var next = add.bind(n += this | 0);
    next.valueOf = function() { return n; };
    return next;
}
//add(a)(2)(3)


var Stream = function(start, output, stepping) {
    this.start = start;
    this.output = output;
    this.stepping = stepping;
    // implement a constructor
};
Stream.prototype = {
    // implement the required functions
    head: function() {
        return this.output(this.start)
    },
    tail: function() {
        return new Stream(this.stepping(this.start), this.output, this.stepping)
    }
};
var increment = function(n) { return n + 1 };
var id = function(n) { return n };

var naturalNumbers = new Stream(0, id, increment);
console.log((naturalNumbers.head(), naturalNumbers.tail().tail().head())

        // Stream.prototype.head.valueOf = function() {
        //     return new Stream(this.stepping(this.start), this.output, this.stepping)
        // }



        var increment = function(n) { return n + 1 };
        var id = function(n) { return n };

        var naturalNumbers = new Stream(0, id, increment);

        Test.assertEquals(naturalNumbers.head(), 0) Test.assertEquals(naturalNumbers.tail().head(), 1) Test.assertEquals(naturalNumbers.tail().tail().head(), 2)