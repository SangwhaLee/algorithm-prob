function palindrome(str) {
    //
    const reversedStr = str.split("").reverse().join("");
    if(str === reversedStr) return true
    else return false
  }

  console.log(palindrome('LeveL'))
  console.log(palindrome('hi'))