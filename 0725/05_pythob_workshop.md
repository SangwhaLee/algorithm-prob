### 1.
```py
def get_dict_avg(dic):
    return sum(dic.values())/len(dic)
```

### 2.

```py
def count_blood(blood_list):
    blood_cnt = {}
    a_cnt = blood_list.count('A')
    b_cnt = blood_list.count('B')
    o_cnt = blood_list.count('O')
    ab_cnt = blood_list.count('AB')

    blood_cnt.update('A'= a_cnt)
    blood_cnt.update('B'= b_cnt)
    blood_cnt.update('O'= o_cnt)
    blood_cnt.update('AB' = ab_cnt)

    return blood_cnt

```