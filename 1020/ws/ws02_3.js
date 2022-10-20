// 1-1
const savedFile = {
  name: 'profile',
  extension: 'jpg',
  size: 29930
}
function fileSummary(file) {
  const { name, extension, size } = file
    console.log(`The file ${name}.${extension} is size of ${size} bytes.`)
}
fileSummary(savedFile);

// 1-2
const data = {
  username: 'myName',
  password: 'myPassword',
  email: 'my@mail.com',
}

const { username, password, email } = data

// 2
function addNumbers(...theArgs) {
  return theArgs.reduce((sum, number) => { 
    return sum + number
  }, 0)
}

// 3-1
const defaultColors = ['red', 'green', 'blue'];
const favoriteColors = ['navy', 'black', 'gold', 'white']
const palette = [...defaultColors,...favoriteColors]

// 3-2
const info1 = { name: 'Tom', age: 30 }
const info2 = { isMarried: true, balance: 3000 }
const fullInfo = {...info1, ...info2}