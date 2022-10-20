for(let i=0;i<5;i++){
  result = ''
  for(let k=4-i;k>0;k--){
    result += ' '
  }
  for(let j=0;j<2*i+1;j++){
    result += '*'
  }
  console.log(result)
}