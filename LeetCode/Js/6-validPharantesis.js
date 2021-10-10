// https://leetcode.com/problems/valid-parentheses

/**
 * @param {string} s
 * @return {boolean}
 */
 var isValid = function(s) {
	let stack = []
	for (char of s) {
		// Char is one of closings, there must be openings in the stack
		if (')}]'.includes(char) && !stack) return false

		// Add openings to the stack
		if ('({['.includes(char)) stack.push(char)

		// Char is closing, last opening in the stack must match
		else if (char == ')') {
			if (stack.pop() != '(') return false
		}
		else if (char == '}') {
			if (stack.pop() != '{') return false
		}
		else if (char == ']') {
			if (stack.pop() != '[') return false
		}
  }
  return stack.length == 0
}
