export default function getStudentsByLocation(students, city) {
<<<<<<< HEAD
=======
  if (!Array.isArray(students)) {
    return [];
  }

>>>>>>> upstream/main
  return students.filter((student) => student.location === city);
}
