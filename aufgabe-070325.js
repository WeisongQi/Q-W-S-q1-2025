// 示例数组
let arr = [1, 2, 3, 4, 5];

// 使用 keys()
// 输出数组的键（索引）。
for (let key of arr.keys()) {
    console.log(key);
}

// 使用 lastIndexOf()
// 返回指定元素在数组中的最后一个索引，如果不存在则返回 -1。
console.log(arr.lastIndexOf(3));

// 使用 length
// 返回数组的长度。
console.log(arr.length);

// 使用 map()
// 创建一个新数组，其结果是对原数组中的每个元素调用一个提供的函数后的返回值。
let mappedArr = arr.map(x => x * 2);
console.log(mappedArr);

// 使用 of()
// 创建一个新的数组实例，具有可变数量的参数。
let newArr = Array.of(6, 7, 8);
console.log(newArr);

// 使用 pop()
// 移除数组的最后一个元素，并返回该元素。
arr.pop();
console.log(arr);

// 使用 prototype
// 输出数组的原型对象，包含所有数组实例共享的属性和方法。
console.log(Array.prototype);

// 使用 push()
// 将一个或多个元素添加到数组的末尾，并返回数组的新长度。
arr.push(6);
console.log(arr);

// 使用 reduce()
// 对数组中的每个元素执行一个提供的函数，将其结果汇总为单个值。
let sum = arr.reduce((acc, val) => acc + val, 0);
console.log(sum);

// 使用 reduceRight()
// 从右到左对数组中的每个元素执行一个提供的函数，将其结果汇总为单个值。
let sumRight = arr.reduceRight((acc, val) => acc + val, 0);
console.log(sumRight);

// 使用 reverse()
// 反转数组中元素的顺序。
arr.reverse();
console.log(arr);

// 使用 shift()
// 移除数组的第一个元素，并返回该元素。
arr.shift();
console.log(arr);

// 使用 slice()
// 返回一个新的数组对象，这一对象是一个从开始到结束（不包括结束）选择的原数组的浅拷贝。
let slicedArr = arr.slice(1, 3);
console.log(slicedArr);

// 使用 some()
// 测试数组中的某些元素是否通过了提供的函数的测试。
let hasEven = arr.some(x => x % 2 === 0);
console.log(hasEven);

// 使用 sort()
// 对数组的元素进行排序，并返回数组。
arr.sort((a, b) => a - b);
console.log(arr);

// 使用 splice()
// 通过删除或替换现有元素或添加新元素来更改一个数组的内容。
arr.splice(1, 1, 9);
console.log(arr);

// 使用 toReversed()
// 返回一个新数组，其元素顺序与原数组相反。
let reversedArr = arr.toReversed();
console.log(reversedArr);

// 使用 toSorted()
// 返回一个新数组，其元素按提供的比较函数排序。
let sortedArr = arr.toSorted((a, b) => b - a);
console.log(sortedArr);

// 使用 toSpliced()
// 返回一个新数组，其中包含从原数组中删除或替换的元素。
let splicedArr = arr.toSpliced(1, 1, 10);
console.log(splicedArr);

// 使用 toString()
// 返回一个字符串，表示指定的数组及其元素。
console.log(arr.toString());

// 使用 unshift()
// 将一个或多个元素添加到数组的开头，并返回数组的新长度。
arr.unshift(0);
console.log(arr);

// 使用 valueOf()
// 返回数组对象的原始值。
console.log(arr.valueOf());

// 使用 with()
// 返回一个新数组，其中包含替换指定索引处的元素后的结果。
let withArr = arr.with(1, 11);
console.log(withArr);

// 使用 concat()
// 合并两个或多个数组，不改变现有数组，返回一个新数组。
let concatArr = arr.concat([7, 8, 9]);
console.log(concatArr);

// 使用 filter()
// 创建一个新数组，其包含通过所提供函数实现的测试的所有元素。
let filteredArr = arr.filter(x => x > 2);
console.log(filteredArr);

// 使用 find()
// 返回数组中满足提供的测试函数的第一个元素的值。
let found = arr.find(x => x > 2);
console.log(found);

// 使用 findIndex()
// 返回数组中满足提供的测试函数的第一个元素的索引。
let foundIndex = arr.findIndex(x => x > 2);
console.log(foundIndex);

// 使用 findLast()
// 返回数组中满足提供的测试函数的最后一个元素的值。
let foundLast = arr.findLast(x => x > 2);
console.log(foundLast);

// 使用 findLastIndex()
// 返回数组中满足提供的测试函数的最后一个元素的索引。
let foundLastIndex = arr.findLastIndex(x => x > 2);
console.log(foundLastIndex);

// 使用 flat()
// 按照指定的深度递归地将数组扁平化。
let nestedArr = [1, [2, 3], [4, [5, 6]]];
console.log(nestedArr.flat(2));

// 使用 forEach()
// 对数组的每个元素执行一次提供的函数。
arr.forEach(x => console.log(x));

// 使用 includes()
// 判断一个数组是否包含一个指定的值，根据情况返回 true 或 false。
console.log(arr.includes(3));

// 使用 indexOf()
// 返回数组中第一个与指定值相等的元素的索引，如果没有找到则返回 -1。
console.log(arr.indexOf(3));

// 使用 join()
// 将数组的所有元素连接成一个字符串，并返回这个字符串。
console.log(arr.join('-'));
