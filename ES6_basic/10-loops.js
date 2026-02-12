export default function appendToEachArrayValue(array, appendString) {
<<<<<<< HEAD
  for (const value of array) {
    const idx = array.indexOf(value);
    array[idx] = appendString + value;
  }

  return array;
=======
    for (const value of array) {
        const idx = array.indexOf(value);
        array[idx] = appendString + value;
    }

    return array;
>>>>>>> upstream/main
}
