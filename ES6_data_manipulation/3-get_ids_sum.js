export default function getStudentIdsSum(students) {
<<<<<<< HEAD
=======
  if (!Array.isArray(students)) {
    return 0;
  }

>>>>>>> upstream/main
  return students.reduce((sum, student) => sum + student.id, 0);
}
