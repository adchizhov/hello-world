
/*
0. Создать массив с 50 записями: строками с числами ('123') 
и строками с текстом ('abc'), на его основе создать новый массив, 
где будут все числа из первого и число 8 вместо текста.
*/
console.log('EXERCISE 0')
var arrayNumbLet = []

for (i = 0; i < 50; i++) {
	if (i % 2 == 0) {
		arrayNumbLet.push('123');
	} else {
		arrayNumbLet.push('abc');
	}
}

console.log(arrayNumbLet);

var arrayWith8 = arrayNumbLet.slice();

for (e in arrayWith8) {
	if (arrayWith8[e] == 'abc') {
		arrayWith8[e] = 8;
	} else {
		arrayWith8[e] = 123 ;
	}
}

console.log(arrayWith8);

/*
1. Напишем функцию, которая бы сортировала массив, и 
возвращала занчение, сколько объектов изменили свой порядок. 
Пример: mySortCount([0, 2, 1]) # => 2
*/
console.log('EXERCISE 1')
var arrayNumbers = [0, 1, 4, 2, -1];

function mySortCount(x) {
	var count = 0
	arrayNewNumbers = x.slice();
	arrayNewNumbers.sort();
	console.log(x);
	console.log(arrayNewNumbers);
	for (i = 0; i <= x.length; i++) {
		if (x[i] !== arrayNewNumbers[i]) {
			count = count + 1;
		}
	}
	return count;
}

console.log(mySortCount(arrayNumbers));

/*
2. Напишите программу, которая выводит на экран числа от 1 до 100. 
При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz», 
а вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5, 
то программа должна выводить слово «FizzBuzz».
*/
console.log('EXERCISE 2')
for (i = 1; i <=100; i++) {
	if ((i % 3 === 0) && (i % 5 === 0)) {
		console.log('FizzBuzz');
	} else if (i % 3 === 0) {
		console.log('Fizz');
	} else if (i % 5 === 0) {
		console.log('Buzz');
	} else {
		console.log(i);
	}
}

// Доделаю попозже с браузером задачки!