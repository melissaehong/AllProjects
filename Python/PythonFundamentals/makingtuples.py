my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

new_arr = []
for data in my_dict:
    tuple1 = (data, my_dict[data])
    new_arr.append(tuple1)
print new_arr
