// https: //www.codewars.com/kata/whats-the-next-number/discuss

function nextNumber(seq) {
    let seq_dif = seq.slice(0, -1).map((val, index) => seq[index + 1] - v);
    let fin_dif = seq_dif.slice(0, -1).map((val, index) => seq_diff[index + 1] - v);
    let dif = seq_dif.pop() + fin_dif.pop();
    return seq[seq.length - 1] + dif


}