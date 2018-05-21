/*

We start this sort by scanning given list to find its smallest element and exchange it with first element,
putting smallest element in its final position in the sorted list
 */


var selection_sort = function(arr) {
    for (var i = 0; i < arr.length; i++) {
        min = i;
        for (var j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[min]) {
                min = j;
            }
        }
        var temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp
    }
    return arr;
}

var a = [2, 3, 1, 5, 4, 9, 16];
selection_sort(a)