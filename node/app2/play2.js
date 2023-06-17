const str = "www.abc.xy";
const k = 87;
const str2 = str.split("");

const str3 = str2.map((value) => {
  //console.log(value);
  if (/^[A-Za-z]$/.test(value)) {
    const codePoint = value.codePointAt(0);
    //console.log(codePoint);
    let newCodePoint = codePoint + k;
    if (codePoint >= 97 && newCodePoint > 122) {
      newCodePoint = newCodePoint - 26;
    }
    if (codePoint < 97 && newCodePoint > 90) {
      newCodePoint = newCodePoint - 26;
    }
    let d1 = Math.floor(k / 26);
    if (k % 26 != 0) {
      d1++;
    }
    console.log("d1=" + d1);
    if (k > 26) {
      newCodePoint = newCodePoint - d1 * 26;
    }

    const newChar = String.fromCodePoint(newCodePoint);
    return newChar;
  }

  return value;
});

//console.log(str3);
console.log(str3.join(""));

console.log("f".codePointAt(0));

//102 119 + 87
