/*

 */
var bf_string_match = function(text, search) {
    for (let i = 0; i <= (text.length - search.length); i++) {
        console.log(text.substring(i, i + search.length))
        if (text.substring(i, i + search.length) === search)
            return i
    }
}

console.log(
    bf_string_match(
        'hello world',
        'world'
    )
)