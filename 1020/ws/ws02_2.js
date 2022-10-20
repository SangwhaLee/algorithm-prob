const users = [
  { name: 'John', age: 31, isMarried: true, balance: 100, },
  { name: 'Sarah', age: 22, isMarried: false, balance: 200, },
  { name: 'Ashley', age: 25, isMarried: true, balance: 300, },
  { name: 'Robert', age: 27, isMarried: false, balance: 400, },
  { name: 'Tom', age: 35, isMarried: true, balance: 500, },
]

//1.
users.forEach(element => console.log(element.name))

//2.
const married = users.filter(user => user.isMarried === true)
console.log(married)

//3.
const tom = users.find(user => user.name === 'Tom')
console.log(tom)

//4.
const newUsers = users.map(user => user.isAlive=true)
console.log(users)

//5.
const totalBalance = users.reduce((total, user) => total+user.balance, 0)
console.log(totalBalance)