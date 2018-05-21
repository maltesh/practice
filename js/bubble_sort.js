/*
Bruteforce Application for sorting problem is to compare adjacenet elements of the list and exchange 
them if they are ourt of order.By doing repatedly we end up "bubbling up" largest lement to last position 
on the list
 */

var bubble_sort = function(arr) {
    for (let i = 0; i < arr.length; i++) {
        let min = i;
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[min]) {
                let temp = arr[j];
                arr[j] = arr[min];
                arr[min] = temp;
            }
        }
    }
    return arr

}

var a = [2, 3, 1, 5, 4, 9, 16];
bubble_sort(a)