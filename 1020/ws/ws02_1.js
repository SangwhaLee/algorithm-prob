const name = 'Tom'
console.log(`Hi, my name is ${name}`)

const add = (x,y) => x+y

const tom = {
  name,
  introduce(){
    console.log(`Hi, my name is ${this.name}`)
  }
}

console.log(add(1,2))
tom.introduce()