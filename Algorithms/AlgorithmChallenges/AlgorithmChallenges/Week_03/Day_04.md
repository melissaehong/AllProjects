##Objects Day 4 ([Solution](Day_04.js))

###How many items?
Given an object, `return` the number of items in the object. For example, given:

```js
{
  name: "Charlie",
  age: 29,
  sayHello: function() {
    console.log("Hello!")
  }
}
```

Your function should return `3`.

###Part II
Instead of returning a single number, return another object with two key-value pairs, `properties` and `methods`. The value associated with `properties` should be a count of the initial object's non-function items. The value associated with `methods` should be a count of the initial object's functions. Given the example object above, you'd return the following:

```js
{
  properties: 2,
  methods: 1
}
```
