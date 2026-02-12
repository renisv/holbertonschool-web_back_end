<<<<<<< HEAD
export default function getListStudentIds(idArray) {
  if (!Array.isArray(idArray)) {
    return [];
  }
  return idArray.map((student) => student.id);
=======
export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  return students.map((student) => student.id);
>>>>>>> upstream/main
}
