### 1.

```py
def duplicated_letters(word):
  exists = []
  duplicates = []
  for letter in word:
    if letter in exists:
      duplicates.append(letter)
    else:
      exists.append(letter)
  
  return list(set(duplicates))
```

### 2.

```py
def low_and_up(word):
  tmp = []
  tmp.extend(word)
  if tmp[0].islower():
    for i in range(1, len(tmp)):
      if i%2:
        tmp[i] = tmp[i].upper()
      else:
        tmp[i] = tmp[i].lower()
  else:
    for i in range(1, len(tmp)):
      if i%2:
        tmp[i] = tmp[i].lower()
      else:
        tmp[i] = tmp[i].upper()
  
  return ''.join(tmp)
```

### 3.

```py
def lonely(numbers):
  alone = []
  before_idx = 0
  for idx, value in enumerate(numbers):
    if idx ==0 :
      alone.append(value)
    else:
      if numbers[idx] != numbers[idx-1]:
        alone.append(value)
  
  return alone

```