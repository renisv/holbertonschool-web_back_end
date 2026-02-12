export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
<<<<<<< HEAD
  const dataView = new DataView(buffer);

  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  dataView.setInt8(position, value);
  return dataView;
=======
  const view = new DataView(buffer);

  if (position >= length || position < 0) {
    throw new Error('Position outside range');
  }

  view.setInt8(position, value);

  return view;
>>>>>>> upstream/main
}
