const arr1 = [1, 2, 3, 4, 5];

const persons = [
  {
    first: "Zohar",
    last: "Shalom",
    age: 32,
    amount: 400
  },
  {
    first: "Zohar",
    last: "Shalom",
    age: 22,   
    amount: 270 
  },
];

const arr2 = arr1.map((value) => {
  return value * 3;
});

const person2 = persons.map((value) => {
  return {
    value.age * 3
    value.amount *7
}
});

console.log(arr1);
console.log(arr2);
console.log(person2);
