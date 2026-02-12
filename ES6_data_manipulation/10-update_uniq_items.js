export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
<<<<<<< HEAD
  
  for (const [key, value] of map.entries()) {
    if (value === 1) {
      map.set(key, 100);
    }
  }
=======

  map.forEach((value, key) => {
    if (value === 1) {
      map.set(key, 100);
    }
  });

>>>>>>> upstream/main
  return map;
}
