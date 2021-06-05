(function() {
  // Variables
  const viewer = document.querySelector("#viewer") // Calculator screen where result is displayed
  const equals = document.querySelector("#equals") // Equal button
  const nums = document.querySelectorAll(".num") // List of numbers
  const ops = document.querySelectorAll(".ops") // List of operators
  let currentNum = "" // Current number
  let oldNum = "" // First number
  let resultNum // Result
  let operator // Operator

  // When: Number is clicked. Get the current number selected
  const setNum = function() {
    if (resultNum) { // If a result was displayed, reset number
      currentNum = this.getAttribute("value");
      resultNum = "";
    } else { // Otherwise, add digit to previous number (this is a string!)
      currentNum += this.getAttribute("value");
    }

    viewer.innerHTML = currentNum; // Display current number

  };




  // When: Operator is clicked. Pass number to oldNum and save operator
  const moveNum = function() {
    oldNum = currentNum;
    currentNum = "";
    operator = this.getAttribute("operator");

    equals.setAttribute("result", ""); // Reset result in attr
  };






  // When: Equals is clicked. Calculate result
  const displayNum = function() {

    // Convert string input to numbers
    oldNum = parseFloat(oldNum);
    currentNum = parseFloat(currentNum);

    if (operator == "plus"){
      resultNum = oldNum + currentNum;
    }
    else if (operator == "minus"){
      resultNum = oldNum - currentNum;
    }
    else if (operator == "times"){
      resultNum = oldNum * currentNum;
    }
    else if (operator == "divided by"){
      resultNum = oldNum / currentNum;
    }
    else { // If equal is pressed without an operator, keep number and continue
      resultNum = currentNum;
    }

    // Display result, finally!
    viewer.innerHTML = resultNum;
    equals.setAttribute("result", resultNum);

    // Now reset oldNum & keep result
    oldNum = 0;
    currentNum = resultNum;

  };






  // When: Clear button is pressed. Clear everything
  const clearAll = function() {
    oldNum = "";
    currentNum = "";
    viewer.innerHTML = "0";
    equals.setAttribute("result", resultNum);
  };







  /* The click events */

  // Add click event to numbers
  for (let i = 0, l = nums.length; i < l; i++) {
    nums[i].onclick = setNum;
  }

  // Add click event to operators
  for (let i = 0, l = ops.length; i < l; i++) {
    ops[i].onclick = moveNum;
  }

  // Add click event to equal sign
  equals.onclick = displayNum;

  // Add click event to clear button
  document.querySelector("#clear").onclick = clearAll;

  // Add click event to reset button
  document.querySelector("#reset").onclick = function() {
    window.location = window.location;
  };

}());