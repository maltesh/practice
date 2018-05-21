/*

 */
var bf_string_match = function(text, search) {
    for (let i = 0; i <= (text.length - search.length); i++) {
        if (text.substring(i, i + search.length) === search)
            return i
    }
    return -1
}

console.log(
    bf_string_match(
        'hello world',
        'worl1d'
    )
)