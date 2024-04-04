function linearSearch(array, element) {
    if (array.length === 0) {
        return "emptyArray";
    }

    for (let i = 0; i < array.length; i++) {
        if (array[i] === element) {
            return `Element Found at index ${i} ==> position ${i+1}`;
        }
    }
    return "Element was not found";
}


let array = [4, 6, 1, 3, 8, 0, 2, 5, 9];
const target = 31;

const searchResult = linearSearch(array, target);
console.log(searchResult);