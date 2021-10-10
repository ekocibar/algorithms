// https://leetcode.com/problems/pascals-triangle/

/**
 * @param {number} numRows
 * @return {number[][]}
 */
const generate = (numRows, arr=[[1], [1, 1]]) => {
    // numRows=1
    if (numRows === 1) return [[1]]

    // Stop when row size reaches the limit
    if (arr.length === numRows) return arr

    // Get the middle part of the new row
    let midOfNewRow = []
    const lastRow = arr[arr.length - 1]
    for (let i=0; i<lastRow.length-1; i++) {
        midOfNewRow.push(lastRow[i] + lastRow[i+1])
    }
    const newRow = [1, ...midOfNewRow, 1]
    arr.push(newRow)
    return generate(numRows, arr)
}
