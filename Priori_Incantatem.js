//  https: //www.codewars.com/kata/priori-incantatem/train/javascriptconst handler = {
//  https: //www.codewars.com/kata/priori-incantatem/train/javascriptconst handler = {



const MAX_PRIOR_SPELLS = 3
class Wand {
    constructor(spells) {
        this.my_stack = [];
        this.ignore_methods = ['deletrius', 'my_stack'];
        Object.assign(this, spells)
        return new Proxy(this, {
            get: function(target_obj, prop) {
                if (target_obj.ignore_methods.indexOf(prop) === -1 &&
                    typeof target_obj[prop] === 'function') {
                    target_obj.my_stack.unshift(prop);
                }
                return target_obj[prop];
            }
        })
    }
    prioriIncantatem() {
        return this.my_stack.slice(1, MAX_PRIOR_SPELLS + 1)
    }

    deletrius() {
        this.my_stack = ['deletrius']
    }
}