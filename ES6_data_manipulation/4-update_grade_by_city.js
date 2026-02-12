export default function updateStudentGradeByCity(students, city, newGrades) {
<<<<<<< HEAD
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
      return {
        ...student,
        grade: gradeObj ? gradeObj.grade : 'N/A'
=======
  if (!Array.isArray(students)) {
    return [];
  }

  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeObj = newGrades.find(
        (grade) => grade.studentId === student.id,
      );

      return {
        ...student,
        grade: gradeObj ? gradeObj.grade : 'N/A',
>>>>>>> upstream/main
      };
    });
}
